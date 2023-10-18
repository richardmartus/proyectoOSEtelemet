$(document).ready(function() {
    $.ajax({
        url: '/board/obtener_localidades/',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            console.log(data);

            var map = L.map('map').setView([-32.80965357305832, -56.158987904223466], 7);

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 19,
                attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            }).addTo(map);

            var hasData = false;


            for (var i = 0; i < data.length; i++) {
                var localidad = data[i];

                if (localidad.latitud !== null && localidad.longitud !== null) {
                    var popupContent = '<b>Sector:</b> ' + localidad.sector + '<br><b>Localidad:</b> ' + localidad.nombre + '<br><b>Departamento:</b> ' + localidad.departamento;
                    var marker = L.marker([localidad.latitud, localidad.longitud]).addTo(map);
                    marker.bindPopup(popupContent);

                    hasData = true;
                }
            }

            if (!hasData) {
                $('.pagination').hide();
            }
        },
        error: function() {
            console.error('Error al obtener los datos de localidades.');
        }
    });
});
