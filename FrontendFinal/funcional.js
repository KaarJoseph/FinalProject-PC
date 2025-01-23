/*function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
    document.querySelector("header").classList.toggle("dark-mode");
    document.querySelector("footer").classList.toggle("dark-mode");
    document.querySelectorAll("section").forEach(sec => sec.classList.toggle("dark-mode"));
    document.querySelector("nav").classList.toggle("dark-mode");

    // Guardar la preferencia del usuario en localStorage
    const isDarkMode = document.body.classList.contains("dark-mode");
    localStorage.setItem("darkModeEnabled", isDarkMode);
}

// Verificar si el usuario ya tiene el modo oscuro activado
window.onload = () => {
    const darkModeEnabled = JSON.parse(localStorage.getItem("darkModeEnabled"));
    if (darkModeEnabled) {
        toggleDarkMode();
    }
};
*/
function extraerInformacion() {
    alert("Iniciando extracción de información...");
    // Aquí puedes agregar lógica para iniciar el proceso de extracción
    // como una llamada a una API o iniciar una funcionalidad en tu aplicación.
}

// Datos de ejemplo de TikTok
const tiktokData = [
    "Comentario 1 de TikTok",
    "Comentario 2 de TikTok",
    "Comentario 3 de TikTok",
];

// Función para manejar la extracción de datos
function extractTiktokData() {
    const tiktokDataContainer = document.getElementById("tiktok-data");
    tiktokDataContainer.innerHTML = ""; // Limpia los datos previos

    // Generar una lista de datos
    const ul = document.createElement("ul");
    tiktokData.forEach((comment) => {
        const li = document.createElement("li");
        li.textContent = comment;
        ul.appendChild(li);
    });

    tiktokDataContainer.appendChild(ul); // Añade la lista al contenedor
}

// Agregar el evento al botón
const extractButton = document.getElementById("extract-tiktok-data");
extractButton.addEventListener("click", extractTiktokData);

