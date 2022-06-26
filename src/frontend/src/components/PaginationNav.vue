<template>
  <paginate
    :page-count="totalPageNumber"
    :prev-text="'＜'"
    :next-text="'＞'"
    :click-handler="fetchPostWithNumber"
    :container-class="'pagination'"
    :prev-link-class="'page-link prev'"
    :next-link-class="'page-link next'"
  ></paginate>
</template>

<script>
import axios from "axios";
import Paginate from "vuejs-paginate-next";

export default {
  props: {
    totalPageNumber: {
      required: false,
    },
  },

  components: {
    paginate: Paginate,
  },

  methods: {
    // 任意ページの記事一覧を取得
    async fetchPostWithNumber(pageNum) {
      await axios
        .get(`http://localhost/api/posts/?page=${pageNum}`)
        .then((response) => {
          this.$store.commit("setPosts", response.data);
        })
        .catch((error) => {
          console.log("axiosGetErr", error);
        });
    },
  },
};
</script>

<style lang="scss">
@import "../assets/styles/responsive";
@import "../assets/styles/ease";
@import "../assets/styles/basecolor";

// 共通スタイル
@include responsive(xs) {
  .pagination {
    position: relative;
    left: 50%;
    top: 50%;
    transform: translate(-50%, 0%);
    margin: 0;
    padding: 10px;
    background-color: $secondaryColor;
    // border-radius: 40px;
    // box-shadow: 0 5px 25px 0 rgba(0,0,0,.5);

    .page-item {
      display: inline-block;
      list-style: none;
    }

    .page-link {
      display: block;
      font-weight: bold;
      width: 35px;
      height: 35px;
      line-height: 35px;
      background-color: #fff;
      text-align: center;
      text-decoration: none;
      color: $paragraphColor;
      border-radius: 4px;
      margin: 5px;
      border: 3px $buttonColor solid;
      transition: all 0.2s ease;

      @include responsive(md) {
        &:hover,
        &.active {
          color: $secondaryColor;
          background-color: $buttonColor;
        }
      }
    }
  }
}
</style>
