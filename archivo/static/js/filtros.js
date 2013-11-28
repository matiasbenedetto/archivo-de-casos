$(document).ready(function() {

    //click en la lista desplegada de los dropdown
    $(".dropdown-menu li a").click(function(){
        var obj = $(this);
        $(obj).closest(".btn-group").find(".btn").text($(obj).text() );
        $(obj).closest(".btn-group").find(".btn").val($(obj).attr("val"))
        crear_consulta ();
    });

});



function crear_consulta (){
    var desde = $("#desde").val();
    var hasta = $("#hasta").val();
    var tipo_edad = $("#tipo-edad").val();
    var sexo = $("#sexo").val();
    var fuerza = $("#fuerza").val();
    var provincia = $("#provincia").val();
    
    $.post( "/archivo/cargar-marcadores/", {
        desde: desde,
        hasta: hasta,
        tipo_edad: tipo_edad,
        sexo: sexo,
        fuerza: fuerza,
        provincia: provincia
    }, function( data ) {
      remueve_marcadores();
      crear_marcadores (data);
    });
}


function remueve_marcadores(){
    //remueve todos los marcadores del mapa
    for(i=0;i<markers.length;i++) {
        map.removeLayer(markers[i]);
    } 
}


function crear_marcadores (data){
    //crea e inserta los marcadores de casos en el mapa
    var data_length = data.length;
    markers = new Array();
    for (var i = 0; i < data_length; i++) {
        var coordenadas = data[i][0].split(",");
        var lat = parseFloat(coordenadas[0], 10) - (Math.random()* (0.02 - -0.02) + 0.02);
        var lon = parseFloat(coordenadas[1], 10) - (Math.random()* (0.02 - -0.02) + 0.02);
        if (data[i][4] == "V"){
            var icono = iconoMasculino;
        }else{
            var icono = iconoFemenino;
        }
        var marker = L.marker( [lat, lon], {icon: icono} ).bindPopup("<a href='/archivo/caso/"+data[i][3]+"'>" + data[i][1] + " " + data[i][2] + "</a>");
        markers.push(marker);
        map.addLayer(markers[i]);
    }
    casos_mostrados(data_length);
}