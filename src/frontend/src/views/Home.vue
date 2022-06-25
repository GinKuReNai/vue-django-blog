<template>
  <main class="home">
    <div class="home_description">
      <h1>Title</h1>
      <p class="description">Software Engineer Tech Blog</p>
    </div>
    <!-- ページ内カード数の表示 -->
    <div class="home_lead">
      <p>{{ postCount }}件中 {{ postRangeFirst }}～{{ postRangeLast }}件を一覧表示</p>
    </div>
    <!-- 記事一覧 -->
    <section class="home_content">
      <!-- 記事カードを表示 -->
      <div class="post-card" v-for="value in postList" :key="value.id">
        <PostCard :post="value" />
      </div>
    </section>
    <!-- ページ遷移ナビゲーション -->
    <nav class="home_pagenav">
      <a v-if="hasPrevious" @click="fetchPostPrevious()">
        <img src="../assets/back.png">
      </a>
      <span>Page {{ postCurrentPageNumber }}</span>
      <a v-if="hasNext" @click="fetchPostNext()">
        <img src="../assets/next.png">
      </a>
    </nav>
  </main>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'
import axios from 'axios'

import PostCard from "../components/PostCard.vue";

export default {

  components: {
    PostCard,
  },

  computed: {
    // Responseの各種情報を取得するゲッター
    ...mapGetters([
      'postList',
      'postCount',
      'postRangeFirst',
      'postRangeLast',
      'postCurrentPageNumber',
      'hasPrevious',
      'hasNext',
      'getPreviousURL',
      'getNextURL',
    ])
  },

  methods: {
    ...mapMutations(['setPosts']),
    ...mapActions(['fetchPostsAction']),
  
    // 前ページの記事一覧を取得
    async fetchPostPrevious() {
      await axios.get(this.getPreviousURL)
      .then((response) => {
          this.$store.commit('setPosts', response.data)
      })
      .catch((error) => {
          console.log('axiosGetErr', error)
      })
    },
    
    // 次ページの記事一覧を取得
    async fetchPostNext() {
      await axios.get(this.getNextURL)
      .then((response) => {
        this.$store.commit('setPosts', response.data)
      })
      .catch((error) => {
        console.log('axiosGetErr', error)
      })
    },
  },

  mounted() {
    // Axios処理のためstoreからactionsを呼び出す
      this.$store.dispatch('fetchPostsAction')
  },
};
</script>

<style lang="scss">
@import "../assets/styles/responsive";

@include responsive(md) {
  .home {
    &_content {
      width: 700px;
      margin: 0 auto;
    }
  }
}
</style>
