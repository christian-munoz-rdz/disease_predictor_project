<template>
    <div class="container">
      <h2 class="text-center mt-4">Formulario de Predicción de Diabetes</h2>
      <form @submit.prevent="submitPredictionForm" class="mt-3">
        <div class="mb-3">
          <label for="pregnancies" class="form-label">Número de embarazos</label>
          <input type="number" class="form-control" id="pregnancies" v-model.number="formData.pregnancies" required>
        </div>
        <div class="mb-3">
          <label for="glucose" class="form-label">Nivel de glucosa</label>
          <input type="number" class="form-control" id="glucose" v-model.number="formData.glucose" required>
        </div>
        <div class="mb-3">
          <label for="bloodPressure" class="form-label">Presión arterial diastólica</label>
          <input type="number" class="form-control" id="bloodPressure" v-model.number="formData.bloodPressure" required>
        </div>
        <div class="mb-3">
          <label for="skinThickness" class="form-label">Espesor del pliegue de la piel del tríceps</label>
          <input type="number" class="form-control" id="skinThickness" v-model.number="formData.skinThickness" required>
        </div>
        <div class="mb-3">
          <label for="insulin" class="form-label">Nivel de insulina en suero</label>
          <input type="number" class="form-control" id="insulin" v-model.number="formData.insulin" required>
        </div>
        <div class="mb-3">
          <label for="bmi" class="form-label">Índice de masa corporal</label>
          <input type="number" class="form-control" id="bmi" v-model.number="formData.bmi" step="0.01" required>
        </div>
        <div class="mb-3">
          <label for="diabetesPedigreeFunction" class="form-label">Función del pedigrí de diabetes</label>
          <input type="number" class="form-control" id="diabetesPedigreeFunction" v-model.number="formData.diabetesPedigreeFunction" step="0.001" required>
        </div>
        <div class="mb-3">
          <label for="age" class="form-label">Edad</label>
          <input type="number" class="form-control" id="age" v-model.number="formData.age" required>
        </div>
        <div class="text-center">
          <button type="submit" class="btn btn-success d-inline-block mr-3 btn-spacing">Predecir Diabetes</button>
          <button @click="$emit('showDashboard')" class="btn btn-secondary d-inline-block btn-spacing" style="margin-left: 10px;">Regresar al Dashboard</button>
        </div>
      </form>
      
    </div>
</template>
  
<script>
  export default {
    name: 'DiabetesForm',
    data() {
      return {
        formData: {
          pregnancies: null,
          glucose: null,
          bloodPressure: null,
          skinThickness: null,
          insulin: null,
          bmi: null,
          diabetesPedigreeFunction: null,
          age: null
        }
      };
    },
    methods: {
      submitPredictionForm() {
        const apiURL = 'http://127.0.0.1:8000/predict/'; // Ajuste esta URL a la de su API
        fetch(apiURL, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.formData),
        })
        .then(response => response.json())
        .then(data => {
          console.log('Success:', data);
          this.$emit('showResults', data.probability); // Emitir evento con la probabilidad
        })
        .catch((error) => {
          console.error('Error:', error);
        });
      // Reseteo del formulario movido a una promesa para asegurar la secuencia correcta
        Object.keys(this.formData).forEach(key => {
          this.formData[key] = null;
        });
      }
    }
  };
</script>

<style>

.btn-spacing {
  padding: auto;
}

</style>