
		function validarFormulario() {
			var nombre = document.forms["registro"]["nombre"].value;
			var correo = document.forms["registro"]["correo"].value;
			var contrasena = document.forms["registro"]["contrasena"].value;
			if (nombre == "" || correo == "" || contrasena == "") {
				alert("Por favor complete todos los campos.");
				return false;
			}
		}
