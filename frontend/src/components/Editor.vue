<template>
  <div class="container">
    <QuillEditor theme="snow" :toolbar="toolbar" :modules="modules" />
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
    const toolbar = [
      [{ header: [1, 2, 3, 4, 5, 6, false] }],
      // [{ header: 1 }, { header: 2 }], // custom button values
      ["bold", "italic", "underline", "strike"], // toggled buttons
      [{ script: "sub" }, { script: "super" }], // superscript/subscript
      [{ color: [] }, { background: [] }], // dropdown with defaults from theme
      [{ indent: "-1" }, { indent: "+1" }], // outdent/indent
      ["blockquote", "code-block"],
      [{ list: "ordered" }, { list: "bullet" }],
      // [{ direction: "rtl" }], // text direction

      // [{ size: ["small", false, "large", "huge"] }], // custom dropdown
      // [{ font: [] }],
      [{ align: [] }],

      ["clean"], // remove formatting button
    ];
    const modules = {
      name: "blotFormatter",
      module: BlotFormatter,
      options: {
        /* options */
      },
    };
    return { modules, toolbar };
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
