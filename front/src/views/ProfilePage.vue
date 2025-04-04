<script setup>
import location from '@/svg/location.vue';
import FooterNav from '@/components/FooterNav.vue';
// import { onMounted } from 'vue';

// onMounted(async () = {
  
// })

</script>

<template>
  <FooterNav/>
  <div class="container">
    <div class="title">
      <span>Ваш профиль</span>
    </div>

    <div class="avatar">
      <img src="/test/avatar.jpg" />
      <div class="name">Иван Иванов, 28</div>
      <div class="city">
        <location></location>
        Москва
      </div>
    </div>

    <div class="about">
      <span class="title_about">О себе</span>
     
      <span class="about_text"
        >Люблю путешествовать, читать книги и заниматься спортом. Работаю в IT
        компании. Ищу человека с похожими интересами.</span
      >
    </div>

    <div class="settings">
      <span class="title_settings">Настройки профиля</span>
      
      <div class="edit_profile">
        <span>Редактировать профиль</span>
      </div>

      <div class="edit_profile">
        <span>Настройки профиля</span>
      </div>

      <!-- <div class="edit_profile">
        <span>Редактировать профиль</span>
      </div> -->
    </div>
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
  }

  .about {
    display: flex;
    flex-direction: column;
    margin-top: 10px;
    width: 90%;

    .title_about {
      font-family: "Inter", sans-serif;
      font-weight: 500;
      font-size: 1.125rem;
      line-height: 1.75rem;
     
    }
    .about_text {
      color: #65758b;
      margin-top: 5px;
 
    }
  }

  .settings{
    margin-top: 25px;
   
    .title_settings{
      font-size: 16px;
      font-weight: 500;
      margin-top: 15px;
      font-size: 1.125rem;
      line-height: 1.75rem;
      ;
    }
    .edit_profile{
      margin-top: 10px;
      width: 80%;
      background-color: #F1F5F9;
      padding: 13px;
      border-radius: 15px;
      color: #65758b;
     
    }
   
  }
}
</style>
