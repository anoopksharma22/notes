<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <Editor />
  </div>
</template>

<script>
// @ is an alias to /src
import Editor from "@/components/Editor.vue";

export default {
  name: "Home",
  components: {
    Editor,
  },
};
</script>
