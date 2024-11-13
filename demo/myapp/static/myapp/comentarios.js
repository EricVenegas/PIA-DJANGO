function mostrarTexto() {
    const comentario = document.getElementById('comentario').value;
    const correo = document.getElementById('eemail').value;

    document.getElementById('usaer').innerText = "Usuario: " + correo;
    document.getElementById('comentador').innerText = "Comentario: " + comentario;
}