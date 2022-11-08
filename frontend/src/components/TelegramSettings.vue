<template>
  <MDBContainer>
    <MDBCard>
      <MDBCardBody>
        <MDBCardTitle>Connectivity settings</MDBCardTitle>
        <MDBCardText>
          <MDBInput v-model="token" label="Bot token" @change="setUnsaved()"/>
          <br/>
          <MDBInput v-model="chatId" label="Chat ID" @change="setUnsaved()"/>
        </MDBCardText>
        <MDBBtn :disabled="saving" color="primary" @click.prevent="saveSettings">Save</MDBBtn>
        <MDBBtn :disabled="saved === false && saving === false" color="primary" @click.prevent="testSettings">Test
        </MDBBtn>
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
              <ul class="switch-group">
                <li v-for="(statusValue, statusName) in event.statuses" :key="statusName" class="switch-group-item">
                  <SettingsItem
                    :value="statusValue"
                    :name="statusName"
                    :loading="getSpinner(eventName, statusName)"
                    @statusChange="(value) => this.handleChange(eventName, statusName, value)"
                  />
                </li>
              </ul>
            </MDBAccordionItem>
          </MDBAccordion>
        </MDBCardText>
      </MDBCardBody>
    </MDBCard>
    <MDBModal
        id="modal"
        v-model="modal"
        labelledby="modalLabel"
        tabindex="-1"
    >
      <MDBModalHeader>
        <MDBModalTitle id="modalLabel"> {{ modalTitle }}</MDBModalTitle>
      </MDBModalHeader>
      <MDBModalBody>{{ modalBody }}</MDBModalBody>
      <MDBModalFooter>
        <MDBBtn color="secondary" @click="modal = false">Ok</MDBBtn>
      </MDBModalFooter>
    </MDBModal>
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
  MDBModal,
  MDBModalBody,
  MDBModalFooter,
  MDBModalHeader,
  MDBModalTitle,
} from "mdb-vue-ui-kit";
import {ref} from "vue";
import SettingsItem from './SettingsItem.vue'

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
    MDBModal,
    MDBModalHeader,
    MDBModalTitle,
    MDBModalBody,
    MDBModalFooter,
    SettingsItem,
  },
  data() {
    return {
      token: '',
      chatId: '',
      notifications: {},
      saved: true,
      saving: false,
      spinners: {},
      modalTitle: "",
      modalBody: ""
    }
  },
  setup() {
    const activeItem = ref('collapseOne');
    const modal = ref(false);
    return {
      activeItem,
      modal
    }
  },
  async created() {
    try {
      const response = await fetch('/api/settings');
      const {token, chatId, notifications} = await response.json();
      this.token = token;
      this.chatId = chatId;
      this.notifications = notifications;
    } catch (error) {
      // TODO: It doesn't catch 500
      this.showError('Request failed: ' + error);
    }
  },
  methods: {
    showError(body = 'Some error') {
      this.modalTitle = 'Error!';
      this.modalBody = body;
      this.modal = true;
    },
    showAlert(body = '') {
      this.modalTitle = 'OK!';
      this.modalBody = body;
      this.modal = true;
    },
    getSpinner(eventName, statusName) {
      return !!(this.spinners[eventName] && this.spinners[eventName][statusName]);
    },
    setSpinner(eventName, statusName, value) {
      if (!this.spinners[eventName]) {
        this.spinners[eventName] = {};
      }
      this.spinners[eventName][statusName] = value;
    },
    setUnsaved() {
      this.saved = false
    },
    async saveSettings() {
      this.saving = true;
      await this.makeRequest(false);
      this.saving = false;
    },
    async testSettings() {
      const requestOptions = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
          message: "This is a test message",
        })
      };
      try {
        await fetch('/api/test-message', requestOptions)
            .then((response) => {
              switch (response.status) {
                case 204:
                case 200:
                  this.showAlert('request successfully sent!');
                  return;
                case 400:
                case 401:
                case 500:
                default:
                  response.json()
                      .then((json) => {
                        this.showError('Request failed: ' + json.detail);
                      })
            }})
      } catch (error) {
        this.showError('Request failed: ' + error);
      }
    },
    async handleChange(eventName, statusName, value) {
      console.log(eventName)
      console.log(statusName)
      console.log(value)


      this.notifications[eventName].statuses[statusName] = value;
      this.setSpinner(eventName, statusName, true);
      await this.makeRequest(true);
      this.setSpinner(eventName, statusName, false);
    },
    async makeRequest(silent) {
      let requestOptions = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
          token: this.token,
          chatId: this.chatId,
          notifications: this.notifications
        })
      };
      try {
        await fetch('/api/settings', requestOptions);
        if (!silent) {
          this.showAlert('Settings saved!');
        }
        this.saved = true
      } catch (error) {
        this.showError('Request failed: ' + error);
      }
    },
    getTitle(event) {
      const countStatusesEnabled = Object.keys(event.statuses).map(statusName => event.statuses[statusName]).filter(Boolean).length;
      const countAllStatuses = Object.keys(event.statuses).length;
      return `${event.title} (${countStatusesEnabled} of ${countAllStatuses} enabled)`
    }
  }
};
</script>

<style scoped>
.switch-group .switch-group-item {
  list-style-type: none;
}
</style>
