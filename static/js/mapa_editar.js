var map = L.map('map').setView([-32.80965357305832, -56.158987904223466], 7);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

   map.on('click', function(e) {
  var lat = e.latlng.lat;
  var lng = e.latlng.lng;

  // Actualiza los campos de entrada en el formulario
  document.getElementById('latitud').value = lat;
  document.getElementById('longitud').value = lng;
});









