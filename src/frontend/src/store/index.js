import { createStore } from'vuex'
import axios from 'axios'

export default createStore({
    state: {
        // Axiosで取得した記事データ
        posts: {},
        profile: {},
        tags: {},
        categories: {},
    },
    mutations: {
        // この関数を仲介させてstate.postsを変更
        setPosts(state, responseData) {
            state.posts = responseData
        },
        
        // この関数を仲介させてstate.profileを変更
        setProfile(state, responseData) {
            state.profile = responseData
        },

        // この関数を仲介させてstate.tagsを変更
        setTags(state, responseData) {
            state.tags = responseData
        },
        
        // この関数を仲介させてstate.tagsを変更
        setCategories(state, responseData) {
            state.categories = responseData
        },
    },
    actions: {
        // 非同期処理でAxiosにより記事一覧を取得
        async fetchPostsList(context) {
            await axios.get('http://localhost/api/posts/')
            .then((response) => {
                context.commit('setPosts', response.data)
            })
            .catch((error) => {
                console.log('axiosGetErr', error)
            })
        },

        // 非同期処理でAxiosによりプロフィールを取得
        async fetchProfile(context) {
            await axios.get('http://localhost/api/profile/')
            .then((response) => {
                context.commit('setProfile', response.data)
            })
            .catch((error) => {
                console.log('axiosGetErr', error)
            })
        },

        // 非同期処理でAxiosによりタグ一覧を取得
        async fetchTags(context) {
            await axios.get('http://localhost/api/posts/tag/')
            .then((response) => {
                console.log(response.data)
                context.commit('setTags', response.data)
            })
            .catch((error) => {
                console.log('axiosGetErr', error)
            })
        },
        
        // 非同期処理でAxiosによりカテゴリー一覧を取得
        async fetchCategories(context) {
            await axios.get('http://localhost/api/posts/category/')
            .then((response) => {
                console.log(response.data)
                context.commit('setCategories', response.data)
            })
            .catch((error) => {
                console.log('axiosGetErr', error)
            })
        },
       
    },
    modules: {

    },
    getters: {
        // state.postsからPaginationの各種情報を取得
        getPreviousURL(state) {
            return state.posts.previous
        },

        getNextURL(state) {
            return state.posts.next
        },

        hasPrevious(state) {
            return !!state.posts.previous
        },

        hasNext(state) {
            return !!state.posts.next
        },

        postRangeFirst(state) {
            return state.posts.range_first
        },

        postRangeLast(state) {
            return state.posts.range_last
        },

        postCurrentPageNumber(state) {
            return state.posts.current_page
        },

        postTotalPageNumber(state) {
            return state.posts.total_pages
        },

        postCount(state) {
            return state.posts.count
        },

        postList(state) {
            return state.posts.results
        },
        
        // state.profileからプロフィール情報を取得
        getProfileList(state) {
            return state.profile
        },
        
        // state.tagsからタグ一覧を取得
        getTagList(state) {
            return state.tags
        },

        // state.categoriesからカテゴリー一覧を取得
        getCategoryList(state) {
            return state.categories
        },
    }
})

