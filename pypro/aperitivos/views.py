# Create your views here.
from django.shortcuts import render


def video(request, slug):
    return render(request, 'aperitivos/video.html')
