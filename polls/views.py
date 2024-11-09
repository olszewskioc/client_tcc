from django.shortcuts import render
from .models import Video

from django.http import HttpResponse


def index(request):
    return render(request, 'polls/index.html')

def stream(request):
    context = {
        'min_higr': 30,  # Valor mínimo para o sensor de umidade
        'max_higr': 70,  # Valor máximo para o sensor de umidade
        'min_ntc': 28,   # Valor mínimo para o sensor de temperatura
        'max_ntc': 40,   # Valor máximo para o sensor de temperatura
        'min_mq7': 100,  # Valor mínimo para o sensor de CO
        'max_mq7': 500,  # Valor máximo para o sensor de CO
        'min_ldr': 200,  # Valor mínimo para o sensor de luminosidade
        'max_ldr': 800,  # Valor máximo para o sensor de luminosidade
    }
    return render(request, 'polls/stream.html', context)

def video_stream(request):
    return render(request, 'polls/video_stream.html', {"ip": 105})