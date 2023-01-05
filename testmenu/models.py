from django.db import models
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError


class Menu(models.Model):
    """ Название главного меню """
    title = models.CharField(max_length=255, verbose_name="Name")

    def __str__(self):
        return self.name

class Category(models.Model):
    """ Название подкатегорий главного меню """
    title = models.CharField(max_length=255, verbose_name="Name")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='categories', null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('page_with_menu', kwargs={'pk': self.title})

    def clean(self):
        if self.menu != self.parent.menu:
            raise ValidationError(
                {'parent': f"Элемент и его родитель должны находиться в одном меню. Родительское меню: {self.parent.menu}"}
            )

    def __str__(self):
        return self.title