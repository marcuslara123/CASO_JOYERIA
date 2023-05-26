function validar() {
	var nombre = document.forms["registro"]["nombre"].value;
	var correo = document.forms["registro"]["correo"].value;
	var contrasena = document.forms["registro"]["contrasena"].value;
	var fecha_nac = document.forms["registro"]["fecha_nacimiento"].value;
	var text;
	var formValido = true;
	
	
	if (nombre.length == 0){
        text = "Nombre no debe estar vacio";   
		formValido = false;
    }else{
        text = "";
    }
    document.getElementById("valida_nombre").innerHTML = text;

	if (correo.length == 0){
        text = "Correo no debe estar vacio";   
		formValido = false;
    }else{
        text = "";
    }
    document.getElementById("valida_email").innerHTML = text;

	if (fecha_nac.length == 0){
        text = "Ingrese su nacimiento";   
		formValido = false;
    }else{
        text = "";
    }
    document.getElementById("valida_nac").innerHTML = text;
	

	
	
	if (contrasena.length < 8){
        text = "Contraseña debe tener largo 8";
		formValido = false;
    }else{
        text = "";
    }
    document.getElementById("valida_password").innerHTML = text;
	
	
	if (formValido) {
        alert('REGISTRO COMPLETADO   ☑');
       
      }



	
}
