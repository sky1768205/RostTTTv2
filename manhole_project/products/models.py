from django.db import models

class Product(models.Model):
    name = models.CharField("Название", max_length=200)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to='products/', null=True, blank=True)
    specifications = models.TextField("Характеристики", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name

    class Meta:
        verbose_name = "Люк"
        verbose_name_plural = "Люки"