from django.shortcuts import get_object_or_404
from .models import Video, Genre
from .services import open_file
from django.http import StreamingHttpResponse
from django.views.generic import ListView, DetailView
from datetime import datetime


class VideoList(ListView):
    model = Video
    ordering = '-create_at'
    template_name = 'video_hosting/home.html'
    context_object_name = 'video_list'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['genre'] = Genre.objects.all()
        return context


class VideoDetail(DetailView):
    model = Video
    template_name = 'video_hosting/video.html'
    context_object_name = 'video'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['genre'] = Genre.objects.all()
        return context

def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response


class GenreListView(VideoList):
    model = Genre
    ordering = '-create_at'
    template_name = 'video_hosting/genre_list.html'
    context_object_name = 'genre_films'

    def get_queryset(self):
        self.genre = get_object_or_404(self.model, id=self.kwargs['pk'])
        queryset = Video.objects.filter(genre=self.genre).order_by('-create_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['genre'] = Genre.objects.all()
        return context




