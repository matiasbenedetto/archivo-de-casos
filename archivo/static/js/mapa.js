var iconoMasculino = L.icon({
    iconUrl: '/static/img/iconos/masculino-mapa.png',
    shadowUrl: '/static/img/iconos/masculino-sombra-mapa.png',

    iconSize:     [25, 60], // size of the icon
    shadowSize:   [46, 31], // size of the shadow
    iconAnchor:   [12, 30], // point of the icon which will correspond to marker's location
    shadowAnchor: [10, 0],  // the same for the shadow
    popupAnchor:  [0, -30] // point from which the popup should open relative to the iconAnchor
});


$(document).ready(function() {
	tamanio_mapa();

  // create a map in the "map" div, set the view to a given place and zoom
  map = L.map('mapa').setView([-34.8, -58.7], 5);

  // add an OpenStreetMap tile layer
  L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  cargar_marcadores();

});




function cargar_marcadores () {
	$.get( "/archivo/cargar-marcadores/", function( data ) {

		var data_length = data.length;
		for (var i = 0; i < data_length; i++) {
			var coordenadas = data[i][0].split(",");
			var lat = parseFloat(coordenadas[0], 10) - (Math.random()* (0.02 - -0.02) + 0.02);
			//console.log(coordenadas[0]);
			//console.log(lat);
			//console.log("------------");
			var lon = parseFloat(coordenadas[1], 10) - (Math.random()* (0.02 - -0.02) + 0.02);
			var marker = L.marker( [lat, lon], {icon: iconoMasculino} ).addTo(map)
							.bindPopup("<a href='/archivo/caso/"+data[i][3]+"'>" + data[i][1] + " " + data[i][2] + "</a>");
		}

		casos_mostrados(data_length);

	});
}


function casos_mostrados(cantidad){
	$("#cantidad-casos").html(cantidad);	
}


function tamanio_mapa (){
	var ancho = $("#mapa").closest(".col-lg-9").width();
	$("#mapa").width(ancho+"px");
	//console.log(ancho);

	var alto = $("#mapa").closest(".container").height();
	$("#mapa").height(alto-50+"px");
	//console.log(alto);
}