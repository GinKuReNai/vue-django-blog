<template>
  <div class="home">
    <div class="home_description">
      <h1>Title</h1>
      <p class="description">Software Engineer Tech Blog</p>
    </div>
    <div class="home_content">
      <div class="home_inner">
        <!-- 記事カードを表示 -->
        <div class="post-card" v-for="value in posts" :key="value.id">
          <PostCard :post="value" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PostCard from "../components/PostCard.vue";

export default {
  components: {
    PostCard,
  },
  data() {
    return {
      posts: [],
    };
  },
  mounted() {
    this.axios
      .get("http://localhost:80/api/posts/")
      .then((response) => {
        console.log("status: ", response.status);
        console.log("axiosGetData: ", response.data);
        this.posts = response.data.results;
      })
      .catch((err) => {
        console.log("axiosGetErr", err);
      });
  },
};
</script>

<style lang="scss"></style>
