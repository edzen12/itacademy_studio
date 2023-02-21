from django.db import models
from ckeditor.fields import RichTextField

class Service(models.Model):
    img = models.ImageField(upload_to='service/')  
    name = models.CharField(max_length=255, verbose_name= 'Название ')
    desc = models.TextField(verbose_name= 'Описание')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Услуги'


class Prices(models.Model):
    name = models.CharField('тариф', max_length=55)
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    color = models.CharField('цвета', max_length=6, default='color1' ,
        help_text="вставьте 'color1' - зеленый\n2'color2' - аква\n2'color3' - оранжевый"
    )
    desc_tarif = RichTextField()

    def __str__(self) -> str:
        return self.name