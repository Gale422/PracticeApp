<template>
  <div>
    <page-title>{{ $data.title }}</page-title>
    <v-chip-group>
      <v-chip v-for="tag in $data.tags" :key="tag.name">
        {{ tag.name }}
      </v-chip>
    </v-chip-group>
    <div>予定時刻: {{ $data.start_time }} 〜 {{ $data.end_time }}</div>
    <div>場所: {{ $data.location }}</div>
    <p>{{ $data.detail }}</p>
    <p>{{ $data.other }}</p>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import PageTitle from '@/components/PageTitle.vue';
export default Vue.extend({
  components: { PageTitle },
  data(): {
    id: number | undefined;
    title: string | undefined;
    tags: Array<String> | undefined;
    detail: string | undefined;
    other: object | undefined;
  } {
    return {
      id: undefined,
      title: undefined,
      tags: undefined,
      detail: undefined,
      other: undefined,
    };
  },
  mounted(): void {
    this.$data.id = this.$route.params.id;
    this.getDetail();
  },
  methods: {
    async getDetail(): Promise<void> {
      // .post('/todo/detail', { id: this.$data.id })
      const data: {
        title: string;
        tags: Array<String>;
        detail: string;
      } = await this.$axios
        .get('/todo/detail', {
          params: {
            id: this.$data.id,
          },
        })
        .then((result) => result.data)
        .catch((): any[] => []);
      this.$data.title = data.title;
      this.$data.tags = data.tags;
      this.$data.detail = data.detail;
      this.$data.other = data;
    },
  },
});
</script>
