from django.db import models


class Sett(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo/')
    facebook = models.CharField(max_length=255, blank=True, null=True)
    google = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    youtube = models.CharField(max_length=255, blank=True, null=True)
    whatsapp = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    vk = models.CharField(max_length=255, blank=True, null=True)
    ok = models.CharField(max_length=255, blank=True, null=True)
    ph_number = models.CharField(max_length=13, null = True, blank = True)
    ph_number_support = models.CharField(max_length=13, null = True, blank = True)
    email = models.CharField(max_length=255, null = True, blank = True)
    address = models.CharField(max_length=255, null = True, blank = True)


    def __str__(self) -> str:
        return self.title 

    class Meta:
        verbose_name_plural = "Настройки"



class Slider(models.Model):
    image = models.ImageField(upload_to='service/', blank=True, null=True)  
    video_link = models.CharField(max_length=255, null=True, blank=True)  
    title_regular = models.CharField(max_length=55, verbose_name= 'текст 1 ')
    title_bold = models.CharField(max_length=55, verbose_name= 'текст 2 ')
    title_sing = models.CharField(max_length=55, verbose_name= 'текст 3 ') 

    def __str__(self) -> str:
        return f"{self.title_regular} {self.title_bold} {self.title_sing}"
    
    class Meta:
        verbose_name_plural = 'Слайдер'

class Plan(models.Model):
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


class CategoryPortfolio(models.Model):
    name = models.CharField(max_length=255, verbose_name= 'Название ')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Категории портофолио'


class Portfolio(models.Model):
    category = models.ForeignKey(CategoryPortfolio, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='home/')  
    name = models.CharField(max_length=255, verbose_name= 'Название ')
    desc = models.TextField(verbose_name= 'Описание')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Портофолио'


class Reviews(models.Model):
    calendar = models.DateTimeField(auto_now_add=False)
    img = models.ImageField(upload_to='home/')  
    name = models.CharField(max_length=55, verbose_name= 'ФИО')
    desc_reviews = models.TextField(verbose_name= 'Описание отзыва')


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Отзывы'

