<template>
  <div class="lds-dual-ring"></div>
</template>

<style scoped>
.lds-dual-ring {
  display: inline-block;
  width: 100px;
  height: 100px;
}
.lds-dual-ring:after {
  content: ' ';
  display: block;
  width: 100px;
  height: 100px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #74223c;
  border-color: #74223c transparent #74223c transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
