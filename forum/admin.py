from django.contrib import admin

from .models import (
    Contato,
    ItemLista,
    MembroEquipe,
    Pilar,
    PraticaEstudio,
    SecaoConteudo,
    Tecnologia,
)


@admin.register(SecaoConteudo)
class SecaoConteudoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'pagina', 'ordem']
    list_filter = ['pagina']
    search_fields = ['titulo', 'texto']


@admin.register(MembroEquipe)
class MembroEquipeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'curso', 'ordem', 'ativo']
    list_filter = ['ativo', 'curso']
    search_fields = ['nome', 'email']


@admin.register(Pilar)
class PilarAdmin(admin.ModelAdmin):
    list_display = ['sigla', 'nome', 'ordem']


@admin.register(ItemLista)
class ItemListaAdmin(admin.ModelAdmin):
    list_display = ['texto', 'categoria', 'ordem']
    list_filter = ['categoria']


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ordem']


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'empresa', 'assunto', 'data_envio',
                    'respondido']
    list_filter = ['assunto', 'respondido', 'data_envio']
    search_fields = ['nome', 'email', 'empresa', 'mensagem']
    date_hierarchy = 'data_envio'


@admin.register(PraticaEstudio)
class PraticaEstudioAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'pilar', 'ordem']
    list_filter = ['pilar']
    search_fields = ['titulo', 'descricao']
