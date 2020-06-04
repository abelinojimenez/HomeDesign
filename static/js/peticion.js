$(obtener_registros());

function obtener_registros(idEstudiante)
{
	
	$.ajax({
		type: 'POST',
        url: 'listar_estudiantes.php',                
        data: {idEstudiante:idEstudiante},
	})

	.done(function(resultado){
		$("#tabla-resultado").html(resultado);
	})
}

$(document).on('keyup', '#buscador_habitacion', function()
{	
	var valor=$(this).val();
	if(valor!=""){
		obtener_registros(valor);
	}else{
		obtener_registros();
	}

});

$(obtener_registros_reservacion());

function obtener_registros_reservacion(idReservacion)
{
	
	$.ajax({
		type: 'POST',
        url: 'listar_reservaciones.php',                
        data: {idReservacion:idReservacion},
	})

	.done(function(resultado){
		$("#tabla_resultado_reser").html(resultado);
	})
}

$(document).on('keyup', '#buscador_reservacion', function()
{	
	var valor=$(this).val();
	if(valor!=""){
		obtener_registros_reservacion(valor);
	}else{
		obtener_registros_reservacion();
	}

});