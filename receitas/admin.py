from django.contrib import admin
from .models import Receita


@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_receita', 'pessoa','ativo']
    list_display_links = ['id', 'nome_receita']
    list_editable = ['ativo']
    list_per_page = 10
    search_fields = ['nome_receita', 'pessoa']
    list_filter = ['categoria', 'date_receita']


