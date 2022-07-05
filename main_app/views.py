from django.shortcuts import render
from .models import Card

cards = [
    Card('Alakazam', 1, 'gen1', 'psychic', 'stage 3'),
    Card('Blastoise', 2, 'gen1', 'water', 'stage 3'),
    Card('Charizard', 4, 'gen1', 'fire', 'stage 3'),
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cards_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {'cards': cards})

def card_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    return render(request, 'cards/detail.html', {'card': card})