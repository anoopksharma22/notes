<template>
  <div ref="editor"></div>
  <button @click="saveContent">save</button>
  <div ref="viewer"></div>
</template>

<script>
import { ref, reactive, onMounted } from "vue";
import Quill from "quill";
import BlotFormatter from "quill-blot-formatter";
import "quill/dist/quill.snow.css";
export default {
  setup() {
    const editor = ref(null);
    const viewer = ref(null);
    const viewerq = ref(null);
    const quill = ref(null);
    const toolbarOptions = [
      ["bold", "italic"],
      ["link", "image"],
    ];
    // const content = ref(null);
    const options = reactive({
      modules: {
        syntax: false,
        blotFormatter: BlotFormatter,
        toolbar: toolbarOptions,
      },
      placeholder: "Note here",
      theme: "snow",
    });

    onMounted(() => {
      if (editor.value !== null) {
        Quill.register("modules/blotFormatter", BlotFormatter);
        quill.value = new Quill(editor.value, options);
      }
      if (viewer.value !== null) {
        viewerq.value = new Quill(viewer.value, options);
      }
    });

    async function postData(url = "", data = {}) {
      // Default options are marked with *
      const response = await fetch(url, {
        method: "POST", // *GET, POST, PUT, DELETE, etc.
        mode: "cors", // no-cors, *cors, same-origin
        cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
        credentials: "same-origin", // include, *same-origin, omit
        headers: {
          "Content-Type": "application/json",
          Authorization:
            "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmdWd1IiwiZXhwIjoxNjQzMDQ2ODUwfQ.WmQEd2ht5qP5Y54UlMqE3wbQdc7rGU8wZP0HQOVoCag",
        },
        redirect: "follow", // manual, *follow, error
        referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(data), // body data type must match "Content-Type" header
      });
      return response.json(); // parses JSON response into native JavaScript objects
    }

    const saveContent = () => {
      // viewer.value = quill.value.getContents();
      const data = quill.value.getContents();
      const notedata = {
        title: "From Vue",
        content: data,
        is_provate: false,
        tags: "vue",
      };
      postData("http://127.0.0.1:8000/notes/", notedata);

      // const saveData = null;
      fetch("http://127.0.0.1:8000/notes/")
        .then((response) => response.json())
        .then((data) => viewerq.value.setContents(data[0].content));
    };

    return { saveContent, editor, viewer };
  },
};
</script>
