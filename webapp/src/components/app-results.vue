<template>
    <div class="text-center">
      <!-- Usar 'v-show' para evitar quitar el elemento del DOM y así no interrumpir la animación en progreso -->
      <p class="breathing-text" :class="{ 'stop-breathing': !isBreathing }" v-show="showMessage">
        {{ message }}
      </p>
      <!-- Botón que se muestra cuando se detiene la animación y aparece el mensaje final -->
        <button v-if="!isBreathing" @click="goToDashboard" class="btn btn-primary mt-3 mx-auto d-block">Regresar al Dashboard</button>
    </div>
</template>
  
  <script>
  export default {
    data() {
      return {
        message: 'Calculando resultados...',
        showMessage: true,
        isBreathing: true, // Controla si la animación está activa
      };
    },
    methods: {
      goToDashboard() {
        this.$emit('showDashboard');
      }
    },
    mounted() {
      setTimeout(() => {
        this.message = 'Usted tiene un 50% de probabilidad de padecer diabetes';
        this.isBreathing = false; // Detiene la animación
      }, 15000); // 15 segundos
    }
  };
  </script>
  
  <style>
  @keyframes breathing {
    0%, 100% {
      transform: scale(1);
    }
    25% {
      transform: scale(1.05);
    }
    50% {
      transform: scale(1);
    }
    75% {
      transform: scale(0.95);
    }
  }
  .breathing-text {
    font-size: 4rem; /* Tamaño de texto muy grande */
    animation: breathing 2s ease-out infinite;
    display: inline-block;
    margin-top: 50vh; /* Centrar verticalmente */
    transform: translateY(-50%); /* Ajuste fino de la centración vertical */
  }
  .stop-breathing {
    animation: none; /* Detener la animación */
  }
  </style>
  
  