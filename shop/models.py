from django.db import models
from pytils.translit import slugify
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    testq = models.FileField(null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Image_product(models.Model):
    img = models.ImageField(upload_to='products/shop/media/image_product/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.img.url.split('/')[-1]


class Color(models.Model):
    name = models.CharField(max_length=200)
    css_color = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name


All_BRANDS = (
    ('CROMIA', 'Cromia'),
    ('RIPANI', 'Ripani'),
    ('TOSCA BLU', 'Tosca Blu'),
    ('ELEGANZZA', 'Eleganzza'),
)

class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, blank = True, unique=True, db_index=True)
    brand = models.CharField(
        max_length=100,
        choices=All_BRANDS,
    )
    price = models.DecimalField(max_digits=6, decimal_places=0)
    stock = models.PositiveIntegerField()
    short_description = models.TextField(blank=True)
    detail_description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    color = models.ManyToManyField(Color, related_name='products')
    length = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    created = models.DateTimeField(default=timezone.now )
    updated = models.DateTimeField(auto_now=True)
    image = models.ManyToManyField(Image_product)

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.name) + "-" + str(self.id)
            self.save()

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['id', 'slug'])]

    def __str__(self):
        return self.name