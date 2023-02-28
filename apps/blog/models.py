from django.db import models
from ckeditor.fields import RichTextField


TAG_NEWS_CHOICES = [
    ('Therd', 'Therd'),
    ('Others', 'Others'), 
]

class Posts(models.Model):
    tag = models.CharField('Тег', choices=TAG_NEWS_CHOICES, default='Others', max_length=6)
    calendar = models.DateField(auto_now=False, auto_now_add=False)
    img = models.ImageField(upload_to='home/')  
    name = models.CharField(max_length=255, verbose_name= 'Название ')
    desc = RichTextField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['-id',]
        verbose_name_plural = 'Публикации'
