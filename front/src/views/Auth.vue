<template>
<input placeholder="введите свой id" v-model="id">
<button @click="check_user">отправить</button>

</template>

<script setup>
import { ref } from 'vue';

const id = ref();
async function check_user(){
    console.log(id.value)
}
</script>