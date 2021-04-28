<template>
  <v-container>
    <v-row justify="start" align="start">
      <v-col>
        <h1 class="pageTitle"><slot /></h1>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({});
</script>
