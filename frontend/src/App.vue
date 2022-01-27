<template>
  <nav-bar />
  <router-view />
</template>
<script>
import NavBar from "./components/NavBar.vue";
export default {
  components: {
    NavBar,
  },
};
</script>
<style>
* {
  margin: 0;
  padding: 0;
}
</style>
