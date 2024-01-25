from django.db import models


class Course(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    duracao = models.IntegerField()

    def __str__(self):
        return self.titulo
    


class Professor(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150)
    cargo = models.CharField(max_length=250)
    email = models.EmailField()
    def __str__(self):
        return self.nome + " " + self.sobrenome



