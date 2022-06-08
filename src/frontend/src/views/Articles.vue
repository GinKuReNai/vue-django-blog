<template>
  <div>
    <p>Articles</p>
    <!-- <p>{{ Posts }}</p> -->
    <div v-for="(post, key) in Posts.results" :key="key">
      <p>タイトル: {{ post.title }}</p>
      <p>内容: {{ post.body }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      Posts: [],
    };
  },

  mounted() {
    this.axios
      .get("http://localhost:80/api/posts/")
      .then((response) => {
        console.log("status: ", response.status);
        console.log("axiosGetData: ", response.data);
        this.Posts = response.data;
      })
      .catch((err) => {
        console.log("axiosGetErr", err);
      });
  },
};
</script>

<style></style>
