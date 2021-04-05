<template>
  <v-container>
    <PageTitle value="Home" />
    <v-row>
      <v-col>
        {{ test() }}
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import PageTitle from '../components/PageTitle.vue'

export default Vue.extend({
  components: {
    PageTitle,
  },
  methods: {
    test(): string {
      return 'Hello World'
    },
  },
})
</script>