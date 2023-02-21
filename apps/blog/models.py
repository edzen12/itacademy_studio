from django.db import models



class Posts(models.Model):
    calendar = models.DateField(auto_now=False, auto_now_add=False)
    img = models.ImageField(upload_to='home/')  
    name = models.CharField(max_length=255, verbose_name= 'Название ')
    desc = models.TextField(verbose_name= 'Описание')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Публикации'
