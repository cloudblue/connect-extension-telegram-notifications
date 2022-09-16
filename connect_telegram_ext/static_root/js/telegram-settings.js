import createApp from '/static/js/index-dev.js';

createApp({});

export default {
    data() {
        return {
            token: '',
            chatId: '',
        }
    },
    created() {
        // fetch on init
        this.fetchData()
    },
    methods: {
        save(e) {
            e.preventDefault()
            const requestOptions = {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({
                    token: this.token,
                    chatId: this.chatId,
                })
            };
            fetch('/settings', requestOptions)
                .then(response => response.json())
                .then(data => (alert('saved')));
        },
        async fetchData() {
            const installation = await (await fetch('/settings')).json()
            this.token = installation['settings']['token']
            this.chatId = installation['settings']['chatId']
        }
    },
    template: `
      <div class="card">
        <h2 class="title">Telegram settings</h2>
        <h3 class="subtitle"><label for="token">Bot token</label></h3>
        <input id="token" v-model="token" placeholder="Place your bot's token here"><br />
    
        <h3 class="subtitle"><label for="chatId">Chat ID</label></h3>
        <input id="chatId" v-model="chatId" placeholder="Place your chat id here">
        
        <button @click="save">Save settings</button>
      </div>
  `,
}