<template>
  <!-- プロフィール -->
  <div>
    <div v-for="(profile, value) in profiles" class="profile" :key="value">
      <!-- 背景画像 -->
      <div class="profile_background">
        <img :src="profile.background" alt="" />
      </div>
      <!-- サムネイル画像 -->
      <div class="profile_thumbnail">
        <img :src="profile.thumbnail" alt="" />
      </div>
      <!-- 名前 -->
      <div class="profile_name">
        <p>{{ profile.display_name }}</p>
      </div>
      <!-- 自己紹介 -->
      <div class="profile_bio">
        <p>{{ profile.bio }}</p>
      </div>
      <!-- URL -->
      <ul class="profile_link">
        <!-- Website -->
        <li v-if="profile.website">
          <a :href="profile.website">
            <font-awesome-icon
              :icon="{ prefix: 'fas', iconName: 'earth-asia' }"
            />
            Website
          </a>
        </li>
        <!-- Twitter -->
        <li v-if="profile.twitter">
          <a :href="profile.twitter">
            <font-awesome-icon :icon="{ prefix: 'fab', iconName: 'twitter' }" />
            Twitter
          </a>
        </li>
        <!-- Github -->
        <li v-if="profile.github">
          <a :href="profile.github">
            <font-awesome-icon :icon="{ prefix: 'fab', iconName: 'github' }" />
            GitHub
          </a>
        </li>
        <!-- LinkedIn -->
        <li v-if="profile.linkedin">
          <a :href="profile.linkedin">
            <font-awesome-icon
              :icon="{ prefix: 'fab', iconName: 'linkedin' }"
            />
            LinkedIn
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    profiles: {
      required: false,
      default: null,
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../assets/styles/responsive";
@import "../assets/styles/ease";
@import "../assets/styles/basecolor";

// 共通スタイル
@include responsive(xs) {
  .profile {
    border-radius: 8px;
    box-shadow: 0 3px 7px -3px rgba(0, 0, 0, 0.3);
    margin: 2rem;
    position: relative;
    overflow: hidden;
    background-color: $secondaryColor;


    &_background {
      overflow: hidden;
      // 画像のりサイズ
      img {
        width: 100%;
        height: auto;
      }
    }

    &_thumbnail {
      position: relative;
      // サムネイルが背景画像に半分重なるようにする
      // marginを使うことで空白部分も含めてスライドできる
      margin-top: -25%;
      img {
        width: 40%;
        height: auto;
        // 丸く表示
        border-radius: 50%;
      }
    }

    &_name {
      font-size: 1.5rem;
      font-weight: 600;
      margin-bottom: 10px;
    }

    &_link {
      list-style: none;
      display: flex;
      justify-content: space-around;
      padding: 1rem;
      margin: 20px;
      border: 1px solid gray;
      border-radius: 20px;
    }
  }
}
</style>
