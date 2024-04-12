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
                <input type="text" class="form-control" id="username" v-model="username" required>
              </div>
              <div class="mb-3">
                <label for="password" class="form-label">Contraseña</label>
                <input type="password" class="form-control" id="password" v-model="password" required>
              </div>
              <div v-if="errorMessage" class="alert alert-danger" role="alert">{{ errorMessage }}</div>
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
export default {
  name: 'DiabetesLogin',
  emits: ['showRegister', 'showDashboard', 'loginSuccess'],
  data() {
    return {
      username: '',
      password: '',
      errorMessage: ''
    };
  },
  methods: {
    login(){
      const userData = {
        username: this.username,
        password: this.password
      };
      const loginURL = 'http://127.0.0.1:8000/login/';

      fetch(loginURL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
      })
      .then(response => {
        if(!response.ok){
          throw new Error('Error en la solicitud');
        }
        //Si fue exitosa la solicitud
        return response.json();
      })
      .then(data => {
        this.$emit('loginSuccess', data.username);
        this.$emit('showDashboard');
      })
      .catch(error => {
        this.errorMessage = 'Credenciales incorrectas. Por favor, inténtelo de nuevo.';
        console.error('Error de autenticación:', error);
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