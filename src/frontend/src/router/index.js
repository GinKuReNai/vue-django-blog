import * as vueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Articles from '../views/Articles.vue';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home, 
    },
    {
        path: '/articles',
        name: 'Articles',
        component: Articles,
    }
]

const router = vueRouter.createRouter({
    // mode: createWebHistory(process.env.BASE_URL),
    history: vueRouter.createWebHistory(),
    routes,
})

export default router