import { createRouter, createWebHashHistory } from 'vue-router';
import ProfilePage from '@/views/ProfilePage.vue';
import HistoryPage from '@/views/HistoryPage.vue';
import statistics from '@/views/Statistics.vue';
import test from '@/views/test.vue';
import Auth from '@/views/Auth.vue';
const routes = [
  { path: '/', redirect: '/profile' },
  { path: '/profile', component: ProfilePage },
  { path: '/history', component: HistoryPage },
  { path: '/statistics', component: statistics },
  { path: '/test', component: test },
  { path: '/auth', component: Auth },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
