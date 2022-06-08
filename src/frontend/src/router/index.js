import * as vueRouter from 'vue-router';
import Home from '../views/Home.vue';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home, 
    },
]

const router = vueRouter.createRouter({
    // mode: createWebHistory(process.env.BASE_URL),
    history: vueRouter.createWebHistory(),
    routes,
})

export default router