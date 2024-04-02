<template>
  <div id="app">
    <Login v-if="currentView === 'login'" @showRegister="showRegister"/>
    <Register v-if="currentView === 'register'" @showLogin="showLogin"/>
  </div>
</template>

<script>
import Login from './components/app-login.vue';
import Register from './components/app-register.vue';

export default {
  components: {
    Login,
    Register
  },
  data() {
    return {
      currentView: 'login' // Cambia esto a 'register' para mostrar el registro inicialmente
    };
  },
  methods: {
    showRegister() {
      this.currentView = 'register';
    },
    showLogin() {
      this.currentView = 'login';
    }
  }
}
</script>

<style>
  /*@import './assets/style.css';*/
</style>
