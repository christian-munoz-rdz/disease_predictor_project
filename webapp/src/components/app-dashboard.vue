<template>
    <div class="container mt-5">
      <div class="row justify-content-center">
        <div class="col-md-6 text-center">
          <button @click="$emit('showForm')" class="btn btn-primary mb-3">Nueva Consulta</button>
          <button @click="$emit('showHistory')" class="btn btn-secondary">Ver Historial de Consultas</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'app-dashboard',
    // ...
  };
  </script>
  