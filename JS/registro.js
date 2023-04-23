
function validarFormulario() {
	var nombre = document.forms["registro"]["nombre"].value;
	var correo = document.forms["registro"]["correo"].value;
	var contrasena = document.forms["registro"]["contrasena"].value;
	var fecha_nac = document.forms["registro"]["fecha_nacimiento"].value;
	
	
	
	

	if (nombre == "" || correo == "" || contrasena == "" || fecha_nac == "") {
		
		alert("POR FAVOR COMPLETAR TODOS LOS CAMPOS.");
		
		return false;
		
	}
	if (contrasena.length < 8) {
		alert("CONTRASEÑA DEBE SER MAYOR A 8 CARACTERES.");

		return false;
	  }
	
		

	else  {
		alert("REGISTRO COMPLETADO   ☑");
	}
}


