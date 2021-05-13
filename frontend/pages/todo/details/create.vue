<template>
  <div>
    <breadcrumbs :items="breadcrumbs" />
    <page-title>TODO 作成</page-title>
    <v-card>
      <v-card-text>
        <v-container>
          <v-row
            align="center"
            align-content="space-around"
            dense
            justify="start"
          >
            <v-col cols="1" class="title-column">タイトル</v-col>
            <v-col><v-text-field v-model="todoData.title" /></v-col>
          </v-row>
          <v-row
            align="center"
            align-content="space-around"
            dense
            justify="start"
          >
            <v-col cols="1" class="title-column">タグ</v-col>
            <v-col>
              <v-chip-group multiple :value="selectedTagIndex">
                <v-chip v-for="tag in tags" :key="tag.name" filter>
                  {{ tag.name }}
                </v-chip>
              </v-chip-group>
            </v-col>
            <v-spacer />
            <v-col cols="1">
              <v-btn @click="showCreateTagDialog">タグ作成</v-btn>
            </v-col>
          </v-row>
          <v-row
            align="center"
            align-content="space-around"
            dense
            justify="start"
          >
            <v-col cols="1" class="title-column">予定時刻</v-col>
            <v-col>
              <v-text-field v-model="todoData.start_time" />
            </v-col>
            <v-col cols="1" align-self="center" class="text-center">〜</v-col>
            <v-col>
              <v-text-field v-model="todoData.end_time" />
            </v-col>
          </v-row>
          <v-row
            align="center"
            align-content="space-around"
            dense
            justify="start"
          >
            <v-col cols="1" class="title-column">場所</v-col>
            <v-col><v-text-field v-model="todoData.location" /></v-col>
          </v-row>
          <v-row
            align="center"
            align-content="space-around"
            dense
            justify="start"
          >
            <v-col cols="1" class="title-column">詳細</v-col>
            <v-col><v-textarea v-model="todoData.detail" /></v-col>
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
    todoData: Object;
    tags: Array<Object>;
    selectedTagIndex: Array<Number>;
  } {
    return {
      todoData: {
        title: '',
      },
      tags: [],
      selectedTagIndex: [],
    };
  },
  computed: {
    breadcrumbs(): Array<Object> {
      return [
        {
          text: 'Home',
          href: '/',
        },
        {
          text: 'TODO 作成',
          href: `/todo/details/create`,
          disabled: true,
        },
      ];
    },
  },
  mounted(): void {
    this.getTags();
  },
  methods: {
    async getTags(): Promise<void> {
      this.$data.tags = await this.$axios
        .get('/tags')
        .then((result) => result.data)
        .catch(() => {});
    },
    showCreateTagDialog() {
      // TODO: タグを作成するダイアログを表示するようにする
    },
  },
});
</script>
<style scoped>
.title-column {
  text-align: center;
}
</style>
