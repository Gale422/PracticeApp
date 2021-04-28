<template>
  <v-container>
    <page-title>Home</page-title>
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
        <template #[`item.title`]="{ item }">
          <NuxtLink :to="`todo/details/${item.id}`">{{ item.title }}</NuxtLink>
        </template>
        <template #[`item.tags`]="{ item }">
          <v-chip-group>
            <v-chip v-for="tag in item.tags" :key="tag.name">
              {{ tag.name }}
            </v-chip>
          </v-chip-group>
        </template>
        <template #[`item.start_time`]="{ item }">
          <span class="time">{{ formatDate(item.start_time) }}</span>
        </template>
        <template #[`item.end_time`]="{ item }">
          <span class="time">{{ formatDate(item.end_time) }}</span>
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
import PageTitle from '@/components/PageTitle.vue';
import DataTableHeader, { Option } from '@/content/DataTableHeader';

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
        new DataTableHeader('タイトル', 'title'),
        new DataTableHeader('開始時刻', 'start_time', new Option('center')),
        new DataTableHeader('終了時刻', 'end_time', new Option('center')),
        new DataTableHeader('タグ', 'tags', new Option('center', 400)),
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
        .get('/data', {
          params: {
            search: '検索条件',
          },
        })
        .then((result) => result.data)
        .catch((): any[] => []);
    },
    formatDate(strDate: string): string {
      if (!strDate) {
        return '未定';
      }
      const date: Array<string> = strDate
        .split(/[-\s:]/)
        .map((e) => `${parseInt(e)}`.padStart(2));
      return `${date[0]}年 ${date[1]}月 ${date[2]}日 ${date[3]}時 ${date[4]}分`;
    },
  },
});
</script>

<style scoped>
.data-table {
  width: 100%;
}
.time {
  white-space: pre-wrap;
}
</style>
