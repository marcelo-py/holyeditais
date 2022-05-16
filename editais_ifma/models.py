from django.db import models
from django import forms


class Edital(models.Model):
    edital = models.CharField(max_length=350)

    def __str__(self):
        return self.edital


class Menssagens(models.Model):
    usuario = models.CharField(max_length=15, default='Anônimo')
    menssagem = models.TextField()
    edital = models.ForeignKey(Edital, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Edital')

    def __str__(self):
        return self.menssagem


class FormMenssage(forms.ModelForm):
    class Meta:
        model = Menssagens
        exclude = ()

class FormEdital(forms.ModelForm):
    class Meta:
        model = Edital
        exclude = ()