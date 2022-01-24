<template>
  <label for="name">Name:</label>
  <input type="text" name="name" id="name" v-model="name" /> <br />
  <label for="username">Username:</label>
  <input type="text" name="username" id="username" v-model="username" /> <br />
  <label for="email">email:</label>
  <input type="email" name="email" id="email" v-model="email" /> <br />
  <label for="password">password:</label>
  <input type="password" name="password" id="password" v-model="password" />
  <br />

  <button @click="logFromData">Register</button> <br />
</template>

<script>
import postData from "@/helpers/SendPostRequest.js";
import { ref } from "vue";
const header = {
  "Content-Type": "application/json",
};
const backendURL = "http://127.0.0.1:8000/users/";
export default {
  setup() {
    const name = ref(null);
    const username = ref(null);
    const email = ref(null);
    const password = ref(null);
    const logFromData = () => {
      const data = {
        email: email.value,
        name: name.value,
        username: username.value,
        password: password.value,
      };
      const response = postData(backendURL, data, header);
      console.log(response);
      ctx.
    };
    return { name, username, email, password, logFromData };
  },
};
</script>
