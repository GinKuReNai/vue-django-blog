<template>
  <footer class="footer">
    <div class="footer-icons">
      <h1 class="title"><a href="#">Title</a></h1>
      <ul class="menu">
        <li>
          <a href="#"
            ><font-awesome-icon
              :icon="{ prefix: 'fab', iconName: 'github' }"
              size="2x"
          /></a>
        </li>
        <li>
          <a href="#"
            ><font-awesome-icon
              :icon="{ prefix: 'fab', iconName: 'twitter' }"
              size="2x"
          /></a>
        </li>
      </ul>
    </div>
  </footer>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
@import "../assets/styles/basecolor";
@import "../assets/styles/responsive";

// 共通スタイル
@include responsive(xs) {
  .footer {
    display: flex;
    background-color: $backgroundColor;
    justify-content: center;
    height: 130px;

    .footer-icons {
      display: flex;
      flex-direction: column;
      justify-content: space-around;
      width: 150px;

      .title {
        font-size: 16px;

        a {
          color: $buttonTextColor;
          text-decoration: none;
        }
      }
      .menu {
        display: flex;
        list-style: none;
        justify-content: space-around;

        li {
          margin: auto 10px;

          a {
            color: $buttonTextColor;
            transition: all 0.3s ease-in-out;
            // タブレット以上でホバーを有効
            @include responsive(md) {
              &:hover {
                color: $buttonColor;
              }
            }
          }
        }
      }
    }
  }
}
</style>
