<template>
  <div id="app">
    <Login v-if="currentView === 'login'" @showRegister="showRegister" @showDashboard="showDashboard"/>
    <Register v-if="currentView === 'register'" @showLogin="showLogin" @showDashboard="showDashboard"/>
    <Dashboard v-if="currentView === 'dashboard'" @showForm="showForm" @showHistory="showHistory" @showLogin="showLogin"/>
    <DiabetesForm v-if="currentView === 'form'" @showDashboard="showDashboard" @showResults="showResults"/>
    <History v-if="currentView === 'history'" @showDashboard="showDashboard" @showForm="showForm"/>
    <Results v-if="currentView === 'results'" @showDashboard="showDashboard"/>
  </div>
</template>

<script>
import Login from './components/app-login.vue';
import Register from './components/app-register.vue';
import Dashboard from './components/app-dashboard.vue';
import DiabetesForm from './components//app-form.vue';
import History from './components/app-history.vue';
import Results from './components/app-results.vue';

export default {
  components: {
    Login,
    Register,
    Dashboard,
    DiabetesForm,
    History,
    Results
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
    },
    showDashboard() {
      this.currentView = 'dashboard';
    },
    showResults() {
      this.currentView = 'results';
    }
  }
};
</script>

<style>
  /*@import './assets/style.css';*/
</style>
