<template>
  <main class="home">
    <!-- タイトル / 説明 -->
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
    <!-- ページネーション -->
    <nav class="home_nav">
      <!-- ページ内カード数の表示 -->
      <p>{{ postCount }}件中 {{ postRangeFirst }}～{{ postRangeLast }}件を一覧表示</p>
      <!-- ページ遷移ナビゲーション -->
      <PaginationNav :totalPageNumber="Number(postTotalPageNumber)" />
    </nav>
    <!-- サイドバー -->
    <section class="home_sidebar">
      <Sidebar :profiles="getProfileList" :tags="getTagList" :categories="getCategoryList" />
    </section>
  </main>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

import PostCard from "../components/PostCard.vue";
import PaginationNav from "../components/PaginationNav.vue"
import Sidebar from "../components/Sidebar.vue"

export default {

  components: {
    PostCard,
    PaginationNav,
    Sidebar,
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
      'getProfileList',
      'getTagList',
      'getCategoryList',
    ]),
  },

  methods: {
    ...mapActions([
      'fetchPosts',
      'fetchProfile',
      'fetchTags',
      'fetchCategories',
    ]),
  },

  mounted() {
    // ページ読み込みの初めに1ページ目の記事一覧を取得
    this.$store.dispatch('fetchPosts')
    // サイドバーにプロフィール・タグ・カテゴリーのデータを渡す
    this.$store.dispatch('fetchProfile')
    this.$store.dispatch('fetchTags')
    this.$store.dispatch('fetchCategories')
  },
};
</script>

<style lang="scss">
@import "../assets/styles/responsive";
@import "../assets/styles/ease";
@import "../assets/styles/basecolor";


@include responsive(md) {
  .home {
    background-color: rgb(255, 227, 227);
    &_description {
      background-color: $secondaryColor;
      height: 100px;
      border-bottom: 1px $strokeColor solid;
    } 

    &_content, &_sidebar {
      background-color: $secondaryColor;
      width: 700px;
      margin: 0 auto;
      padding: 1px;
      border-radius: 6px;
      
      @include responsive(md) {
        position: relative;
      }
    }
    
    &_nav {
      background-color: $secondaryColor;
    }
  }
}
</style>
