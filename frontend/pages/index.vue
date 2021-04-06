<template>
  <v-container>
    <PageTitle value="Home" />
    <v-row justify="center" align="center">
      <v-data-table
        :header-props="{ 'single-select': true }"
        :headers="headers"
        :items="items()"
        class="data-table"
      />
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import PageTitle from '../components/PageTitle.vue';
import DataTableHeader from '../content/DataTableHeader';

export default Vue.extend({
  components: {
    PageTitle,
  },
  computed: {
    headers(): DataTableHeader[] {
      return [new DataTableHeader('ヘッダー名', 'バリュー')];
    },
  },
  methods: {
    items(): object[] {
      this.$axios.$get('/data', {
        params: {
          search: '検索条件',
        },
      });
      return [
        {
          バリュー: 'item1',
        },
      ];
    },
  },
});
</script>

<style scoped>
.data-table {
  width: 100%;
}
</style>
