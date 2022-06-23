<template>
  <div class="card">
    <div class="card_container">
      <!-- 画像部分 -->
      <div class="card_photo">
        <img :src="post.image" alt="" />
      </div>
      <!-- 詳細情報 -->
      <div class="card_details">
        <!-- カテゴリー -->
        <div class="card_details_category">
          <p>{{ post.category }}</p>
        </div>
        <!-- タグ -->
        <div class="card_details_tags" v-for="(tag, index) in post.tags" :key="index">
          {{ tag }}
        </div>
        <!-- 作成日時 -->
        <div class="card_details_created">
          <p>{{ post.created_at }}</p>
        </div>
        <!-- 更新日時 -->
        <div class="card_details_updated">
          <p>{{ post.updated_at }}</p>
        </div>
      </div>
      <!-- 記事説明 -->
      <div class="card_descriptions">
        <!-- タイトル -->
        <h1 class="card_descriptions_title">{{ post.title }}</h1>
        <h2 class="card_descriptions_subtitle">{{ post.subtitle }}</h2>
        <!-- メタ情報 -->
        <div class="card_descriptions_meta">
          <p>{{ post.meta_description }}</p>
        </div>
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
  data() {
    return {
      category: [],
    };
  },
  // mounted() {
  //   this.axios
  //     .get(`http://localhost:80/api/posts/${}}`)
  //     .then((response) => {
  //       console.log("status: ", response.status);
  //       console.log("axiosGetData: ", response.data);
  //       this.posts = response.data.results;
  //     })
  //     .catch((err) => {
  //       console.log("axiosGetErr", err);
  //     });
  // },

};
</script>

<style lang="scss" scoped></style>
