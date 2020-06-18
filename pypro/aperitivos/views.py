# Create your views here.
from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 157077066},
        'santamarta': {'titulo': 'Time Lapse Santa Marta', 'vimeo_id': 178990967},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
