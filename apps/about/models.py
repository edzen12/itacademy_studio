from django.db import models


class ThirdBlock(models.Model):
    img1 = models.ImageField(upload_to='plan/')  
    name1 = models.CharField(max_length=255, verbose_name= 'Название ')
    desc1 = models.TextField(verbose_name= 'Описание')
    img2 = models.ImageField(upload_to='plan/')  
    name2 = models.CharField(max_length=255, verbose_name= 'Название ')
    desc2 = models.TextField(verbose_name= 'Описание')
    img3 = models.ImageField(upload_to='plan/')  
    name3 = models.CharField(max_length=255, verbose_name= 'Название ')
    desc3 = models.TextField(verbose_name= 'Описание')
    img4 = models.ImageField(upload_to='plan/')  
    name4 = models.CharField(max_length=255, verbose_name= 'Название ')
    desc4 = models.TextField(verbose_name= 'Описание')

    def __str__(self) -> str:
        return f'{self.name1}, | {self.name2} | {self.name3}| {self.name4}'
    
    class Meta:
        verbose_name_plural = 'План'