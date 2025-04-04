<script setup>
import avatar from "@/components/avatar.vue";
import heart from "@/svg/heart.vue";
import dislike from "@/svg/dislike.vue";
const props = defineProps({
  action: String,
});
</script>

<template>
  <div class="card">
    <div class="info">
      <div
        :class="{
          action_like: action === 'like',
          action_dislike: action === 'dislike',
        }"
      >
        <heart v-if="action === 'like'" />
        <dislike v-else-if="action === 'dislike'" />
      </div>
      <div class="date">
        <span>10/15/2023</span>
      </div>
    </div>
    <div class="avatar">
      <avatar></avatar>
    </div>
    <div class="description"></div>
  </div>
</template>

<style scoped lang="scss">
.card {
  margin-top: 20px;
  .info {
    display: flex;
    gap: 10px;
    align-items: center;
    margin-left: 5px;

    .action_like {
      background-color: #dcfce7;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 5px;
    }
    .action_dislike {
      background-color: #fee2e2;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 5px;
    }
  }
  .date {
    font-size: 12px;
  }
  .avatar{
    margin-top: 5px;
  }
}
</style>
