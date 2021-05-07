<template>
  <div>
    <breadcrumbs :items="breadcrumbs" />
    <page-title>{{ $data.todoData.title }}</page-title>
    <v-chip-group>
      <v-chip v-for="tag in $data.todoData.tags" :key="tag.name">
        {{ tag.name }}
      </v-chip>
    </v-chip-group>
    <v-card>
      <v-card-text>
        <v-container>
          <v-row
            align="center"
            align-content="space-around"
            dense
            justify="start"
          >
            <v-col cols="1" class="title-column">予定時刻</v-col>
            <v-col>{{ showTimeSchedule }}</v-col>
          </v-row>
          <v-row
            align="center"
            align-content="space-around"
            dense
            justify="start"
          >
            <v-col cols="1" class="title-column">場所</v-col>
            <v-col>{{ showLocation }}</v-col>
          </v-row>
          <v-row
            align="center"
            align-content="space-around"
            dense
            justify="start"
          >
            <v-col cols="1" class="title-column">詳細</v-col>
            <v-col>{{ $data.todoData.detail }}</v-col>
          </v-row>
          <v-row
            align="center"
            align-content="space-around"
            dense
            justify="start"
          >
            <v-col cols="1" class="title-column">作成日時</v-col>
            <v-col>{{ showTimeStamp }}</v-col>
          </v-row>
        </v-container>
      </v-card-text>
    </v-card>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import PageTitle from '@/components/PageTitle.vue';
import Breadcrumbs from '@/components/Breadcrumbs.vue';
export default Vue.extend({
  components: { PageTitle, Breadcrumbs },
  data(): {
    id: number | undefined;
    todoData: Object;
  } {
    return {
      id: undefined,
      todoData: {
        title: '',
      },
    };
  },
  computed: {
    showTimeSchedule(): string {
      const todoData: any = this.$data.todoData;
      if (!(todoData && (todoData.start_time || todoData.end_time))) {
        return '未定';
      }
      return `${this.formatDate(todoData.start_time) || '未定'} 〜 ${
        this.formatDate(todoData.end_time) || '未定'
      }`;
    },
    showLocation(): string {
      return `${this.$data.todoData.location || '未定'}`;
    },
    showTimeStamp(): string {
      const inserted: string = this.formatDate(this.$data.todoData.inserted_at);
      const updated: string = this.formatDate(this.$data.todoData.updated_at);
      return `${inserted} ${
        inserted !== updated ? `（最終更新時: ${updated} ）` : ``
      }`;
    },
    breadcrumbs(): Array<Object> {
      return [
        {
          text: 'Home',
          href: '/',
        },
        {
          text: 'TODO 詳細',
          href: `/todo/details/${this.$data.id}`,
          disabled: true,
        },
      ];
    },
  },
  mounted(): void {
    this.$data.id = this.$route.params.id;
    this.getDetail();
  },
  methods: {
    async getDetail(): Promise<void> {
      // .post('/todo/detail', { id: this.$data.id })
      this.$data.todoData = await this.$axios
        .get('/todo/detail', {
          params: {
            id: this.$data.id,
          },
        })
        .then((result) => result.data)
        .catch((): object => {
          return {};
        });
    },
    formatDate(strDate: string): string {
      if (!strDate) {
        return '';
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
.title-column {
  text-align: center;
}
</style>
