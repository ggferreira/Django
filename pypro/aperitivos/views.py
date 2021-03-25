from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': '527255451'},
        'abertura': {'titulo': 'Abertura do Curso', 'vimeo_id': '528991309'},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
# pode apagar, foi so pra passar
