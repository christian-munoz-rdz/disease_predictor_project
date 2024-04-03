<template>
    <div style="position: absolute; top: 20px; left: 20px; right: 20px;">
        <div class="d-flex align-items-center">
            <img src="../assets/user.png" alt="User Avatar" class="rounded-circle" style="width: 50px; height: 50px;">
            <span class="ml-2">Usuario</span>
        </div>
    </div>
    <div class="container mt-5 d-flex flex-column justify-content-center vh-100">
        <div class="row justify-content-center">
            <div class="col-md-6 text-center">
                <button @click="$emit('showForm')" class="btn btn-primary btn-lg mb-3 d-block custom-btn">Nueva Consulta</button>
                <button @click="$emit('showHistory')" class="btn btn-secondary btn-lg d-block custom-btn">Ver Historial de Consultas</button>
                <button @click="$emit('showLogin')" class="btn btn-danger btn-lg d-block custom-btn">Cerrar sesión</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'app-dashboard',
};
</script>

<style>
.d-block {
    display: block;
}

.mb-2 {
    margin-bottom: 10px;
}

.custom-btn {
    width: 100%;
    margin-bottom: 10px;
}

.btn-lg {
    padding: 10px 16px;
    font-size: 18px;
    line-height: 1.3333333;
    border-radius: 6px;
}

.vh-100 {
    height: 100vh;
}

.rounded-circle {
    border-radius: 50%;
}
</style>
  