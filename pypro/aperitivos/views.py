# Create your views here.
from django.shortcuts import render

videos = [
    {'slug': 'motivacao', 'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 157077066},
    {'slug': 'santamarta', 'titulo': 'Time Lapse Santa Marta', 'vimeo_id': 178990967},
]

videos_dct = {dct['slug']: dct for dct in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
