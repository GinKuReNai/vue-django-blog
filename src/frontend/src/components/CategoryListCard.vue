<template>
    <!-- カテゴリー -->
    <div class="categories">
        <p>
            <font-awesome-icon :icon="{ prefix: 'fas', iconName: 'folder' }" />
            カテゴリー
        </p>
        <ol>
            <li v-for="(category, value) in categories" :key="value">
                <a href="#" :class="{'child_category': isParentCategory(category), 'parent_category': !isParentCategory(category)}">{{ category.name }}</a>
            </li>
        </ol>
    </div>
</template>

<script>
export default {
    props: {
        categories: {
            required: false,
            default: null,
        },
    },
    
    methods: {
        isParentCategory(category) {
            if(category.tn_ancestors_pks == "") {
                return false;
            }
            return true;
        }
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
    
    p {
        margin: 10px auto;
        font-weight: bold;
    }
    
    ol {
        counter-reset: list;
        list-style: none;
        margin: 0 auto;
        padding: 0;
        width: 80%;
        
        li {
            .parent_category, .child_category {
                position: relative;
                display: block;
                padding: 5px 5px 5px 35px;
                margin: 7px 0;
                background: #fef6f3;
                color: $paragraphColor;
                font-weight: bold;
                text-decoration: none;
                border-radius: 5px;
                transition: all 0.3s ease-out;
                
                &:hover {
                    background: #b3d5ed;
                }

                &:hover:before {
                    left: -10px;
                    transform: rotate(360deg);
                }
                
                &:before {
                    content: counter(list);
                    counter-increment: list;
                    position: absolute;
                    top: 50%;
                    left: -15px;
                    height: 26px;
                    width: 26px;
                    margin-top: -15px;
                    background: $buttonColor;
                    color: #fff;
                    line-height: 26px;
                    border: 3px solid #fff;
                    border-radius: 30%;
                    text-align: center;
                    font-weight: bold;
                    transition: all 0.3s ease-out;
                }
            }
            
            .child_category {
                // 子カテゴリーは右にずらす
                margin: 7px 0 7px 35px;
            }
        }
    }
}
</style>