<!-- Copyright (c) 2022 Akito Koga
This software is released under the MIT License, see LICENSE. -->

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

<style lang="scss">
/* Reset CSS */
@import "./assets/styles/_reset.scss";
// Google Fonts
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+JP&family=Ubuntu&display=swap");

#app {
  font-family: "Ubuntu", "Noto Sans JP", Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 0px;
  
  // Responsible Font size
  font-size: calc(80% + 0.25vw);

  GlobalFooter {
    position: absolute;
    bottom: 0;
  }
  
  h1 {
    font-size: 2em;
  }
}
</style>
