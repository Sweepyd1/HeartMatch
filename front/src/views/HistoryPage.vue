<script setup>
import FooterNav from "@/components/FooterNav.vue";
import search from "@/svg/search.vue";
import {ref, computed } from 'vue';
import card from "@/components/card.vue";

const selectedTab = ref("all");

const switchTab = (tab)=> {
    selectedTab.value = tab;
}

const cards = ref([
  { id: 1, action: 'dislike' },
  { id: 2, action: 'like' },
  { id: 3, action: 'like' },
  { id: 4, action: 'like' },
  { id: 5, action: 'dislike' },
  { id: 6, action: 'like' },
  { id: 7, action: 'like' },
  { id: 8, action: 'like' },
  { id: 9, action: 'dislike' },
  { id: 10, action: 'like' },
  { id:11, action: 'like' },
  { id: 12, action: 'like' },
]);

const filteredCards = computed(() => {
  if (selectedTab.value === 'all') return cards.value;
  return cards.value.filter(card => card.action === selectedTab.value);
});

</script>

<template>
  <FooterNav />
  <div class="container">
    <div class="title">
      <span>История</span>
    </div>

    <div class="search-container">
      <search class="search-icon"></search>

      <input type="text" placeholder="Поиск..." class="search-input" />
    </div>

    <div class="select-container">
      <div class="all"
       :class="{ active_all: selectedTab === 'all' }"
        @click="switchTab('all')"
      >
        <span>Все</span>

      </div>
      <div class="like"
       :class="{ active_like: selectedTab === 'like' }"
        @click="switchTab('like')"
      >
        <span>Лайки</span>

      </div>
      <div class="dislike" 
      :class="{ active_dislike: selectedTab === 'dislike' }"
       @click="switchTab('dislike')"
      >
        <span>Дизлайки</span>

      </div>
    </div>

    <card 
    v-for="card in filteredCards" 
    :key="card.id" 
    :action="card.action" 
  />
   
  </div>
</template>

<style scoped lang="scss">
span {
  font-family: Arial, sans-serif;
}
.container {
  margin-left: 10px;
  width: 100%;
  height: 100vh;

  .title {
    margin: 40px 0 20px 0;
    color: black;
    font-weight: 700;
    font-size: 24px;
  }
  .search-container {
    position: relative;

    margin: 0 auto;
  }

  .search-icon {
    position: absolute;
    left: 12px;
    top: 50%;
    transform: translateY(-50%);
    width: 20px;
    height: 20px;
    pointer-events: none; /* Чтобы клики проходили сквозь иконку */
    color: #666; /* Цвет иконки */
  }

  .search-input {
    width: 80%;
    padding: 12px 16px 12px 40px; /* Левый отступ для иконки */
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 16px;
    transition: all 0.3s ease;
  }

  .search-input:focus {
    outline: none;
    border-color: #2196f3;
    box-shadow: 0 0 0 2px rgba(33, 150, 243, 0.2);
  }
  .select-container{
    margin-top: 25px;
    display: flex;
    gap: 20px;
    align-items: center;

    .all{
        background: #F1F5F9;
        color: black;
        padding: 12px;
        border-radius: 20px;
        font-size: 14px;
        

    }
    .like{
        background: #F0FDF4;
        color: #24A954;
        padding: 12px;
        border-radius: 20px;
        font-size: 14px;

    }
    .dislike{
        background: #FEF2F2;
        color: #DC2727;
        padding: 12px;
        border-radius: 20px;
        font-size: 14px;

    }
    .active_all{
        color: white;
        background-color: #0F1729;
    }
    .active_like{
        color: white;
        background-color: #22C55E;
    }
    .active_dislike{
        color: white;
        background-color: #EF4444;
    }

}
   
}
</style>
