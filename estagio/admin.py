from django.contrib import admin
from django.db import models
from django.forms import Select, Textarea
from django.utils.html import format_html

from .models import (
    Boletos,
    CidadesAtuacao,
    CidadesOrgaoAtuacao,
    CidadesRealizacaoProvas,
    Editais,
    InscricaoCidades,
    Inscricoes,
    Notas,
    Turnos,
    Universidades,
)

class AuditoriaAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_max_show_all = 20
    readonly_fields = (
        'created_at',
        'created_by',
        'updated_at',
        'updated_by',
    )



class AuditoriaAdminTabularInline(admin.TabularInline):
    list_per_page = 5
    list_max_show_all = 20
    readonly_fields = (
        'created_at',
        'created_by',
        'updated_at',
        'updated_by',
    )
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={
                'rows': 4,
                'cols': 40
            })
        },
        models.ForeignKey: {
            'widget': Select(attrs={
                'style': 'width:150px'
            })
        },
    }


class AuditoriaAdminStackedInline(admin.StackedInline):
    list_per_page = 5
    list_max_show_all = 20
    readonly_fields = (
        'created_at',
        'created_by',
        'updated_at',
        'updated_by',
    )

@admin.register(Boletos)
class BoletosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'codigo_barras',
        'inscricao_id',
        'pago',
    )
    list_filter = (
        'codigo_barras',
        'inscricao_id',
        'pago',
    )
    list_display = (
        'codigo_barras',
        'inscricao_id',
        'pago',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(CidadesAtuacao)
class CidadesAtuacaoAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'fortaleza',
        'interior',
        'edital_id',
    )
    list_filter = (
        'fortaleza',
        'interior',
        'edital_id',
    )
    list_display = (
        'fortaleza',
        'interior',
        'edital_id',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(CidadesOrgaoAtuacao)
class CidadesOrgaoAtuacaoAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'nome',
        'ativo',
    )
    list_filter = (
        'nome',
        'ativo',
    )
    list_display = (
        'nome',
        'ativo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(CidadesRealizacaoProvas)
class CidadesRealizacaoProvasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'nome',
        'ativo',
    )
    list_filter = (
        'nome',
        'ativo',
    )
    list_display = (
        'nome',
        'ativo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]




class CidadesAtuacaoInlineAdmin(AuditoriaAdminTabularInline):
    model = CidadesAtuacao
    list_display = (
        'fortaleza',
        'interior',
        'edital_id',
    )


@admin.register(Editais)
class EditaisAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'descricao',
    )
    list_filter = (
        'descricao',
    )
    list_display = (
        'descricao',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
        CidadesAtuacaoInlineAdmin,
    ]



@admin.register(InscricaoCidades)
class InscricaoCidadesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'inscricao_id',
        'descricao',
        'turno',
    )
    list_filter = (
        'inscricao_id',
        'descricao',
        'turno',
    )
    list_display = (
        'inscricao_id',
        'descricao',
        'turno',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Inscricoes)
class InscricoesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'nome',
        'cpf',
        'email',
    )
    list_filter = (
        'nome',
        'cpf',
        'email',
    )
    list_display = (
        'nome',
        'cpf',
        'email',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Notas)
class NotasAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'inscricao',
        'nota',
    )
    list_filter = (
        'inscricao',
        'nota',
    )
    list_display = (
        'inscricao',
        'nota',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Turnos)
class TurnosAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
    )
    list_filter = (
    )
    list_display = (
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]



@admin.register(Universidades)
class UniversidadesAdmin(AuditoriaAdmin):
    actions = []
    search_fields = (
        'descricao',
        'ativo',
    )
    list_filter = (
        'descricao',
        'ativo',
    )
    list_display = (
        'descricao',
        'ativo',
    )
    readonly_fields = AuditoriaAdmin.readonly_fields + (
    )
    inlines = [
    ]