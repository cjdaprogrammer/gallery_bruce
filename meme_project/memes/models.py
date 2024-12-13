from django.db import models

class Meme(models.Model):
    image = models.ImageField(upload_to='memes/')
    caption = models.CharField(max_length=200)

    def __str__(self):
        return self.caption
