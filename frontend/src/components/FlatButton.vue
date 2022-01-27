<template>
  <button @click="handleClick">
    <slot></slot>
  </button>
</template>

<style scoped>
button {
  width: 100px;
  height: 50px;
}
</style>
