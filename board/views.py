from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from ubicaciones.models import Localidades, Coordenadas, Departamentos, Regiones, Sectores
from django.core.paginator import Paginator
from django.db.models import Q

#################################################################################
def board(request):
    localidades = Localidades.objects.all()
    paginator = Paginator(localidades, 5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'board/board.html', {'page': page})

#################################################################################
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('board:board')
        else:
            return redirect('board:error')

    return render(request, 'board/index.html')

#################################################################################
def error(request):
    return render(request, 'board/error.html')

#################################################################################
def board(request):
    return render(request, 'board/board.html')


#################################################################################
def obtener_localidades(request):
    localidades = Localidades.objects.all()
    data = []

    for localidad in localidades:
        coordenadas = localidad.coordenadas_set.first()  # Acceso a la relación ForeignKey

        if coordenadas:
            latitud = coordenadas.latitud
            longitud = coordenadas.longitud
        else:
            # Si las coordenadas están vacías, proporciona valores por defecto
            latitud = 0
            longitud = 0

        data.append({
            'latitud': latitud,
            'longitud': longitud,
            'nombre': localidad.localidad,
            'departamento': localidad.id_departamento.departamento,
            'region': localidad.id_departamento.id_region.region,
        })

    return JsonResponse(data, safe=False)

#################################################################################
def lista_localidades(request):
    localidades = Localidades.objects.all()
    paginator = Paginator(localidades, 4)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    data = []

    for localidad in page:
        coordenadas = localidad.coordenadas_set.first()

        if coordenadas:
            latitud = coordenadas.latitud
            longitud = coordenadas.longitud
        else:
            latitud = 0
            longitud = 0

        data.append({
            'latitud': latitud,
            'longitud': longitud,
            'nombre': localidad.localidad,
            'departamento': localidad.id_departamento.departamento,
            'region': localidad.id_departamento.id_region.region,
        })

    return JsonResponse({
        'localidades_data': data,
        'has_previous': page.has_previous(),
        'has_next': page.has_next(),
        'pages': paginator.num_pages,
        'current_page': page.number,
    })

#################################################################################

def search(request):
    query = request.GET.get('q')

    # Búsqueda en el modelo Departamentos
    departamentos = Departamentos.objects.filter(
        Q(departamento__icontains=query) |
        Q(id_region__region__icontains=query)
    )

    # Búsqueda en el modelo Regiones
    regiones = Regiones.objects.filter(
        Q(region__icontains=query) |
        Q(departamentos__departamento__icontains=query)
    )

    # Búsqueda en el modelo Localidades y Sectores (sin cambios)
    localidades = Localidades.objects.filter(Q(localidad__icontains=query))
    sectores = Sectores.objects.filter(sector__icontains=query)

    results_dict = {
        'departamentos': [str(departamento) for departamento in departamentos],#
        'localidades': [str(localidad) for localidad in localidades],
        'regiones': [str(region) for region in regiones], #
        'sectores': [str(sector) for sector in sectores],
    }

    # Imprime los resultados en el terminal
    print("Resultados de búsqueda:")
    print("Departamentos:", results_dict['departamentos'])
    print("Localidades:", results_dict['localidades'])
    print("Regiones:", results_dict['regiones'])
    print("Sectores:", results_dict['sectores'])

    return JsonResponse(results_dict)