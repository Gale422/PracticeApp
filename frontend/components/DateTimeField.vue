<template>
  <v-container>
    <v-row align="baseline" class="flex-nowrap">
      <v-text-field
        v-model="year"
        :error="error"
        :error-messages="errorMessage"
        class="align-right"
        @input="setValue"
      />
      年
      <v-text-field
        v-model="month"
        :error="error"
        class="align-right"
        @input="setValue"
      />
      月
      <v-text-field
        v-model="day"
        :error="error"
        class="align-right"
        @input="setValue"
      />
      日
      <v-text-field
        v-model="hour"
        :error="error"
        class="align-right"
        @input="setValue"
      />
      時
      <v-text-field
        v-model="minute"
        :error="error"
        class="align-right"
        @input="setValue"
      />
      分
    </v-row>
  </v-container>
</template>
<script lang="ts">
import Vue from 'vue';

const formatter: Intl.DateTimeFormat = new Intl.DateTimeFormat('ja-JP', {
  timeZone: 'Asia/Tokyo',
  year: 'numeric',
  month: '2-digit',
  day: '2-digit',
  hour: '2-digit',
  minute: '2-digit',
  second: '2-digit',
});

const InvalidStr: string = 'Invalid Date';

export default Vue.extend({
  props: {
    value: {
      type: String,
      required: true,
      default: '',
    },
  },
  data(): {
    year: String;
    month: String;
    day: String;
    hour: String;
    minute: String;
    error: Boolean;
    errorMessage: String;
  } {
    return {
      year: '',
      month: '',
      day: '',
      hour: '',
      minute: '',
      error: false,
      errorMessage: '',
    };
  },
  watch: {
    value(newValue) {
      if (!newValue) {
        return;
      }
      const date: Date = new Date(newValue);
      this.$data.year = date.getFullYear();
      this.$data.month = date.getMonth() + 1;
      this.$data.day = date.getDate();
      this.$data.hour = date.getHours();
      this.$data.minute = date.getMinutes();
    },
  },
  methods: {
    hasEmptyField(): boolean {
      return !(
        this.$data.year &&
        this.$data.month &&
        this.$data.day &&
        this.$data.hour &&
        this.$data.minute
      );
    },
    hasInvalidField(): boolean {
      if (this.hasEmptyField()) {
        return true;
      }
      const year: Number = parseInt(this.$data.year);
      const month: Number = parseInt(this.$data.month);
      const day: Number = parseInt(this.$data.day);
      const hour: Number = parseInt(this.$data.hour);
      const minute: Number = parseInt(this.$data.minute);
      return !(year && month && day && hour && minute);
    },
    clearErrMsg(): void {
      this.$data.error = false;
      this.$data.errorMessage = '';
    },
    setValue(): void {
      this.clearErrMsg();
      if (this.hasInvalidField()) {
        return;
      }
      const newDate: Date = new Date(
        `${this.$data.year}/${this.$data.month}/${this.$data.day} ${this.$data.hour}:${this.$data.minute}:00`
      );
      if (newDate.toString() === InvalidStr) {
        this.$data.error = true;
        this.$data.errorMessage = '不正な日時です。';
      } else {
        this.$emit('input', formatter.format(newDate));
      }
    },
  },
});
</script>
<style scoped>
.align-right >>> input {
  text-align: right !important;
}
</style>
