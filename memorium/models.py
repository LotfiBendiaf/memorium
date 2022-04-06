from django.db import models
from django.urls import reverse 

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name 


class Memory(models.Model):
    class Meta:
        verbose_name_plural = "memories"

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200) 
    memory = models.ImageField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        )
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.memory.url
        except:
            url = ''
        return url

    def get_absolute_url(self):
        return reverse('memory', args=[str(self.id)])
