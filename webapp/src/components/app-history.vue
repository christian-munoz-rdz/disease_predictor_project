<template>
  <div class="container mt-5">
    <h2>Historial de Consultas</h2>
    <table class="table table-striped">
      <thead>
        <tr>
          <th scope="col">Fecha de Consulta</th>
          <th scope="col">Porcentaje de Probabilidad</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(entry, index) in historyEntries" :key="index">
          <td>{{ entry[0] }}</td>
          <td>{{ entry[1] * 100 }}%</td>
        </tr>
      </tbody>
    </table>
    <div class="d-grid gap-2 d-md-flex justify-content-md-center">
      <button @click="goToDashboard" class="btn btn-secondary me-md-2">Volver al Dashboard</button>
      <button @click="performAnotherConsultation" class="btn btn-primary ">Realizar Otra Consulta</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      historyEntries: []
    };
  },
  mounted(){
    this.getHistory();
  },
  methods: {
    getHistory() {
      // Realizar una solicitud al backend para obtener el historial de consultas
      fetch('http://127.0.0.1:8000/history/')
        .then(response => response.json())
        .then(data => {
          // Asignar los datos recibidos del backend a la variable historyEntries
          this.historyEntries = data;
        })
        .catch(error => {
          console.error('Error al obtener el historial de consultas:', error);
        });
    },
    goToDashboard() {
      this.$emit('showDashboard');
    },
    performAnotherConsultation() {
      this.$emit('showForm');
    }
  }
};
</script>

<style>
/* Opcional: Estilos adicionales aquí si se necesita personalizar la tabla más allá de los estilos predeterminados de Bootstrap */
</style>
