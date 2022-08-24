<template>
  <main class="post">
    <h1>{{ data.title }}</h1>
    <article v-html="data.body">
    </article>
  </main>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
        slug: this.$route.params.slug,
        data: {},
    };
  },

  mounted() {
      // 記事の詳細をAPIから取得
      axios.get(`http://localhost/api/posts/${this.slug}/`)
      .then((response) => {
          this.data = response.data
          console.log(response.data)
      })
      .catch((error) => {
          console.log('axiosGetErr', error)
      })
  }
};
</script>

<style></style>
