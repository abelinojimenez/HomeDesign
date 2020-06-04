/*$(document).ready(function()
{
	$('#panel_registro form').submit(function(e))
	{
		e.preventDefault();
		var informacion = $('#panel_registro form').serialize();
		var metodo = $('#panel_registro form').attr('method');
		var peticion = $('#panel_registro form').attr('action');
		$.ajax({
			type: metodo,
			url: peticion,
			data: informacion,
			beforeSend: function()
			{
				$('Cargando informacion <br>');
			}
			error: function(data)
			{
				$('Ocurrio un error');
			}
			success: function(data)
			{
				$('#panel_respuesta').html(data);
			}
		});
		return false;
	};*/

function btn_listar_datos()
{
	//var peticion = $('#panel_listado form').attr('action');
	var ob = "";

	$.ajax({
		type: "POST",
		url: 'listar_estudiantes.php',
		data: ob,
		beforeSend: function(objeto)
		{

		},
		success: function(data)
		{
			$("#panel_estudiante").html(data);
		}
	});
}

function btn_asignar(idEstudiante)
{
	var ob2 = {idEstudiante:idEstudiante};

	$.ajax({
		type: "POST",
		url: 'vista_asignar.php',
		data: ob2,
		beforeSend: function(objeto)
		{

		},
		success: function(tipo)
		{
			$("#panel_asignar").html(tipo);
		}
	});
}	

function btn_asignar_datos()
{
	var idestudiante_asig = $("#idestudiante_asig").val();
	var docente_asig = $("#docente_asig").val();
	var seccion_asig = $("#seccion_asig").val();

	var ob2 = {idestudiante_asig:idestudiante_asig, docente_asig:docente_asig, seccion_asig:seccion_asig};

	$.ajax({
		type: "POST",
		url: 'asignar_estudiante.php',
		data: ob2,
		beforeSend: function(objeto)
		{

		},
		success: function(asignar)
		{
			$("#panel_respuesta_asignar").html(asignar);

			setTimeout(function(){
				$("#panel_respuesta_asignar").html("");
				$('body').removeClass('modal-open');
				$('.modal-backdrop').remove();
				alert("El estudiante fue asignado con éxito!")
				obtener_registros();
			},1000);
		}
	});
}

function btn_editar(idEstudiante)
{
	var ob2 = {idEstudiante:idEstudiante};

	$.ajax({
		type: "POST",
		url: 'vista_editar.php',
		data: ob2,
		beforeSend: function(objeto)
		{

		},
		success: function(tipo)
		{
			$("#panel_editar").html(tipo);
		}
	});
}

function btn_actualizar_datos()
{
	var idestudiante_act = $("#idestudiante_act").val();
	var nombres_act = $("#nombres_act").val();
	var apellidos_act = $("#apellidos_act").val();
	var clave_act = $("#clave_act").val();

	var ob2 = {idestudiante_act:idestudiante_act, nombres_act:nombres_act, apellidos_act:apellidos_act, clave_act:clave_act};

	$.ajax({
		type: "POST",
		url: 'actualizar_estudiante.php',
		data: ob2,
		beforeSend: function(objeto)
		{

		},
		success: function(actualizar)
		{
			$("#panel_respuesta_editar").html(actualizar);

			setTimeout(function(){
				$("#panel_respuesta_editar").html("");
				$('body').removeClass('modal-open');
				$('.modal-backdrop').remove();
				alert("Su registro se actualizó con éxito!")
				obtener_registros();
			},1000);
		}
	});
}

function btn_eliminar(idEstudiante)
{
	var ob = {idEstudiante:idEstudiante};

	$.ajax({
		type: "POST",
		url: 'vista_eliminar.php',
		data: ob,
		beforeSend: function(objeto)
		{

		},
		success: function(elimianr)
		{
			$("#panel_eliminar").html(elimianr);
		}
	});
}						

function btn_eliminar_datos()
{
	var id_estudiante_eli = $("#id_estudiante_eli").val();

	var ob2 = {id_estudiante_eli:id_estudiante_eli};

	$.ajax({
		type: "POST",
		url: 'eliminar_estudiante.php',
		data: ob2,
		beforeSend: function(objeto)
		{

		},
		success: function(actualizar)
		{
			$("#panel_eliminar").html(actualizar);

			setTimeout(function(){
				$("#panel_eliminar").html("");
				$('body').removeClass('modal-open');
				$('.modal-backdrop').remove();
				alert("Su registro se eliminó con éxito!")
				obtener_registros();
			},1000);
		}
	});
}

