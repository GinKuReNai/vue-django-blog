<template>
  <div class="card">
    <!-- 画像部分 -->
    <div class="card_photo">
      <a href="#">
        <img :src="post.image" alt="" />
      </a>
    </div>
    <!-- 詳細情報 -->
    <div class="card_details">
      <!-- カテゴリー -->
      <div class="card_details_category">
        <a href="#">{{ post.category }}</a>
      </div>
      <!-- タグ -->
      <div class="card_details_tags">
        <ul>
          <li v-for="(tag, index) in post.tags" :key="index">
            <a href="#">{{ tag }}</a>
          </li>
        </ul>
      </div>
    </div>
    <!-- 記事説明 -->
    <div class="card_descriptions">
      <!-- タイトル -->
      <h1 class="card_descriptions_title">
        <a :href="post.post_url">{{ post.title }}</a>
      </h1>
      <!-- メタ情報 -->
      <div class="card_descriptions_meta">
        <p>{{ post.meta_description }}</p>
      </div>
      <div class="card_descriptions_comments">
        <p>
          <font-awesome-icon :icon="{ prefix: 'fas', iconName: 'comments' }" />
          コメント: {{ post.comments }}件
        </p>
      </div>
    </div>
    <!-- 日時 -->
    <ul class="card_date">
      <li>
        <font-awesome-icon :icon="{ prefix: 'fas', iconName: 'pen' }" />
        {{ dateFilter(post.created_at) + "投稿" }}
      </li>
      <li>
        <font-awesome-icon :icon="{ prefix: 'fas', iconName: 'file-pen' }" />
        {{ dateFilter(post.updated_at) + "更新" }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    post: {
      required: false,
      default: null,
    },
  },

  methods: {
    // 日時を日本語表記に変更
    dateFilter(date) {
      const pattern = /(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2}).*/;
      const result = pattern.exec(date);
      const toJapanese = `${result[1]}年${result[2]}月${result[3]}日`;

      return toJapanese;
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
  .card {
    border-radius: 8px;
    box-shadow: 0 3px 7px -3px rgba(0, 0, 0, 0.3);
    margin-top: 2rem;
    margin-bottom: 2rem;
    margin-left: 2rem;
    margin-right: 2rem;
    position: relative;
    overflow: hidden;

    @include responsive(md) {
      &:hover {
        box-shadow: 0 3px 7px -3px $highlightColor;
      }
    }

    &_photo {
      // 画面のリサイズ
      width: 326px;
      height: 182.25px;
      @include responsive(md) {
        width: 634px;
        height: 356.63px;
      }
      overflow: hidden;
      transition: transform 0.4s;
      
      // 画像のりサイズ
      img {
        width: 326px;
        height: 182.25px;
        @include responsive(md) {
          width: 634px;
          height: 356.63px;
        }
      }

      // タブレット以上でホバーを有効
      @include responsive(md) {
        &:hover {
          transform: scale(1.1, 1.1);
        }
      }
    }

    &_details {
      &_category {
        display: flex;
        justify-content: flex-start;
        flex-wrap: wrap;
        align-items: center;

        /*========= カテゴリ－のためのCSS ===============*/
        a {
          display: inline-block;
          color: white;
          background-color: $tertiaryColor;
          border: 1px solid $tertiaryColor;
          border-radius: 6px;
          padding: 6px;
          margin: 10px;
          cursor: pointer;
          transition: all 0.3s;
          text-decoration: none;

          // タブレット以上でホバーを有効
          @include responsive(md) {
            color: $buttonTextColor;
            background-color: $backgroundColor;
            border: 1px solid $backgroundColor;

            &:hover {
              color: $secondaryColor;
              background-color: $tertiaryColor;
              border: 1px solid $tertiaryColor;
            }
          }
        }
      }

      &_tags {
        display: flex;
        justify-content: flex-start;
        flex-wrap: wrap;
        align-items: center;

        list-style: none;
        margin: 0;
        overflow: hidden;
        padding: 0;

        /*========= タグのためのCSS ===============*/
        li {
          display: inline-block;

          a {
            line-height: 26px;
            position: relative;
            display: inline-block;
            height: 26px;
            margin: 0 0 10px 10px;
            padding: 0 20px 0 23px;
            transition: color 0.2s;
            text-decoration: none;
            color: $secondaryColor;
            border-radius: 0 3px 3px 0;
            background-color: $buttonColor;

            &::before,
            &::after {
              background-color: #fafcfc;
            }

            &::before {
              position: absolute;
              top: 10px;
              left: 3px;
              width: 6px;
              height: 6px;
              content: "";
              border-radius: 10px;
            }

            &::after {
              position: absolute;
              top: -1px;
              left: -6px;
              width: 0;
              height: 0;
              content: "";
              border-style: solid;
              border-width: 14px 8px 14px 0;
              border-color: transparent $buttonColor transparent transparent;
              border-radius: 4px;
            }

            // タブレット以上でホバーを有効
            @include responsive(md) {
              &:hover {
                background: $paragraphColor;

                &:after {
                  border-color: transparent $paragraphColor transparent
                    transparent;
                }
              }
            }
          }
        }
      }
    }

    &_descriptions {
      &_title {
        a {
          color: $headlineColor;
          text-decoration: none;
          font-size: 0.8em;

          @include responsive(md) {
            &:hover {
              color: rgb(102, 102, 102);
            }
          }
        }
      }

      &_comments {
        text-align: left;
        p {
          display: inline-block;
          font-size: 0.85em;
          color: gray;
          margin-left: 25px;
        }
      }
    }

    &_date {
      list-style: none;

      @include responsive(md) {
        display: flex;
        justify-content: flex-end;
      }

      li {
        display: inline-block;
        margin: 10px;
        font-size: 0.85em;
        color: gray;
      }
    }
  }
}
</style>
