from django.shortcuts import render

# Classes
class Card:
    def __init__(self, name, id, generation, type, evolution_stage):
        self.name = name
        self.id = id
        self.generation = generation
        self.type = type
        self.evolution_stage = evolution_stage

cards = [
    Card('Alakazam', 1, 'gen1', 'pyschic', 'stage 3'),
    Card('Blastoise', 2, 'gen1', 'water', 'stage 3'),
    Card('Charizard', 4, 'gen1', 'fire', 'stage 3'),
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cards_index(request):
    return render(request, 'cards/index.html', {'cards': cards})