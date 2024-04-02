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
                  <label for="email" class="form-label">Correo Electrónico</label>
                  <input type="email" class="form-control" id="email" v-model="email" required>
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
        console.log("Registration attempt with:", this.email, this.password);
      },
    },
  };
</script>
  