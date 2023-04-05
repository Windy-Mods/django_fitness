from django.db import models

from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    type = models.CharField(max_length=15)
    id = models.IntegerField(primary_key=True)
    id_video = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.name} | {self.type}'

    class Meta:
        db_table = "videos"

