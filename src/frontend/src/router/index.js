import * as vueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Post from '../views/Post.vue';

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home, 
    },
    {
        path: '/post/:slug',
        name: 'post_detail',
        component: Post,
    },
]

const router = vueRouter.createRouter({
    // mode: createWebHistory(process.env.BASE_URL),
    history: vueRouter.createWebHistory(),
    routes,
})

export default router