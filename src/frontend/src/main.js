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
        '*': ['class', 'id'],
        'a': ['href'],
        'img': ['src'],

    },
    allowedTags: [
        "address", "article", "aside", "footer", "header", "h1", "h2", "h3", "h4",
        "h5", "h6", "hgroup", "main", "nav", "section", "blockquote", "dd", "div",
        "dl", "dt", "figcaption", "figure", "hr", "li", "main", "ol", "p", "pre",
        "ul", "a", "abbr", "b", "bdi", "bdo", "br", "cite", "code", "data", "dfn",
        "em", "i", "kbd", "mark", "q", "rb", "rp", "rt", "rtc", "ruby", "s", "samp",
        "small", "span", "strong", "sub", "sup", "time", "u", "var", "wbr", "caption",
        "col", "colgroup", "table", "tbody", "td", "tfoot", "th", "thead", "tr", "img"
    ]
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
