from django.shortcuts import render

def index(request):
    dados = {1:{'nome': 'foto1', 'autor':'leo'},2:{'nome':'foto2', 'autor': 'gabi'}}
    return render(request, 'galeria/index.html', {'cards': dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')
