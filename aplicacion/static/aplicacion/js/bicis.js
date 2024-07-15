//narvar
window.addEventListener('scroll', function () {
    var navbar = document.getElementById('navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

//contenido pagina
function openTab(event, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("arriendo-tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tab-link");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    event.currentTarget.className += " active";
}

document.getElementById("arriendo").style.display = "block";

function seleccionarBicicleta() {
    window.location.href = "formulario.html"; // Cambia esto a la URL de tu formulario
}



// Función para abrir el modal y cargar los detalles de la bicicleta

function openModal(bikeName, bikeImg) {
    var modal = document.getElementById("myModal");
    var modalBikeImg = document.getElementById("bike-details-img");
    var modalBikeName = document.getElementById("bike-details-name");

    modal.style.display = "block";
    modalBikeImg.src = bikeImg;
    modalBikeName.textContent = bikeName;
    // También puedes actualizar el valor del input hidden "bike-type"
    var bikeTypeInput = document.getElementById("bike-type");
    bikeTypeInput.value = bikeName;
}

function closeModal() {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
}

function calculateTotal() {
    var rentalDays = document.getElementById("rental-days").value;
    var totalPrice = 0;

    if (rentalDays == 1) {
        totalPrice = 15;
    } else if (rentalDays == 2) {
        totalPrice = 25;
    } else if (rentalDays == 3) {
        totalPrice = 35;
    } else if (rentalDays == 5) {
        totalPrice = 50;
    }

    document.getElementById("total-price").value = "$" + totalPrice;
}

function validateForm() {
    var bikeSize = document.getElementById("bike-size").value;
    var bikeWheelSize = document.getElementById("bike-wheel-size").value;
    var startDate = document.getElementById("start-date").value;
    var rentalDays = document.getElementById("rental-days").value;
    var paymentMethod = document.getElementById("payment-method").value;
    var deposit = document.getElementById("deposit").value;

    // Validación básica de campos obligatorios
    if (bikeSize === "" || bikeWheelSize === "" || startDate === "" || rentalDays === "" || paymentMethod === "" || deposit === "") {
        alert("Por favor completa todos los campos obligatorios.");
        return false;
    }

    // Validación específica para el campo de depósito
    if (isNaN(deposit) || deposit < 0) {
        alert("El depósito de garantía debe ser un número mayor o igual a cero.");
        return false;
    }

    return true; // Retorna true si el formulario es válido y puede enviarse
}
