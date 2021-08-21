from django.contrib import admin
from .models import Receita
# Register your models here.

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('nome_receita', 'tempo_preparo', 'rendimento', 'categoria',
     'modo_preparo', 'ingredientes', 'data_receita')
admin.site.register(Receita, ReceitaAdmin)