<template>
  <div ref="editor"></div>
  <button @click="setContent">save</button>
  <div ref="viewer"></div>
</template>

<script setup>
import { ref, reactive, onMounted } from "vue";
import Quill from "quill";
import "quill/dist/quill.snow.css";

const editor = ref(null);
const viewer = ref(null);
const viewerq = ref(null);
const quill = ref(null);
// const content = ref(null);
const options = reactive({
  modules: {
    syntax: false,
  },
  placeholder: "Note here",
  theme: "snow",
});

onMounted(() => {
  if (editor.value !== null) {
    quill.value = new Quill(editor.value, options);
  }
  if (viewer.value !== null) {
    viewerq.value = new Quill(viewer.value, options);
  }
});

const setContent = () => {
  // viewer.value = quill.value.getContents();
  viewerq.value.setContents(quill.value.getContents());
};
</script>
