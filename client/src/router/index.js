import Vue from 'vue';
import Router from 'vue-router';
import Ping from '../components/Ping.vue';
import Disasters from '../components/Disasters.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Disasters',
      component: Disasters,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
