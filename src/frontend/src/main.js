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

import Paginate from 'vuejs-paginate-next'

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
    .component('font-awesome-icon', FontAwesomeIcon)
    .mount('#app')
