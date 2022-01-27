<template>
  <div id="nav">
    <div class="logo">
      <router-link to="/">
        <img src="../assets/logo.png" alt="Logo" />
      </router-link>
    </div>
    <div class="nav-items">
      <router-link to="/login" class="nav-item">Login</router-link>

      <router-link to="/register" class="nav-item">Register</router-link>
    </div>
  </div>
</template>

<script>
export default {
  components: {},
};
</script>
<style scoped>
#nav {
  background: #1dd1a1;
  height: 3rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 0 2px 0;
  width: 100vw;
  flex-flow: row nowrap;
}
.logo {
  margin-left: 2rem;
}
.logo img {
  max-height: 30px;
}
.nav-items {
  display: flex;
  justify-content: flex-end;
  margin-right: 1rem;
}
.nav-items #nav a.router-link-exact-active {
  color: #42b983;
}
.nav-item {
  margin: 0 5px;
}
</style>
