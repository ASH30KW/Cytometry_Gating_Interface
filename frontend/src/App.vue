<template>
  <div id="nav">
    <!-- <router-link to="/">Example</router-link> | -->
    <!-- <router-link to="/about">About this plugin</router-link> -->
  </div>
  <router-view />
</template>

<script>
export default {
  watch: {
    $route() {
      if (window.parent && window.parent != window) {
        window.parent.postMessage("locationChangedNotification", "*");
      }
    },
  },
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
#chart {
  max-width: 650px;
  margin: 35px auto;
}

#vis {
  weight: 100%;
  height: 100%;
}

#select {
  border: 1px dashed #3366cc;
  position: absolute;
  z-index: 1000;
}
</style>
