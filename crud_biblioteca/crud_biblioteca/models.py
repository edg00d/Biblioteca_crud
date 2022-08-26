from tkinter import CASCADE
from django.db import models

class categoria(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome
class produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    categoria = models.ForeignKey('categoria', on_delete=models.CASCADE)
#python .\manage.py makemigrations crud_biblioteca
#python .\manage.py migrate
#python .\manage.py runserver