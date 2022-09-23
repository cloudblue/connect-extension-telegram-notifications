import createApp from '/static/js/index-dev.js';

createApp({});

export default {
    data() {
        return {
            token: '',
            chatId: '',
            notifications: {},
            saved: false
        }
    },
    created() {
        // fetch on init
        this.fetchData()
    },
    methods: {
        makeRequest() {
            let requestOptions = {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({
                    token: this.token,
                    chatId: this.chatId,
                    notifications: this.notifications
                })
            };
            fetch('/api/settings', requestOptions)
                .then(response => response.json())
                .then(data => {
                    alert('saved')
                    this.saved = true
                });
        },
        saveNotifications(e) {
            setTimeout(this.makeRequest, 300)
        },
        saveSettings(e) {
            e.preventDefault()
            this.makeRequest()
        },
        setUnsaved(e) {
            this.saved = false
        },
        testSettings(e) {
            e.preventDefault()
            let requestOptions = {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({
                    message: "This is a test message",
                })
            };
            fetch('/api/test-message', requestOptions)
                .then(response => response.json())
                .then(data => {
                    if (data.status === "FAIL") {
                        alert('request failed: ' + data.error)
                    } else {
                        alert('request successfully sent!')
                    }
                });
        },

        async fetchData() {
            const installation = await (await fetch('/api/settings')).json()
            this.token = installation['token']
            this.chatId = installation['chatId']
            this.notifications = installation['notifications']
        }
    },
    template: `
      <div class="card">
        <h2 class="title">Telegram settings</h2>
        <h3 class="subtitle"><label for="token">Bot token</label></h3>
        <input id="token" v-model="token" @change="setUnsaved()" placeholder="Place your bot's token here"><br /><br />
    
        <h3 class="subtitle"><label for="chatId">Chat ID</label></h3>
        <input id="chatId" v-model="chatId" @change="setUnsaved()" placeholder="Place your chat id here"><br /><br />
        
        <button @click="saveSettings">Save settings</button>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <button @click="testSettings" :disabled="saved === false">Test settings</button>
      </div>
      <div class="card">
        <h2 class="title">Notification settings</h2>
        <ul>
            <li v-for="(event, eventName) in notifications">
                <p>{{ event.title}}</p>
                <ul>
                    <li v-for="(statusValue, statusName) in event.statuses">
                        <label class="form-switch">
                          <input type="checkbox" v-model="notifications[eventName].statuses[statusName]" @click="saveNotifications">
                          <i></i>
                          {{statusName}}
                        </label>
                    </li>
                </ul>
            </li>
        </ul>
      </div>
  `,
}