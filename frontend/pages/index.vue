<template>
  <v-container>
    <PageTitle value="Home" />
    <v-row justify="center" align="center">
      <v-data-table
        :show-select="true"
        :headers="headers"
        :items="items"
        item-key="id"
        loding
        loding-text="now loding..."
        class="data-table"
      >
        <template #[`item.name`]="{ item }">
          <a :href="item.url">{{ item.name }}</a>
        </template>
        <template #[`item.zip`]>
          <v-icon>mdi-download</v-icon>
        </template>
      </v-data-table>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import PageTitle from '../components/PageTitle.vue';
import DataTableHeader, { Option } from '../content/DataTableHeader';

export default Vue.extend({
  components: {
    PageTitle,
  },
  data() {
    return {
      items: [],
    };
  },
  computed: {
    headers(): DataTableHeader[] {
      return [
        new DataTableHeader('id', 'id'),
        new DataTableHeader('名前', 'name'),
        new DataTableHeader('種類', 'type'),
        new DataTableHeader('', 'zip', new Option('center', 30, false, false)),
      ];
    },
  },
  mounted(): void {
    this.getItems();
  },
  methods: {
    async getItems(): Promise<void> {
      this.$data.items = await this.$axios
        .$get('/data', {
          params: {
            search: '検索条件',
          },
        })
        .catch((): any[] => []);
    },
  },
});
</script>

<style scoped>
.data-table {
  width: 100%;
}
</style>
