from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from videoapp.models import Video


class Comments(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    some_datatime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('comment_create', args=[str(self.video.id)])


