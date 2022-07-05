<template>
  <main class="post">
    <h1></h1>
    <article>
      <h2></h2>
      <p></p>
      <h2></h2>
      <p></p>
    </article>
  </main>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
        slug: this.$route.params.slug,
    };
  },

  mounted() {
      // 記事の詳細をAPIから取得
      axios.get(`http://localhost/api/posts/${this.slug}/`)
      .then((response) => {
          console.log(response.data)
      })
      .catch((error) => {
          console.log('axiosGetErr', error)
      })
  }
};
</script>

<style></style>
