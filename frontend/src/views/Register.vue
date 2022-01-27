<template>
  <base-card>
    <template #cardContent>
      <form>
        <label for="email">Email</label>
        <input type="email" name="email" id="email" />
        <label for="username">Username</label>
        <input type="text" name="username" id="username" />
        <label for="password">Password</label>
        <input type="password" name="password" id="password" />
        <flat-button>Register</flat-button>
      </form>
      <p>
        Already have an account? <router-link to="/login">Login</router-link>
      </p>
    </template>
  </base-card>
</template>

<script>
import BaseCard from "../components/BaseCard";
import FlatButton from "../components/FlatButton.vue";
export default {
  components: {
    BaseCard,
    FlatButton,
  },
};
</script>
<style scoped>
form {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 100%;
}
label {
  margin: 10px 0 0 0;
  width: 100%;
}
input {
  margin: 10px 0 0 0;
  width: 100%;
  height: 30px;
  padding: 5px;
}
button {
  margin: 10px 0 0 0;
}
p {
  margin: 10px 0 0 0;
}
</style>
