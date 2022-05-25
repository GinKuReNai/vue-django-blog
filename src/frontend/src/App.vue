<script setup>
import GlobalHeader from "./components/GlobalHeader.vue";
import GlobalFooter from "./components/GlobalFooter.vue";
</script>

<template>
  <div class="app">
    <GlobalHeader />
    <router-view></router-view>
    <GlobalFooter />
  </div>
</template>

<style>
/* Reset CSS */
@import "./assets/styles/_reset.scss";

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
