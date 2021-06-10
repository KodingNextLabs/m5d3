from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        permissions = (
            ("uya_post", "Can test pos"),
        )

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Judul')
    owner = models.ForeignKey(User, related_name='owners', on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    price = models.PositiveBigIntegerField(default=0)
    stock = models.PositiveBigIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    total_price = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Produk Karpet'
        verbose_name_plural = 'Produk Karpet Mantab'