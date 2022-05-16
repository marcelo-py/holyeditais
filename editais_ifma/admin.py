from django.contrib import admin
from . import models


class MenssagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'menssagem', 'edital')


class EditalAdmin(admin.ModelAdmin):
    list_display = ('id', 'edital')


admin.site.register(models.Menssagens, MenssagemAdmin)
admin.site.register(models.Edital, EditalAdmin)
