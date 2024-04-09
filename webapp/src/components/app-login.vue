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
                <label for="email" class="form-label">Correo Electrónico</label>
                <input type="email" class="form-control" id="email" v-model="email" required>
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
export default {
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    login() {
      // Implemente su lógica de autenticación aquí
      this.$emit('showDashboard');
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