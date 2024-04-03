<template>
  <div id="app">
    <Login v-if="currentView === 'login'" @showRegister="showRegister"/>
    <Register v-if="currentView === 'register'" @showLogin="showLogin"/>
    <Dashboard v-if="currentView === 'dashboard'" @showForm="showForm" @showHistory="showHistory"/>
    <DiabetesForm v-if="currentView === 'form'"/>
    <History v-if="currentView === 'history'"/>
  </div>
</template>

<script>
import Login from './components/app-login.vue';
import Register from './components/app-register.vue';
import Dashboard from './components/app-dashboard.vue';
import DiabetesForm from './components//app-form.vue';
import History from './components/app-history.vue';

export default {
  components: {
    Login,
    Register,
    Dashboard,
    DiabetesForm,
    History
  },
  data() {
    return {
      currentView: 'login' 
    };
  },
  methods: {
    showRegister() {
      this.currentView = 'register';
    },
    showLogin() {
      this.currentView = 'login';
    },
    showForm() {
      this.currentView = 'form';
    },
    showHistory() {
      this.currentView = 'history';
    }
  }
}
</script>

<style>
  /*@import './assets/style.css';*/
</style>
