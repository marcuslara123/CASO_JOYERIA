function validarCampos() {
    // Obtener los valores de los campos
    var usuario = document.getElementById('usuario').value;
    var contraseña = document.getElementById('contraseña').value;
  
    // Validar el campo de usuario
    if (usuario === '') {
      document.getElementById('usuarioError').textContent = 'Por favor, ingresa tu usuario.';
      return false;
    } else {
      document.getElementById('usuarioError').textContent = '';
    }
  
    // Validar el campo de contraseña
    if (contraseña === '') {
      document.getElementById('contraseñaError').textContent = 'Por favor, ingresa tu contraseña.';
      return false;
    } else {
      document.getElementById('contraseñaError').textContent = '';
    }
  
    
    alert('Inicio de sesión exitoso');
    return true;
  }
  