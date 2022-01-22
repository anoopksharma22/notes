<script setup>
import { ref, reactive, onMounted } from "vue";
import Quill from "quill";
import "quill/dist/quill.snow.css";

const editor = ref(null);
const quill = ref(null);
const content = ref(null);
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
});

const setContent = () => {
  content.value = quill.value.getContents();
  console.log(content.value);
};
</script>

<template>
  <div ref="editor"></div>
  <button @click="setContent">save</button>
</template>
