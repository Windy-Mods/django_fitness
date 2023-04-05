from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from fitness_site.models import Video
from fitness_site.serializer import VideoSerializer

def Test(requests):
    type_ = requests.GET.get('type', None)
    if type_ == 'short':
        return render(requests, 'index.html', {'videos_data': Video.objects.filter(type='short')})
    elif type_ == 'long':
        return render(requests, 'index.html', {'videos_data': Video.objects.filter(type='long')})
    else:
        return render(requests, 'index.html', {'videos_data': Video.objects.filter(type='short')})

class VideosApi(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer