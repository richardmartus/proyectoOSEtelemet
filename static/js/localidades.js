$(document).ready(function() {
            var currentPage = 1; // Página inicial

            function updatePaginationButtons(data) {
                var paginationContainer = $('#pagination-container');
                paginationContainer.empty();

                if (data.has_previous) {
                    paginationContainer.append('<li class="page-item" id="prevPageBtn"><a class="page-link" href="#" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>');
                } else {
                    paginationContainer.append('<li class="page-item disabled"><a class="page-link" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>');
                }

                for (var i = 1; i <= data.pages; i++) {
                    if (i === data.current_page) {
                        paginationContainer.append('<li class="page-item active"><a class="page-link" href="#">' + i + '</a></li>');
                    } else {
                        paginationContainer.append('<li class="page-item"><a class="page-link" href="#" data-page="' + i + '">' + i + '</a></li>');
                    }
                }

                if (data.has_next) {
                    paginationContainer.append('<li class="page-item" id="nextPageBtn"><a class="page-link" href="#" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>');
                } else {
                    paginationContainer.append('<li class="page-item disabled"><a class="page-link" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>');
                }

                // Agregar el manejador de clic para las páginas
                $('.page-link[data-page]').on('click', function() {
                    var page = $(this).data('page');
                    fetchLocalidades(page);
                });
            }

            function fetchLocalidades(page) {
                $.ajax({
                    url: '/board/localidades/',  // Reemplaza con la URL de tu vista AJAX
                    type: 'GET',
                    data: { 'page': page },
                    dataType: 'json',
                    success: function(data) {
                        var localidadesContainer = $('#localidades-container');
                        localidadesContainer.empty(); // Borra el contenido anterior

                        data.localidades_data.forEach(function(localidad) {
                            var listItem = $('<li class="list-group-item d-flex justify-content-between align-items-start"></li>');
                            var contentDiv = $('<div class="ms-2 me-auto"></div>');
                            var subheading = $('<div class="fw-bold">' + localidad.nombre + '</div>');
                            var departamento = $('<p>' + localidad.departamento + '</p>');
                            var region = $('<p>' + localidad.region + '</p>');
                            var latitudLongitud = $('<span class="badge bg-primary rounded-pill">' + localidad.latitud + ', ' + localidad.longitud + '</span>');

                            contentDiv.append(subheading, departamento, region);
                            listItem.append(contentDiv, latitudLongitud);
                            localidadesContainer.append(listItem);
                        });

                        updatePaginationButtons(data);
                    }
                });
            }

            // Botón de página anterior
            $('#prevPageBtn').click(function() {
                if (currentPage > 1) {
                    fetchLocalidades(currentPage - 1);
                }
            });

            // Botón de página siguiente
            $('#nextPageBtn').click(function() {
                if (data.has_next) {
                    fetchLocalidades(currentPage + 1);
                }
            });

            // Carga la página inicial
            fetchLocalidades(currentPage);
        });
