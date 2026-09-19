from django.shortcuts import render
from django.conf import settings
import requests

def index(request):
    return render(request, 'index.html')

def consultar(request):
    nombre = request.POST.get('nombre', '').lower()
    pokemon = None
    error = None
    try:
        resp = requests.get(f'{settings.MICROSERVICIO_URL}/{nombre}')
        if resp.status_code == 200:
            pokemon = resp.json()
        else:
            error = 'Pokemon no encontrado'
    except Exception:
        error = 'No se pudo conectar al microservicio'

    return render(request, 'index.html', {'pokemon': pokemon, 'error': error, 'nombre': nombre})
