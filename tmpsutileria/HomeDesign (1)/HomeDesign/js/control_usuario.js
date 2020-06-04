var getData = function()
{
	var num_habitacion = document.getElementById("num_habitacion").value;
	var descripcion = document.getElementById("descripcion").value;
	var costo = document.getElementById("costo").value;
	var estado = document.getElementById("estado").value;
	var tipo_habitacion = document.getElementById("tipo_habitacion").value;

	alert(num_habitacion+" - "+descripcion+" - "+costo+" - "+estado+" - "+tipo_habitacion);

	/*var ob = {num_habitacion:num_habitacion, descripcion:descripcion, costo:costo, estado:estado, tipo_habitacion:tipo_habitacion};

	$.ajax({
		type: 'POST',
		url: "../Proyecto_Hostal/registrar_datos.php",
		data: ob,
		beforeSend: function(objeto){

		},
		success: function(data)
		{
			$("#panel_respuesta").html(data);
		}
	});
*/

}