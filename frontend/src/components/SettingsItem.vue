<template>
  <div class="checkbox-wrapper">
    <MDBSwitch
      v-model="status"
      :label="name"
      :disabled="loading"
    />
    <span v-if="loading" class="request-saved"  data-test="loader">Saving...</span>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import {
  MDBSwitch,
} from "mdb-vue-ui-kit";

export default defineComponent({
  name: "SettingsItem",
  components: {
    MDBSwitch,
  },
  data() {
    return {
      status: this.value,
    }
  },
  props: ['name', 'value', 'loading'],
  watch: {
    status: {
      handler() {
        this.$emit('statusChange', this.status);
      }
    }
  },
});
</script>

<style scoped>
.checkbox-wrapper {
  display: flex;
}
.request-saved {
  color: #6A9955;
  margin-left: 20px;
}
</style>
