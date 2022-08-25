import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// Fontawesome Icons
import { library } from "@fortawesome/fontawesome-svg-core"
import {
    faTwitter,
    faGithub,
    faLinkedin,
} from "@fortawesome/free-brands-svg-icons"
import {
    faHouse,
    faNewspaper,
    faFolder,
    faTags,
    faRss,
    faCircleInfo,
    faPen,
    faFilePen,
    faComments,
    faEarthAsia,
} from "@fortawesome/free-solid-svg-icons"
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome"

// Axios
import axios from 'axios'
import VueAxios from 'vue-axios'
// Pagination
import Paginate from 'vuejs-paginate-next'
// v-html sanitizer
import Vue3Sanitize from 'vue-3-sanitize'

// sanitizer Settings
const overridenOptions = {
    allowedAttributes: {
        'div': ['class', 'id'],
        'p': ['class', 'id'],
        'ul': ['class', 'id'],
    },
}

// Header icons
library.add(faHouse)
library.add(faNewspaper)
library.add(faFolder)
library.add(faTags)
library.add(faRss)
library.add(faCircleInfo)
// Footer icons
library.add(faTwitter)
library.add(faGithub)
// PostCard icons
library.add(faComments)
library.add(faPen)
library.add(faFilePen)
// Side Bar icons
library.add(faEarthAsia)
library.add(faLinkedin)

createApp(App)
    .use(router)
    .use(store)
    .use(VueAxios, axios)
    .use(Paginate)
    .use(Vue3Sanitize, overridenOptions)
    .component('font-awesome-icon', FontAwesomeIcon)
    .mount('#app')
