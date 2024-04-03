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
        <tr v-for="entry in historyEntries" :key="entry.id">
          <td>{{ entry.date }}</td>
          <td>{{ entry.percentage }}%</td>
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
      historyEntries: [
        // Aquí se generan algunos datos ficticios para el ejemplo
        { id: 1, date: '2024-04-01', percentage: 50 },
        { id: 2, date: '2024-03-28', percentage: 45 },
        { id: 3, date: '2024-03-20', percentage: 60 },
        // ... Añadir más entradas según sea necesario hasta 10
      ]
    };
  },
  methods: {
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
