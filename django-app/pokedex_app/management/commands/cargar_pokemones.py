from django.core.management.base import BaseCommand
from pokedex_app.models import Pokemon

DATA = [
    ('pikachu', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png', 0.4, 6.0, 'thunder-shock', 'quick-attack'),
    ('charmander', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png', 0.6, 8.5, 'scratch', 'ember'),
    ('bulbasaur', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png', 0.7, 6.9, 'tackle', 'growl'),
    ('squirtle', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png', 0.5, 9.0, 'tackle', 'water-gun'),
    ('charizard', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png', 1.7, 90.5, 'flamethrower', 'wing-attack'),
    ('blastoise', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png', 1.6, 85.5, 'hydro-pump', 'bite'),
    ('venusaur', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png', 2.0, 100.0, 'razor-leaf', 'sludge-bomb'),
    ('jigglypuff', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png', 0.5, 5.5, 'sing', 'pound'),
    ('eevee', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png', 0.3, 6.5, 'tackle', 'tail-whip'),
    ('mewtwo', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png', 2.0, 122.0, 'psychic', 'shadow-ball'),
]

class Command(BaseCommand):
    help = 'Carga los 10 pokemones en la base de datos local SQLite'

    def handle(self, *args, **kwargs):
        Pokemon.objects.all().delete()
        for nombre, imagen, altura, peso, ataque1, ataque2 in DATA:
            Pokemon.objects.create(
                nombre=nombre, imagen=imagen, altura=altura,
                peso=peso, ataque1=ataque1, ataque2=ataque2
            )
        self.stdout.write(self.style.SUCCESS('10 pokemones cargados en SQLite local'))
