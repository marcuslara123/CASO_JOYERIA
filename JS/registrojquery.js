$(document).ready(function() {
    $('#registro-form3').submit(function(event) {
      event.preventDefault();
      var nombre = $('#nombre').val();
      var correo = $('#correo').val();
      var contrasena = $('#contrasena').val();
      var fecha_nac = $('#fecha-nac').val();
      var formValido = true;
      
   
      if (nombre == '') {
        $('#nombre-error').text('Por favor INGRESAR NOMBRE VALIDO');
        formValido = false;
      } else {
        $('#nombre-error').text('');
      }

      if (fecha_nac  == "") {
        $('#nac-error').text('Por favor INGRESAR FECHA VALIDA');
        formValido = false;
      } else {
        $('#nac-error').text('');
      }
      
      
      
      
      if (correo == "") {
        $('#correo-error').text('PORFAVOR INGRESAR CORREO VALIDO');
        formValido = false;
      } else {
        $('#correo-error').text('');
      }
      
      
      if (contrasena.length < 8) {
        $('#contrasena-error').text('CONTRASEÑA DEBE SER MAYOR A 8 CARACTERES.');
        formValido = false;
      } else {
        $('#contrasena-error').text('');
      }
      
      if (formValido) {
        alert('REGISTRO COMPLETADO   ☑');
       
      }
    });
  });