<template>
  <div class="container">
    <QuillEditor theme="snow" toolbar="full" :modules="modules" />
  </div>
</template>

<script>
// import { ref, defineComponent } from "vue";
import { QuillEditor } from "@vueup/vue-quill";
import BlotFormatter from "quill-blot-formatter";
import "@vueup/vue-quill/dist/vue-quill.snow.css";

export default {
  components: {
    QuillEditor,
  },
  setup: () => {
    const modules = {
      name: "blotFormatter",
      module: BlotFormatter,
      options: {
        /* options */
      },
    };
    return { modules };
  },
};
</script>

<style>
#app {
  display: flex;
  justify-content: center;
}
.container {
}
.ql-container {
  background: rgba(250, 247, 224, 0.466)
    radial-gradient(rgba(0, 0, 0, 0.3) 1px, transparent 1px);
  background-size: 25px 25px;
  height: 90vh;
  box-shadow: 0 0 2px 0px;
}
</style>
