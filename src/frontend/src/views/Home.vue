<template>
  <div class="home">
    <p>ここは私のホームページだよ！！</p>
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

<style lang="scss"></style>