function select_habitacion()
{
	var No_Habitacion = $("#select_habitacion").val();
	var ob = {No_Habitacion:No_Habitacion};

		$.ajax({
		type: "POST",
		url: 'elegir_habitacion.php',
		data: ob,
		beforeSend: function(objeto)
		{

		},
		success: function(actualizar)
		{
			$("#panel_elegir").html(actualizar);
		}
	});
}

function btn_select_habitacion(No_Habitacion)
{
	var No_Habitacion = $("#select_habitacion").val();
	var ob = {No_Habitacion:No_Habitacion};

	$.ajax({
		type: "POST",
		url: 'vista_elegir.php',
		data: ob,
		beforeSend: function(objeto)
		{

		},
		success: function(elimianr)
		{
			$("#panel_elegir").html(elimianr);
		}
	});
}

function btn_reservar(num_habitacion)
{
	var ob2 = {num_habitacion:num_habitacion};

	$.ajax({
		type: "POST",
		url: 'vista_reservar.php',
		data: ob2,
		beforeSend: function(objeto)
		{

		},
		success: function(tipo)
		{
			$("#panel_reservar").html(tipo);
		}
	});
}


function btn_editar_reser(idReservacion)
{
	var ob2 = {idReservacion:idReservacion};

	$.ajax({
		type: "POST",
		url: 'vista_editar_reservaciones.php',
		data: ob2,
		beforeSend: function(objeto)
		{

		},
		success: function(tipo)
		{
			$("#panel_editar_reser").html(tipo);
		}
	});
}

function btn_actualizar_datos_reser()
{
	var dpi_act_reser = $("#dpi_act_reser").val();
	var fecha_entrada_act_reser = $("#fecha_entrada_act_reser").val();
	var fecha_salida_act_reser = $("#fecha_salida_act_reser").val();
	var costo_act_reser = $("#costo_act_reser").val();
	var nombres_act_reser = $("#nombres_act_reser").val();
	var apellidos_act_reser = $("#apellidos_act_reser").val();

	var ob2 = {dpi_act_reser:dpi_act_reser, fecha_entrada_act_reser:fecha_entrada_act_reser, fecha_salida_act_reser:fecha_salida_act_reser, costo_act_reser:costo_act_reser, nombres_act_reser:nombres_act_reser, apellidos_act_reser:apellidos_act_reser};

	$.ajax({
		type: "POST",
		url: 'actualizar_reservacion.php',
		data: ob2,
		beforeSend: function(objeto)
		{

		},
		success: function(actualizar)
		{
			$("#panel_respuesta_editar_reser").html(actualizar);

			setTimeout(function(){
				$("#panel_respuesta_editar_reser").html("");
				$('body').removeClass('modal-open');
				$('.modal-backdrop').remove();
				alert("Su registro se actualizó con éxito!")
				obtener_registros_reservacion();
			},1000);
		}
	});
}

function btn_eliminar_reserva(idReservacion)
{
	var ob = {idReservacion:idReservacion};

	$.ajax({
		type: "POST",
		url: 'vista_eliminar_reservacion.php',
		data: ob,
		beforeSend: function(objeto)
		{

		},
		success: function(elimianr)
		{
			$("#panel_eliminar_reser").html(elimianr);
		}
	});
}						

function btn_eliminar_datos_reserva()
{
	var idReservacion_eli = $("#idReservacion_eli").val();

	var ob2 = {idReservacion_eli:idReservacion_eli};

	$.ajax({
		type: "POST",
		url: 'eliminar_reservacion.php',
		data: ob2,
		beforeSend: function(objeto)
		{

		},
		success: function(actualizar)
		{
			$("#panel_eliminar_reser").html(actualizar);

			setTimeout(function(){
				$("#panel_eliminar_reser").html("");
				$('body').removeClass('modal-open');
				$('.modal-backdrop').remove();
				alert("Su registro se eliminó con éxito!")
				obtener_registros();
			},1000);
		}
	});
}