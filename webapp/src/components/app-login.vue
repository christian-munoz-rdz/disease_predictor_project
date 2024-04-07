<template>
    <div class="text-center">
      <img src="../assets/login-logo.png" alt="Diabetes Prediction" style="width: 200px;">
    </div>
    <div class="container mt-5">
      <div class="row justify-content-center">
        <div class="col-md-6">
          <div class="card">
            <div class="card-header">
              Iniciar Sesión
            </div>
            <div class="card-body">
              <form @submit.prevent="login">
                <div class="mb-3">
                  <label for="username" class="form-label">Nombre de usuario</label>
                  <input type="username" class="form-control" id="username" v-model="username" required>
                </div>
                <div class="mb-3">
                  <label for="password" class="form-label">Contraseña</label>
                  <input type="password" class="form-control" id="password" v-model="password" required>
                </div>
                <button type="submit" class="btn btn-primary">Ingresar</button>
                <button type="button" class="btn btn-link" @click="$emit('showRegister')">Crear una cuenta nueva</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>
  
<script>
import axios from 'axios';

  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      login() {
        // Implemente su lógica de autenticación aquí
        axios.post('http://192.168.100.17:8080/app-login',{
          username: this.username,
          password: this.password
        })
        .then(response => {
          console.log(response.data);
          this.$emit('showDashboard');
        })
        .catch(error => {
          console.error('Error: ',error);
        });
      },
    },
  };
</script>
  

<style>
  .logo {
    max-width: 100px; /* Ajuste el tamaño según sea necesario */
    margin: 20px 0; /* Espaciado superior e inferior para el logo */
  }
</style>