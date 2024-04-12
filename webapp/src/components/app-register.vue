<template>
    <div class="container mt-5">
      <div class="row justify-content-center">
        <div class="col-md-6">
          <div class="card">
            <div class="card-header">
              Crear Cuenta
            </div>
            <div class="card-body">
              <form @submit.prevent="register">
                <div class="mb-3">
                  <label for="username" class="form-label">Nombre de usuario</label>
                  <input type="text" class="form-control" id="username" v-model="username" required>
                </div>
                <div class="mb-3">
                  <label for="password" class="form-label">Contraseña</label>
                  <input type="password" class="form-control" id="password" v-model="password" required>
                </div>
                <button type="submit" class="btn btn-success">Crear Cuenta</button>
                <button type="button" @click="$emit('showLogin')" class="btn btn-link">Ya tengo una cuenta</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
    
  </template>
  
<script>
  export default {
    data() {
      return {
        email: '',
        password: '',
      };
    },
    methods: {
      register() {
        // Implemente su lógica de registro aquí
        const userData = {
          username: this.username,
          password: this.password
        };

        fetch('http://127.0.0.1:8000/register/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(userData),
        })
        .then(response => {
          if(!response.ok){
            throw new Error('Error en la solicitud');
          }
          //Si el registro fue exitoso
          this.$emit('showLogin');
        })
        .catch(error => {
          console.error('Error de registro:', error);
        })
      },
    },
  };
</script>
  