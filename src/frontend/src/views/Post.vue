<template>
  <div class="post">
    <main class="post_content">
      <!-- 画像 -->
      <div class="post_content_photo">
        <img :src="post.image" alt="" />
      </div>
      <!-- ヘッダー -->
      <div class="post_content_header">
        <!-- 日時 -->
        <ul class="post_content_header_datetime">
          <li>
            <font-awesome-icon :icon="{ prefix: 'fas', iconName: 'pen' }" />
            {{ post.created_at + "投稿" }}
          </li>
          <li>
            <font-awesome-icon :icon="{ prefix: 'fas', iconName: 'file-pen' }" />
            {{ post.updated_at + "更新" }}
          </li>
        </ul>
        <!-- タイトル -->
        <div class="post_content_header_title">
          <h1>{{ post.title }}</h1>
        </div>
        <!-- カテゴリー -->
        <div class="post_content_header_category">
          <a href="#">{{ post.category }}</a>
        </div>
        <!-- タグ一覧 -->
        <ul class="post_content_header_tags">
          <li v-for="(tag, index) in post.tags" :key="index">
            <a href="#">{{ tag }}</a>
          </li>
        </ul>
      </div>
      <!-- 本文 -->
      <article class="post_content_body" v-html="$sanitize(post.body)">
      </article>
      <!-- フッター -->
      <div class="post_content_footer">
        <!-- コメント -->
        <div class="post_content_footer_comment">
          <!-- コメント投稿 -->
          <div class="post_content_footer_comment_input">
            <h3 class="title">コメントを書く</h3>
            <form action="#">
              <input type="text" class="name" placeholder="name" maxlength="255"/>
              <textarea rows="10" cols="50" class="comment" placeholder="comment" wrap="soft"/>
              <button type="submit" class="submit"><span>コメントを投稿する</span></button>
            </form>
          </div>
          <!-- コメント一覧 -->
          <div class="post_content_footer_comment_view">
            <h3 class="title">コメント一覧</h3>
          </div>
        </div>
        <!-- シェアボタン等 -->
        <div class="post_content_footer_buttoms">

        </div>
        <!-- 関連記事 -->
        <div class="post_content_footer_relatedposts">

        </div>
      </div>
    </main>
    <div class="post_sidebar">
      <ProfileCard :profiles="getProfileList" />
      <TagListCard :tags="getTagList" />
      <CategoryListCard :categories="getCategoryList" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

import ProfileCard from "../components/ProfileCard.vue"
import TagListCard from "../components/TagListCard.vue"
import CategoryListCard from "../components/CategoryListCard.vue"
import hljs from "highlight.js";

export default {
  components: {
    ProfileCard,
    TagListCard,
    CategoryListCard,
  },

  data() {
    return {
        slug: this.$route.params.slug,
        post: {},
        comments: {},
    };
  },

  computed: {
    // Responseの各種情報を取得するゲッター
    ...mapGetters([
      "getProfileList",
      "getTagList",
      "getCategoryList",
    ]),
  },

  mounted() {
    // 記事の詳細をAPIから取得
    axios.get(`http://localhost/api/posts/${this.slug}/`)
    .then((response) => {
      this.post = response.data
      // 投稿日時と更新日時のフォーマットを変換
      this.post.created_at = this.dateFilter(this.post.created_at)
      this.post.updated_at = this.dateFilter(this.post.updated_at)
      console.log(response.data)
    })
    .catch((error) => {
      console.log('axiosGetErr', error)
    })

    // コメント一覧をAPIから取得
    axios.get(`http://localhost/api/posts/${this.slug}/comment/`)
    .then((response) => {
      this.comments = response.data
      this.comments.created_at = this.dateFilter(this.comments.created_at)
      console.log(response.data)
    })
    .catch((error) => {
      console.log('axiosGetErr', error)
    })

    // サイドバーにプロフィール・タグ・カテゴリーのデータを渡す
    this.$store.dispatch("fetchProfile");
    this.$store.dispatch("fetchTags");
    this.$store.dispatch("fetchCategories");
  },

  updated() {
    this.updateCodeSyntaxHighlighting()
  },

  methods: {
    // 日時を日本語表記に変更
    dateFilter(date) {
      const pattern = /(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2}).*/;
      const result = pattern.exec(date);
      const toJapanese = `${result[1]}年${result[2]}月${result[3]}日`;

      return toJapanese;
    },

    // <code>の中身をエスケープ処理
    escapeProcessingInCodeTag() {
      document.querySelectorAll("code").forEach(function(element) {
        element.innerHTML = element.innerHTML.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;");
      });
    },

    // Syntax Highlightを適用
    updateCodeSyntaxHighlighting() {
      document.querySelectorAll('pre code').forEach(block => {
        hljs.highlightBlock(block)
      })
    },
  },
 
};
</script>

