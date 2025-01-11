from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentsForm
from .models import Comments
from videoapp.models import Video, Genre
from datetime import datetime


class CommentsCreate(LoginRequiredMixin, CreateView, ListView):
    form_class = CommentsForm
    model = Comments
    ordering = '-some_datatime'
    template_name = 'comment/createcomment.html'
    context_object_name = 'comments'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.video_id = self.kwargs['pk']
        comment.save()
        return super().form_valid(form)

    def get_queryset(self):
        self.video = get_object_or_404(Video, id=self.kwargs['pk'])
        queryset = Comments.objects.filter(video=self.video).order_by('-some_datatime')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['genre'] = Genre.objects.all()
        return context
