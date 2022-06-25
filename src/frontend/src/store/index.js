import { createStore } from'vuex'
import axios from 'axios'

export default createStore({
    state: {
        // Axiosで取得した記事データ
        posts: {}
    },
    mutations: {
        // この関数を仲介させてstate.postsを変更
        setPosts(state, responseData) {
            state.posts = responseData
        }
    },
    actions: {
        // 非同期処理でAxiosにより記事一覧を取得
        async fetchPostsAction(context) {
            await axios.get('http://localhost/api/posts/')
            .then((response) => {
                context.commit('setPosts', response.data)
            })
            .catch((error) => {
                console.log('axiosGetErr', error)
            })
        }

    },
    modules: {

    },
    getters: {
        // postsからPaginationの各種情報を取得
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

        postCount(state) {
            return state.posts.count
        },

        postList(state) {
            return state.posts.results
        },
    }
})

