<template>
    <!-- カテゴリー -->
    <ul class="categories">
        <li v-for="(category, value) in categories" :key="value">{{ category.name }}</li>
    </ul>
</template>

<script>
export default {
    props: {
        categories: {
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

.categories {
    border-radius: 8px;
    box-shadow: 0 3px 7px -3px rgba(0, 0, 0, 0.3);
    margin: 2rem;
    position: relative;
    overflow: hidden;
    background-color: $secondaryColor;
}
</style>