<script setup>
import { ref, watch } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import profile from '@/svg/profile.vue';
import statistics from '@/svg/statistics.vue';
import history from '@/svg/history.vue';

const router = useRouter();
const route = useRoute();
const selectedTab = ref(route.path.slice(1) || 'profile');

// Синхронизация с URL при изменении маршрута
watch(() => route.path, (newPath) => {
  const tab = newPath.slice(1);
  if (['profile', 'history', 'statistics'].includes(tab)) {
    selectedTab.value = tab;
  }
});

const switchTab = async (tab) => {
  if (selectedTab.value === tab) return;
  
  try {
    selectedTab.value = tab; // Мгновенное визуальное обновление
    await router.push(`/${tab}`); // Ждем завершения навигации
    
    // Дополнительная проверка после навигации
    if (route.path !== `/${tab}`) {
      selectedTab.value = route.path.slice(1);
    }
  } catch (error) {
    console.error('Navigation error:', error);
    selectedTab.value = route.path.slice(1);
  }
};
</script>

<template>
  <div class="footer">
    <div 
      class="profile tab"
      :class="{ active: selectedTab === 'profile' }"
      @click="switchTab('profile')"
    >
      <profile />
      <span>Профиль</span>
    </div>
    
    <div 
      class="history tab"
      :class="{ active: selectedTab === 'history' }"
      @click="switchTab('history')"
    >
      <history />
      <span>История</span>
    </div>
    
    <div 
      class="statistics tab"
      :class="{ active: selectedTab === 'statistics' }"
      @click="switchTab('statistics')"
    >
      <statistics/>
      <span>Статистика</span>
    </div>
  </div>
</template>

<style scoped lang="scss">
.footer {
  position: fixed;
  bottom: 25px;
  background-color: white;
  width: 90%;
  height: 7vh;
  z-index: 100;
  margin: auto;
  left: 0;
  right: 0;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
  border-radius: 20px;
  display: flex;
  justify-content: space-around;
  align-items: center;

  .tab {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 8px 12px;
    cursor: pointer;
    transition: all 0.3s ease;
    opacity: 0.5;
    transform: scale(0.95);
    -webkit-tap-highlight-color: transparent;

    &.active {
      opacity: 1;
      transform: scale(1);
      span {
        color: black;
        font-weight: 500;
      }
    }

    span {
      font-size: 12px;
      transition: color 0.3s ease;
      margin-top: 2px;
      user-select: none;
    }
  }

  
}
</style>