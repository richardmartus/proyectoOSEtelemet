$(document).ready(function() {
    $('#search-form').on('submit', function(event) {
        event.preventDefault();
        var query = $('#search-input').val();
        console.log("Realizando búsqueda con el término: " + query);

        $.ajax({
            type: 'GET',
            url: '/board/search/',
            data: {
                q: query
            },
            success: function(data) {
                console.log("Resultados de búsqueda recibidos:");


                console.log("Departamentos:", data.departamentos);
                console.log("Localidades:", data.localidades);
                console.log("Regiones:", data.regiones);
                console.log("Sectores:", data.sectores);

                $('#search-results').html(data);
            }
        });
    });
});
