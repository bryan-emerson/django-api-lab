from django.db import models
from django.urls import reverse

# Create your models here.
#book model

class Book(models.Model):
  title = models.CharField(max_length=120)
  author = models.CharField(max_length=120)

  def get_absolute_url(self):
    return reverse('book_detail', kwargs={'pk': self.pk})

  def __str__(self):
    return self.title