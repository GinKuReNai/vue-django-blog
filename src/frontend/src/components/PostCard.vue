<template>
  <div class="card">
    <div class="card_container">
      <div class="card_inner">
        <h1>{{ post.title }}</h1>
        <p>PostCard</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  // Homeから記事データを受け渡し
  props: {
    post: {
      required: false,
      default: null,
    },
  },
};
</script>

<style lang="scss" scoped></style>
