from django.shortcuts import render
from django.conf import settings
from .models import Pokemon
import requests

def index(request):
    return render(request, 'index.html')

def consultar(request):
    nombre = request.POST.get('nombre', '').lower()
    pokemon = None
    error = None
    try:
        resp = requests.get(f'{settings.MICROSERVICIO_URL}/{nombre}', timeout=5)
        if resp.status_code == 200:
            pokemon = resp.json()
        else:
            error = 'Pokemon no encontrado'
    except Exception:
        error = 'No se pudo conectar al microservicio (puede estar suspendido)'

    return render(request, 'index.html', {'pokemon': pokemon, 'error': error, 'nombre': nombre})

def consultar_local(request):
    nombre = request.POST.get('nombre', '').lower()
    pokemon = None
    error = None
    try:
        p = Pokemon.objects.get(nombre=nombre)
        pokemon = {
            'nombre': p.nombre, 'imagen': p.imagen, 'altura': p.altura,
            'peso': p.peso, 'ataque1': p.ataque1, 'ataque2': p.ataque2,
        }
    except Pokemon.DoesNotExist:
        error = 'Pokemon no encontrado en la base local'

    return render(request, 'index.html', {'pokemon': pokemon, 'error': error, 'nombre': nombre})
