<template>
  <v-container>
    <v-row justify="start" align="start">
      <v-col>
        <h1 class="pageTitle">{{ value }}</h1>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  props: {
    value: {
      type: String,
      default: null,
      required: true,
    },
  },
})
</script>
