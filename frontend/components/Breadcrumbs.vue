<template>
  <span>
    <v-breadcrumbs :items="items" divider="/">
      <template #item="{ item }">
        <li>
          <NuxtLink
            :to="item.href"
            :disabled="item.disabled"
            class="breadcrumbItems"
          >
            {{ item.text }}
          </NuxtLink>
        </li>
      </template>
    </v-breadcrumbs>
    <v-divider />
  </span>
</template>
<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  props: {
    items: {
      type: Array,
      default: () => {
        return [];
      },
    },
  },
});
</script>
<style scoped>
.breadcrumbItems {
  align-items: center;
  display: inline-flex;
  text-decoration: none;
  transition: 0.3s cubic-bezier(0.25, 0.8, 0.5, 1);
}

a[disabled] {
  color: rgba(255, 255, 255, 0.5);
}
</style>
