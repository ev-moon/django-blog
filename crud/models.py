from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_at = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]