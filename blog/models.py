from django.db import models
from django.urls import reverse


class Partition(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание')
    declaration = models.TextField(verbose_name='Большое описание', default='')
    cost = models.IntegerField(verbose_name='Стоимость', default=0)
    preview = models.ImageField(upload_to='static/images/preview', default='default.jpg', verbose_name='Изображение')
    title = models.CharField(max_length=80, blank=True, null=True, verbose_name='title')
    meta_description = models.CharField(max_length=150, blank=True, null=True, verbose_name='meta description')
    keywords = models.TextField(verbose_name='ключевые слова', blank=True, null=True,)
    slug = models.SlugField(unique=True, verbose_name='Адрес-страницы')

    class Meta:
        verbose_name = 'Раздел Продукции'
        verbose_name_plural = 'Разделы Продукции'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена')
    area = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Площадь')
    time = models.CharField(max_length=10, verbose_name='Время работы')
    published = models.DateField(auto_now_add=True, verbose_name='Опубликовано')
    elem_partitions = models.ForeignKey('ElPartition', on_delete=models.CASCADE, related_name='products', verbose_name='Элемент раздела')
    img = models.ImageField(upload_to='static/images/products', verbose_name='Изображение')
    telephone = models.SmallIntegerField(blank=True, null=True, verbose_name='Телефон клиента')
    first_name = models.CharField(blank=True, null=True, verbose_name='Имя клиента', max_length=255)
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=80, blank=True, null=True, verbose_name='title')
    meta_description = models.CharField(max_length=150, blank=True, null=True, verbose_name='meta description')
    keywords = models.TextField(verbose_name='ключевые слова', blank=True, null=True,)
    slug = models.SlugField(unique=True, verbose_name='Адрес-страницы')

    class Meta:
        verbose_name = 'Выполненный заказ'
        verbose_name_plural = 'Выполненные заказы'
        ordering = ['-published']

    def __str__(self):
        return f"{self.name}: {self.elem_partitions.name} - ({self.published}) {self.id}"


class ElPartition(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    partition = models.ForeignKey(Partition, on_delete=models.CASCADE, related_name='elements', verbose_name='Раздел')
    img = models.ImageField(upload_to='static/images/elpartition', verbose_name='Изображение')
    benefits = models.ManyToManyField('Benefits', related_name="benes", verbose_name='Преимущества', blank=True)
    title = models.CharField(max_length=80, blank=True, null=True, verbose_name='title')
    meta_description = models.CharField(max_length=150, blank=True, null=True, verbose_name='meta description')
    keywords = models.TextField(verbose_name='ключевые слова', blank=True, null=True,)

    slug = models.SlugField(unique=True, verbose_name='Адрес-страницы')

    class Meta:
        verbose_name = 'Элемент раздела'
        verbose_name_plural = 'Элементы раздела'

    def __str__(self):
        return f"{self.partition}: {self.name}"
    
    def get_absolute_url(self):
        return reverse('list_elements', kwargs={'slug': self.slug})


class Benefit(models.Model):
    name = models.CharField(max_length=255, verbose_name="преимущество")


    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

    def __str__(self):
        return self.name


class Benefits(models.Model):
    title = models.CharField(max_length=511, verbose_name='Заголовок')
    descr = models.TextField(verbose_name='Описание')
    benefit = models.ManyToManyField(Benefit, verbose_name='Преимущества')

    class Meta:
        verbose_name = 'Список преимушеств'
        verbose_name_plural = 'Списки преимуществ'

    def __str__(self):
        return self.title

    def get_benefit(self):
        list = self.benefit.all()
        return list


