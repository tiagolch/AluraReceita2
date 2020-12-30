from django.contrib import admin
from .models import Pessoa


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email']
    list_display_links = ['id', 'nome']
    list_editable = ['email']
    search_fields = ['nome']
    list_per_page = 10