<style lang="scss" scoped>
@import "../assets/styles/responsive";
@import "../assets/styles/ease";
@import "../assets/styles/basecolor";

@import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro&display=swap');

// 共通スタイル
@include responsive(xs) {
  .post {
    @include responsive(md) {
      display: flex;
    }

    &_content {
      @include responsive(md) {
        width: 700px;
        margin-right: 50px;
      }
      
      &_photo {
        overflow: hidden;
        img {
          width: 100%;
          height: auto;
        }
      }
      
      &_header {
        border-bottom: solid 1px grey;

        &_datetime {
          list-style: none;
          display: flex;
          justify-content: flex-end;

          li {
            display: inline-block;
            margin-right: 10px;
            font-size: 0.5em;
            color: gray;
          }
        }

        &_title {
          margin-top: 20px;
          padding: 0 15px;
          font-size: 0.9em;
        }
        
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
          list-style: none;
          overflow: hidden;

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

      &_body {
        padding: 0 20px;

        ::v-deep(.toc) {
          border: dotted 2px $highlightColor;
          padding: 0.5em 0.5em 0.5em 0.5em 2em;
          
          li {
            padding: 0.5em;
            list-style: decimal-leading-zero;
            // リストマーカーを内側に
            list-style-position: inside;
            
            a {
              color: $paragraphColor;
            }
          }
        }

        ::v-deep(h2) {
          border-bottom: solid 2px grey;
          margin: 20px 0;
        }
        
        ::v-deep(code) {
          background-color: black;
          padding: 0.2em 0.5em;
          margin: 0.5em;
          border-radius: 5px;
          font-size: 0.8em;
          font-family: "Source Code Pro";
          color: white;
        }
        
        ::v-deep(img) {
          width: 100%;
          height: auto;
          text-align: center;
        }
        
        ::v-deep(p) {
          margin-bottom: 1em;
        }
        
        ::v-deep(.admonition) {
          background-color: #ffd499;
          padding: 0.5em;
          
          .admonition-title {
            font-weight: bold;
          }
        }
      }
      
      &_footer {
        border-top: solid 1px grey;
        
        &_comment {
          &_input {
            border: dotted 2px orange;
            padding: 0.5em 0.5em 1em 0.5em;
            margin: 20px;

            .title {
              margin: 10px;
            }
            .name {
              display: block;
              border: solid 1px black;
              border-radius: 5px;
              margin: 10px;
            }
            
            .comment {
              display: block;
              border: solid 1px black;
              border-radius: 5px;
              resize: none;
              width: 70%;
              margin: 10px;
            }
            
            .submit {
              position: relative;
              text-decoration: none;
              display: inline-block;
              text-align: center;
              background: transparent;
              border-radius: 25px;
              border: solid 1px #333;
              outline: none;
              
              @include responsive(md) {
                transition: all 0.2s ease;
                &:hover {
                  border-color: transparent;
                  
                  span {
                    background-color: #333;
                    color: #fff;
                    // ホバーの際に文字をずらす
                    transform: translate(4px, 4px);
                  }
                }
                
                // beforeで影を表現
                &:before {
                  content: "";
                  position: absolute; /* 絶対位置で影の位置を決定 */
                  z-index: -1;
                  top: 4px;
                  left: 4px;
                  width: 100%;
                  height: 100%;
                  border-radius: 25px;
                  background-color: #333;
                }
              }
              
              span {
                position: relative;
                z-index: 2; /* 文字を背景より手前に表示 */
                display: block;
                padding: 10px 30px;
                background: #fff;
                border-radius: 25px;
                color: #333;
                
                @include responsive(md) {
                  transition: all 0.3s ease;
                }
              }
            }
          }
          
          &_view {
            border-top: solid 1px grey;

            .title {
              margin: 20px;
            }
          }
        }
      }
    }
    
    &_sidebar {
      // モバイル時は非表示
      @media screen and (max-width: 767px) {
        display: none;
      }
      width: 400px;
    }
  }
}

</style>
