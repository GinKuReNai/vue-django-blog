<template>
  <header class="header">
    <h1 class="title"><a href="#">Title</a></h1>
    <!-- ハンバーガーメニュー -->
    <div
      @click="isActive = !isActive"
      :class="{
        responsive__btn: !isActive,
        'responsive__btn active': isActive,
      }"
    >
      <span class="menu_line"></span>
      <span class="menu_line"></span>
      <span class="menu_line"></span>
    </div>
    <!-- ナビゲーション -->
    <nav :class="{ nav: !isActive, 'nav panelactive': isActive }">
      <!-- メニューリスト -->
      <ul class="nav__wrapper">
        <li class="nav__item"><a href="#">Home</a></li>
        <li class="nav__item"><a href="#">Articles</a></li>
        <li class="nav__item"><a href="#">RSS</a></li>
        <li class="nav__item"><a href="#">About</a></li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  data() {
    return {
      isActive: false,
    };
  },
};
</script>

<style lang="scss" scoped>
@import "../assets/styles/responsive";
@import "../assets/styles/ease";
@import "../assets/styles/basecolor";

/*========= ナビゲーションのためのCSS ===============*/

// 共通スタイル
@include responsive(xs) {
  .header {
    background-color: $backgroundColor;
    height: 70px;
    // タブレット以上
    @include responsive(md) {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px;
    }

    .title {
      position: relative;
      height: 100%;
      align-items: center;
      // タブレット以上
      @include responsive(md) {
        display: flex;
      }

      a {
        display: flex;
        color: $buttonTextColor;
        text-decoration: none;
        align-items: center;
        text-align: center;
        font-weight: bold;
        padding: 20px;
      }
    }

    // モバイルのみスライドメニュー
    @media screen and (max-width: 767px) {
      .nav {
        /* position:fixed;にし、z-indexの数値を大きくして前面へ */
        position: fixed;
        z-index: 999;
        /* ナビのスタート位置と形状 */
        top: 0;
        right: -120%;
        width: 100%;
        height: 100vh; /* ナビの高さ */
        background-color: $tertiaryColor;
        opacity: 0.8;
        /* 動き */
        transition: all 1s ease(in-out-back);

        // アクティブクラスがついたら位置を0に
        &.panelactive {
          right: 0;
        }

        // ナビゲーション
        .nav__wrapper {
          /*ナビゲーション天地中央揃え*/
          position: absolute;
          z-index: 999;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);

          // リストのレイアウト設定
          .nav__item {
            list-style: none;
            text-align: center;

            a {
              color: $buttonTextColor;
              text-decoration: none;
              padding: 10px;
              display: block;
              text-transform: uppercase;
              letter-spacing: 0.1em;
              font-weight: bold;
            }
          }
        }
      }
    }

    // タブレット以上
    @include responsive(md) {
      .nav {
        display: flex;

        // ナビゲーション
        .nav__wrapper {
          list-style: none;
          display: flex;
          justify-content: right;

          .nav__item a {
            position: relative;
            text-decoration: none;
            color: $buttonTextColor;
            padding: 10px;
            transition: color 0.2s;
            margin: 0 10px;
            padding: 0;

            // ホバー時に色を変化
            &:hover {
              color: $buttonColor;
              // 線を拡大
              &::after {
                transform: scale(1, 1); // x方向にスケール拡大
              }
            }

            &::after {
              content: "";
              // 絶対位置で線の位置を決める
              position: absolute;
              bottom: -5px;
              left: 10%;
              // 線の形状
              width: 80%;
              height: 2px;
              background-color: $buttonColor;
              // アニメーション指定
              transition: all 0.3s;
              transform: scale(0, 1); // x方向0, y方向1
              transform-origin: left top; // 左上基点
            }
          }
        }
      }
    }

    /*========= ボタンのためのCSS ===============*/
    // モバイルのみ表示
    @media screen and (max-width: 767px) {
      .responsive__btn {
        position: fixed;
        z-index: 9999; /*ボタンを最前面に*/
        top: 10px;
        right: 10px;
        cursor: pointer;
        width: 50px;
        height: 50px;

        /*×に変化*/
        .menu_line {
          display: inline-block;
          transition: all 0.4s;
          position: absolute;
          left: 14px;
          height: 3px;
          border-radius: 2px;
          background-color: $buttonColor;
          width: 45%;

          &:nth-of-type(1) {
            top: 15px;
          }
          &:nth-of-type(2) {
            top: 23px;
          }
          &:nth-of-type(3) {
            top: 31px;
          }
        }

        &.active {
          .menu_line {
            &:nth-of-type(1) {
              top: 18px;
              left: 18px;
              transform: translateY(6px) rotate(-45deg);
              width: 30%;
            }

            &:nth-of-type(2) {
              opacity: 0;
            }

            &:nth-of-type(3) {
              top: 30px;
              left: 18px;
              transform: translateY(-6px) rotate(45deg);
              width: 30%;
            }
          }
        }
      }
    }
  }
}
</style>
