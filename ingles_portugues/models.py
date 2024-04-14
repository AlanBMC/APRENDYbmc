from django.db import models

# Create your models here.
class Palavras(models.Model):
    
    palavra_portugues = models.TextField()
    palavra_pronuncia = models.CharField(max_length=255)
    palavra_ingles = models.CharField(max_length=255)


class Frase(models.Model):
    palavra = models.ManyToManyField(Palavras, related_name='frases')
    
class Usuario(models.Model):
    nome = models.CharField(max_length=255)

class Frases_usuario(models.Model):
    frase_ingles = models.TextField()
    frase_traduziada = models.TextField()
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name='frases_usuario', )

class Palavras_usuario(models.Model):
    palavra_portugues = models.TextField()
    palavra_pronuncia = models.CharField(max_length=255)
    palavra_ingles = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name='palavras_usuario')