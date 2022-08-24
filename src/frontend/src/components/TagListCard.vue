<template>
<div class="tags">
    <p>
      <font-awesome-icon :icon="{ prefix: 'fas', iconName: 'tags' }" />
      タグ一覧({{ tags.length }})
    </p>
    <ul>
        <li v-for="(tag, value) in tags" :key="value">
            <a href="#">{{ tag.name }}</a>
        </li>
    </ul>
</div>
</template>

<script>
export default {
    props: {
        tags: {
            required: false,
            default: null,
        },
    },
}
</script>

<style lang="scss" scoped>
@import "../assets/styles/responsive";
@import "../assets/styles/ease";
@import "../assets/styles/basecolor";

.tags {
    border-radius: 8px;
    box-shadow: 0 3px 7px -3px rgba(0, 0, 0, 0.3);
    margin: 2rem;
    position: relative;
    overflow: hidden;
    background-color: $secondaryColor;
    
    display: flex;
    justify-content: flex-start;
    flex-wrap: wrap;
    align-items: center;

    list-style: none;
    overflow: hidden;
    padding: 0;
    text-align: center;
    
    p {
        margin: 10px auto;
        font-weight: bold;
    }

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
</style>