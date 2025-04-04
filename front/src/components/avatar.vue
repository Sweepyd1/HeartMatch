<script setup>
import location from "@/svg/location.vue";
</script>
<template>
  <div class="avatar">
    <img src="/test/avatar.jpg" />
    <div class="name">Иван Иванов, 28</div>
    <div class="city">
      <location></location>
      Москва
    </div>
  </div>
  <div class="about">
      <br />
      <span class="about_text"
        >Люблю путешествовать, читать книги и заниматься спортом. Работаю в IT
        компании. Ищу человека с похожими интересами.</span
      >
    </div>
</template>

<style scoped lang="scss">
.avatar {
  position: relative;
  img {
    width: 95%;
    height: 30vh;
    border-radius: 20px 20px 0 0;
    object-fit: cover;
  }

  .name,
  .city {
    position: absolute;
    left: 0;
    right: 0;
    padding: 18px 12px;
    color: white;
    font-weight: 700;
    margin-left: 10px;

    font-family: Arial, sans-serif;
  }
  .name {
    bottom: 30px;
    font-size: 24px;
    font-weight: bold;
  }

  .city {
    bottom: 0;
    font-size: 15px;
    opacity: 0.4;
    display: flex;
    align-items: center;
    gap: 5px;
  }
  .about {
    .title {
      font-family: "Inter", sans-serif;
      font-weight: 500;
      font-size: 1.125rem;
      line-height: 1.75rem;
    }
    .about_text {
      color: #65758b;
    }
  }
}
</style>
