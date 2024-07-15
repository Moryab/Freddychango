function showconfirm() {
    Swal.fire({
    position: "top-center",
    icon: "success",
    title: "Registrado con exito",
    showConfirmButton: false,
    timer: 1500
  });
}

function registrarUsuario() {
    // Aquí deberías tener la lógica para registrar al usuario (p. ej., enviar una solicitud AJAX)
    // Simularemos una solicitud exitosa después de 1 segundo
    setTimeout(function() {
      showconfirm(); // Llama a la función showconfirm después de registrar con éxito
    }, 1000);
  }