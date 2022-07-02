<template>
<div class="tags">
    <p>タグ一覧({{ tags.length }})</p>
    <ul>
        <li v-for="(tag, value) in tags" :key="value">{{ tag.name }}</li>
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
}
</style>