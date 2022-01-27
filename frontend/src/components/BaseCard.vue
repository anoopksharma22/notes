<template>
  <div class="base-card">
    <slot name="cardContent"></slot>
  </div>
</template>

<script>
export default {
  name: "BaseCard",
};
</script>

<style>
.base-card {
  background: #fff;
  width: 35rem;
  margin: 50px auto;
  padding: 50px;
  box-shadow: 0 0 5px 0;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
