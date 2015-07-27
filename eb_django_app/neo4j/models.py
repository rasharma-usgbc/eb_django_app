from django.db import models

# Create your models here.
class Buildings(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return str(self.id)
