import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// Fontawesome Icons
import { library } from "@fortawesome/fontawesome-svg-core"
import { faTwitter, faGithub } from "@fortawesome/free-brands-svg-icons"
import { faHouse, faNewspaper, faRss, faCircleInfo } from "@fortawesome/free-solid-svg-icons"
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome"

// Header icons
library.add(faHouse)
library.add(faNewspaper)
library.add(faRss)
library.add(faCircleInfo)
// Footer icons
library.add(faTwitter)
library.add(faGithub)

createApp(App)
    .use(router)
    .use(store)
    .component('font-awesome-icon', FontAwesomeIcon)
    .mount('#app')
