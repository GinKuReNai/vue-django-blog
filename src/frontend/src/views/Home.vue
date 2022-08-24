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
      <div class="home_content_card">
        <PostCard v-for="value in postList" :post="value" :key="value.id" />
      </div>
      <!-- サイドバー -->
      <div class="home_content_sidebar">
        <ProfileCard :profiles="getProfileList" />
        <TagListCard :tags="getTagList" />
        <CategoryListCard :categories="getCategoryList" />
      </div>
    </section>
    <!-- ページネーション -->
    <nav class="home_nav">
      <!-- ページ内カード数の表示 -->
      <p>
        {{ postCount }}件中 {{ postRangeFirst }}～{{
          postRangeLast
        }}件を一覧表示
      </p>
      <!-- ページ遷移ナビゲーション -->
      <PaginationNav :totalPageNumber="Number(postTotalPageNumber)" />
    </nav>
  </main>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

import PostCard from "../components/PostCard.vue";
import PaginationNav from "../components/PaginationNav.vue";
import ProfileCard from "../components/ProfileCard.vue"
import TagListCard from "../components/TagListCard.vue"
import CategoryListCard from "../components/CategoryListCard.vue"

export default {
  components: {
    PostCard,
    PaginationNav,
    ProfileCard,
    TagListCard,
    CategoryListCard,
},

  computed: {
    // Responseの各種情報を取得するゲッター
    ...mapGetters([
      "postList",
      "postCount",
      "postRangeFirst",
      "postRangeLast",
      "postCurrentPageNumber",
      "postTotalPageNumber",
      "hasPrevious",
      "hasNext",
      "getPreviousURL",
      "getNextURL",
      "getProfileList",
      "getTagList",
      "getCategoryList",
    ]),
  },

  methods: {
    ...mapActions([
      "fetchPostsList",
      "fetchProfile",
      "fetchTags",
      "fetchCategories",
    ]),
  },

  mounted() {
    // ページ読み込みの初めに1ページ目の記事一覧を取得
    this.$store.dispatch("fetchPostsList");
    // サイドバーにプロフィール・タグ・カテゴリーのデータを渡す
    this.$store.dispatch("fetchProfile");
    this.$store.dispatch("fetchTags");
    this.$store.dispatch("fetchCategories");
  },
};
</script>

<style lang="scss">
@import "../assets/styles/responsive";
@import "../assets/styles/ease";
@import "../assets/styles/basecolor";

// 共通スタイル
@include responsive(xs) {
  
  .home {
    // text-align: center;
    // タブレット以上で背景を設定
    @include responsive(md) {
      background-color: rgb(255, 227, 227);
    }
    &_description {
      background-color: $secondaryColor;
      height: 100px;
      border-bottom: 1px $strokeColor solid;
      text-align: center;
      // タイトルと説明を中央揃え
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    
    &_content {
      @include responsive(md) {
        display: flex;
        justify-content: center;
        background-color: rgb(255, 227, 227);
      }
      
      &_card {
        background-color: $secondaryColor;
        @include responsive(md) {
          width: 700px;
          margin-right: 50px;
        }
      }
      
      &_sidebar {
        // モバイル時は非表示
        @media screen and (max-width: 767px) {
          display: none;
        }
        width: 400px;
      }
    }
    
    &_nav {
      background-color: $secondaryColor;

      p {
        text-align: center;
      }
    }
  }
}
</style>
