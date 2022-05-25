<template>
  <header class="header">
    <div class="site-header__wrapper">
      <h1 class="title"><a href="#">Title</a></h1>
      <!-- ハンバーガーメニュー -->
      <div class="responsive__btn">
        <div class="menu_line"></div>
        <div class="menu_line"></div>
        <div class="menu_line"></div>
      </div>
      <!-- ナビゲーション -->
      <nav class="nav">
        <ul class="nav__wrapper">
          <li class="nav__item"><a href="#">Home</a></li>
          <li class="nav__item"><a href="#">Articles</a></li>
          <li class="nav__item"><a href="#">RSS</a></li>
          <li class="nav__item"><a href="#">About</a></li>
          <li class="nav__item"><a href="#">Subscribe</a></li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<style lang="scss" scoped>
@import "../assets/styles/responsive";
$backgroundColor: #d2f6ff;
$marginSize: 10px;

// Reset CSS
.header {
  background-color: $backgroundColor;

  a:link,
  a:visited,
  a:hover,
  a:active {
    text-decoration: none;
    color: black;
  }

  .site-header__wrapper {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 50px;

    .title {
      font-weight: bold;
      cursor: pointer;
      margin-left: $marginSize;
    }

    .responsive__btn {
      @include responsive(sm) {
      }
    }

    .nav__wrapper {
      @include responsive(sm) {
        display: flex;
        list-style: none;
      }
      .nav__item {
        @include responsive(sm) {
          margin: 0 $marginSize;
        }
      }
    }
  }
}
</style>
