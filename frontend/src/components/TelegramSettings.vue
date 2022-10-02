<template>
  <br/>
  <br/>
  <MDBContainer>
    <MDBCard>
      <MDBCardBody>
        <MDBCardTitle>Connectivity settings</MDBCardTitle>
        <MDBCardText>
          <MDBInput v-model="token" label="Bot token" @change="setUnsaved()"/>
          <br/>
          <MDBInput v-model="chatId" label="Chat ID" @change="setUnsaved()"/>
        </MDBCardText>
        <MDBBtn color="primary" @click="saveSettings">Save</MDBBtn>
        <MDBBtn :disabled="saved === false" color="primary" @click="testSettings">Test</MDBBtn>
      </MDBCardBody>
    </MDBCard>
    <br/>
    <br/>
    <MDBCard>
      <MDBCardBody>
        <MDBCardTitle>Notification settings</MDBCardTitle>
        <MDBCardText>
          <MDBAccordion v-model="activeItem">
            <MDBAccordionItem v-for="(event, eventName) in notifications" :key="eventName"
                              :collapseId="eventName"
                              :headerTitle="getTitle(event)">
              <ul>
                <li v-for="(statusValue, statusName) in event.statuses" :key="statusName">
                  <MDBSwitch
                      v-model="notifications[eventName].statuses[statusName]"
                      :label="statusName"
                      @click="saveNotifications(eventName, statusName)"
                  />
                  <span v-if="spinners[eventName][statusName]" class="requestSaved">Saved!</span>
                </li>
              </ul>
            </MDBAccordionItem>
          </MDBAccordion>
        </MDBCardText>
      </MDBCardBody>
    </MDBCard>
  </MDBContainer>
</template>

<script>
import {
  MDBAccordion,
  MDBAccordionItem,
  MDBBtn,
  MDBCard,
  MDBCardBody,
  MDBCardText,
  MDBCardTitle,
  MDBContainer,
  MDBInput,
  MDBSwitch,
} from "mdb-vue-ui-kit";
import {ref} from "vue";

export default {
  name: "TelegramSettings",
  components: {
    MDBCard,
    MDBCardBody,
    MDBCardTitle,
    MDBCardText,
    MDBBtn,
    MDBContainer,
    MDBInput,
    MDBAccordion,
    MDBAccordionItem,
    MDBSwitch,
  },
  data() {
    return {
      token: '',
      chatId: '',
      notifications: {},
      saved: true,
      spinners: []
    }
  },
  setup() {
    const activeItem = ref('collapseOne');
    return {
      activeItem
    }
  },
  async created() {
    await fetch('/api/settings').then(installation => {
    this.token = installation['token']
    this.chatId = installation['chatId']
    this.notifications = installation['notifications']

    for (let eventKey in this.notifications) {
      this.spinners[eventKey] = {}
      for (let statusKey in this.notifications[eventKey]['statuses']) {
        this.spinners[eventKey][statusKey] = false
      }
    }
    })

  },
  methods: {
    setUnsaved() {
      this.saved = false
    },
    saveNotifications(eventName, statusName) {
      setTimeout(() => {
        this.makeRequest()
        this.spinners[eventName][statusName] = true
        setTimeout(() => {
          this.spinners[eventName][statusName] = false
        }, 2000)
      }, 3000)
    },
    saveSettings(e) {
      e.preventDefault()
      this.makeRequest()
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
          .then(() => {
            alert('saved')
            this.saved = true
          });
    },
    getTitle(event) {
      let countStatusesEnabled = 0
      for (let eventStatus in event.statuses) {
        if (event.statuses[eventStatus]) {
          countStatusesEnabled++
        }
      }
      return event.title + ' ('+countStatusesEnabled+' of '+Object.keys(event.statuses).length+' enabled)'
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.form-switch {
  display: inline-block;
  margin-right: 10px;
}

.requestSaved {
  color: #6A9955
}
</style>
