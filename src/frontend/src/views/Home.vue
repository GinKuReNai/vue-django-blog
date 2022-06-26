<template>
  <main class="home">
    <div class="home_description">
      <h1>Title</h1>
      <p class="description">Software Engineer Tech Blog</p>
    </div>
    <!-- 記事一覧 -->
    <section class="home_content">
      <!-- 記事カードを表示 -->
      <div class="post-card" v-for="value in postList" :key="value.id">
        <PostCard :post="value" />
      </div>
    </section>
    <!-- ページ内カード数の表示 -->
    <div class="home_lead">
      <p>{{ postCount }}件中 {{ postRangeFirst }}～{{ postRangeLast }}件を一覧表示</p>
    </div>
    <!-- ページ遷移ナビゲーション -->
    <nav class="home_nav">
      <PaginationNav :totalPageNumber="Number(postTotalPageNumber)" />
    </nav>
  </main>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

import PostCard from "../components/PostCard.vue";
import PaginationNav from "../components/PaginationNav.vue"

export default {

  components: {
    PostCard,
    PaginationNav,
  },

  computed: {
    // Responseの各種情報を取得するゲッター
    ...mapGetters([
      'postList',
      'postCount',
      'postRangeFirst',
      'postRangeLast',
      'postCurrentPageNumber',
      'postTotalPageNumber',
      'hasPrevious',
      'hasNext',
      'getPreviousURL',
      'getNextURL',
    ]),
  },

  methods: {
    ...mapActions(['fetchPostsAction']),
  },

  mounted() {
    // ページ読み込みの初めに1ページ目の記事一覧を取得
      this.$store.dispatch('fetchPostsAction')
  },
};
</script>

<style lang="scss">
@import "../assets/styles/responsive";
@import "../assets/styles/ease";
@import "../assets/styles/basecolor";


@include responsive(md) {
  .home {
    &_description {
      height: 100px;
    } 

    &_content {
      width: 700px;
      margin: 0 auto;
    }
  }
}
</style>
