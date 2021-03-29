from django.db import models
#from django_currentuser.db.models import CurrentUserField
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from .choices import *

User = get_user_model()

class BaseModel(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(
        #CurrentUserField(),
        User,
        on_delete=models.DO_NOTHING,
        related_name='%(class)s_created_by',
        blank=True,
        null=True,
        default=User
    )
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='%(class)s_update_by',
        blank=True,
        null=True
    )

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.created_by or not self.created_at:
            self.created_by = get_current_user()
            self.created_at = timezone.now()
        else:
            self.update_by = get_current_user()
            self.update_at = timezone.now()
        super(BaseModel, self).save(force_insert=False, force_update=False, using=None,
                                    update_fields=None)

class Boletos(BaseModel):

    cols = {
        'codigo_barras': 3,
        'inscricao_id': 3,
        'pago': 3,
        'vencimento': 3,
        'data_emissao': 3,
        'banco': 3,
        'valor': 3,
        'data_pagamento': 3,
        'valor_pago': 3,
        'data_credito': 3,
        'forma_pagamento': 3,
        'sequencial_guia': 3,
        'importacao_boleto_id': 3,
        'codigo_barras_sem_digitos': 3,
        'identificador_dae': 3,}
    
    codigo_barras = models.CharField(
        'Codigo Barras', 
        max_length=255, 
        blank=True, 
        null=True, )
    inscricao_id = models.ForeignKey(
        'estagio.Inscricoes', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_inscricao_id', 
        blank=True, 
        null=True, )
    pago = models.BooleanField(
        'Pago', 
        blank=True, )
    vencimento = models.DateField(
        'Vencimento', 
        blank=True, 
        null=True, )
    data_emissao = models.DateField(
        'Data Emissão', 
        blank=True, 
        null=True, )
    banco = models.CharField(
        'Banco', 
        max_length=255, 
        blank=True, 
        null=True, )
    valor = models.CharField(
        'Valor', 
        max_length=255, 
        blank=True, 
        null=True, )
    data_pagamento = models.DateField(
        'Data Pagamento', 
        blank=True, 
        null=True, )
    valor_pago = models.CharField(
        'Valor Pago', 
        max_length=255, 
        blank=True, 
        null=True, )
    data_credito = models.CharField(
        'Data Credito', 
        max_length=255, 
        blank=True, 
        null=True, )
    forma_pagamento = models.CharField(
        'Forma Pagamento', 
        max_length=255, 
        blank=True, 
        null=True, )
    sequencial_guia = models.CharField(
        'Sequencial Guia', 
        max_length=255, 
        blank=True, 
        null=True, )
    importacao_boleto_id = models.IntegerField(
        'Importação Boleto', 
        blank=True, 
        null=True, )
    codigo_barras_sem_digitos = models.CharField(
        'Codigo Barras Sem Digitos', 
        max_length=255, 
        blank=True, 
        null=True, )
    identificador_dae = models.CharField(
        'Identificador DAE', 
        max_length=255, 
        blank=True, 
        null=True, )
    

    def __str__(self):
        return '{}'.format(self.codigo_barras)

    class Meta:
        verbose_name = 'Boleto'
        verbose_name_plural = 'Boletos'



class CidadesAtuacao(BaseModel):

    cols = {
        'fortaleza': 4,
        'interior': 4,
        'edital_id': 4,}
    
    fortaleza = models.BooleanField(
        'Fortaleza', 
        blank=True, )
    interior = models.BooleanField(
        'Interior', 
        blank=True, )
    edital_id = models.ForeignKey(
        'estagio.Editais', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_edital_id', 
        blank=True, 
        null=True, )
    

    def __str__(self):
        return '{}'.format(self.fortaleza)

    class Meta:
        verbose_name = 'Cidade de Atuacão'
        verbose_name_plural = 'Cidades de Atuacão'



class CidadesOrgaoAtuacao(BaseModel):

    cols = {
        'nome': 6,
        'ativo': 6,}
    
    nome = models.CharField(
        'Nome', 
        max_length=255, 
        blank=True, 
        null=True, )
    ativo = models.BooleanField(
        'Ativo', 
        blank=True, )
    

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        verbose_name = 'Cidade do Orgão de Atuação'
        verbose_name_plural = 'Cidades dos Orgãos de Atuação'



class CidadesRealizacaoProvas(BaseModel):

    cols = {
        'nome': 6,
        'ativo': 6,}
    
    nome = models.CharField(
        'Nome', 
        max_length=255, 
        blank=True, 
        null=True, )
    ativo = models.BooleanField(
        'Ativo', 
        blank=True, )
    

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        verbose_name = 'Cidade da Realizacao da Prova'
        verbose_name_plural = 'Cidades Realizacao Provas'



class Editais(BaseModel):

    cols = {
        'descricao': 3,
        'valor': 3,
        'vencimento': 3,
        'pago': 3,
        'interior': 3,
        'ativo': 3,}
    
    descricao = models.CharField(
        'Descrição', 
        max_length=255, 
        blank=True, 
        null=True, )
    valor = models.CharField(
        'Valor', 
        max_length=255, 
        blank=True, 
        null=True, )
    vencimento = models.DateField(
        'Vencimento', 
        blank=True, 
        null=True, )
    pago = models.BooleanField(
        'Pago', 
        blank=True, )
    interior = models.BooleanField(
        'Interior', 
        blank=True, )
    ativo = models.BooleanField(
        'Ativo', 
        blank=True, )
    

    def __str__(self):
        return '{}'.format(self.descricao)

    class Meta:
        verbose_name = 'Edital'
        verbose_name_plural = 'Editais'



class InscricaoCidades(BaseModel):

    cols = {
        'inscricao_id': 4,
        'descricao': 4,
        'turno': 4,}
    
    inscricao_id = models.ForeignKey(
        'estagio.Inscricoes', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_inscricao_id', 
        blank=True, 
        null=True, )
    descricao = models.CharField(
        'Descrição', 
        max_length=255, 
        blank=True, 
        null=True, )
    turno = models.CharField(
        'Turno', 
        max_length=255, 
        blank=True, 
        null=True, )
    

    def __str__(self):
        return '{}'.format(self.descricao)

    class Meta:
        verbose_name = 'Inscricao Cidade'
        verbose_name_plural = 'Inscricao Cidades'



class Inscricoes(BaseModel):

    cols = {
        'nome': 3,
        'identidade': 3,
        'cpf': 3,
        'endereco': 3,
        'bairro': 3,
        'telefone': 3,
        'cep': 3,
        'celular': 3,
        'email': 3,
        'curso': 3,
        'turno': 3,
        'universidade': 3,
        'comarcas_de_cidades': 3,
        'deficiente': 3,
        'condicao_especial': 3,
        'cidade': 3,
        'descricao_deficiencia': 3,
        'cidade_realizacao': 3,
        'ativo': 3,
        'edital': 3,
        'condicao_especial_descricao': 3,
        'documento_comprobatorio_isencao': 3,
        'pedido_isencao': 3,
        'cota_racial': 3,
        'condicao_cota_racial': 3,
        'documento_auto_declaracao': 3,}
    
    nome = models.CharField(
        'Nome', 
        max_length=255, 
        blank=True, 
        null=True, )
    identidade = models.CharField(
        'Identidade', 
        max_length=255, 
        blank=True, 
        null=True, )
    cpf = models.CharField(
        'CPF', 
        max_length=255, 
        blank=True, 
        null=True, )
    endereco = models.CharField(
        'Endereco', 
        max_length=255, 
        blank=True, 
        null=True, )
    bairro = models.CharField(
        'Bairro', 
        max_length=255, 
        blank=True, 
        null=True, )
    telefone = models.CharField(
        'Telefone', 
        max_length=255, 
        blank=True, 
        null=True, )
    cep = models.CharField(
        'CEP', 
        max_length=255, 
        blank=True, 
        null=True, )
    celular = models.CharField(
        'Celular', 
        max_length=255, 
        blank=True, 
        null=True, )
    email = models.CharField(
        'Email', 
        max_length=255, 
        blank=True, 
        null=True, )
    curso = models.CharField(
        'Curso', 
        choices=CHOICES_CURSO, 
        max_length=255, 
        blank=True, 
        null=True, 
        default='Direito', )
    turno = models.ForeignKey(
        'estagio.Turnos', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_turno', 
        blank=True, 
        null=True, )
    universidade = models.ForeignKey(
        'estagio.Universidades', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_universidade', 
        blank=True, 
        null=True, )
    comarcas_de_cidades = models.CharField(
        'Comarcas De Cidades', 
        max_length=255, 
        blank=True, 
        null=True, )
    deficiente = models.BooleanField(
        'Deficiente', 
        blank=True, )
    condicao_especial = models.BooleanField(
        'Condição Especial', 
        blank=True, )
    cidade = models.ForeignKey(
        'estagio.CidadesAtuacao', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_cidade', 
        blank=True, 
        null=True, )
    descricao_deficiencia = models.CharField(
        'Descrição Deficiencia', 
        max_length=255, 
        blank=True, 
        null=True, )
    cidade_realizacao = models.ForeignKey(
        'estagio.CidadesRealizacaoProvas', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_cidade_realizacao', 
        blank=True, 
        null=True, )
    ativo = models.BooleanField(
        'Ativo', 
        blank=True, )
    edital = models.ForeignKey(
        'estagio.Editais', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_edital', 
        blank=True, 
        null=True, )
    condicao_especial_descricao = models.CharField(
        'Condição Especial Descrição', 
        max_length=255, 
        blank=True, 
        null=True, )
    documento_comprobatorio_isencao = models.CharField(
        'Documento Comprobatorio Isenção', 
        max_length=255, 
        blank=True, 
        null=True, )
    pedido_isencao = models.BooleanField(
        'Pedido Isenção', 
        blank=True, )
    cota_racial = models.BooleanField(
        'Cota Racial', 
        blank=True, )
    condicao_cota_racial = models.CharField(
        'Condição Cota Racial', 
        max_length=255, 
        blank=True, 
        null=True, )
    documento_auto_declaracao = models.CharField(
        'Documento Auto Declaração', 
        max_length=255, 
        blank=True, 
        null=True, )
    

    def __str__(self):
        return '{} - {} - {}'.format(self.nome, self.cpf, self.email)

    class Meta:
        verbose_name = 'Inscricão'
        verbose_name_plural = 'Inscricoes'



class Notas(BaseModel):

    cols = {
        'inscricao': 6,
        'nota': 6,}
    
    inscricao = models.ForeignKey(
        'estagio.Inscricoes', 
        on_delete=models.PROTECT,  
        related_name='%(class)s_inscricao', 
        help_text='?', 
        blank=True, 
        null=True, )
    nota = models.IntegerField(
        'Nota', 
        help_text='?', 
        blank=True, 
        null=True, )
    

    def __str__(self):
        return '{}'.format(self.inscricao)

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'



class Turnos(BaseModel):

    cols = {
        'nome': 6,
        'ativo': 6,}
    
    nome = models.CharField(
        'Nome', 
        max_length=255, 
        blank=True, 
        null=True, )
    ativo = models.BooleanField(
        'Ativo', 
        blank=True, )
    

    def __str__(self):
        return ''.format()

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'



class Universidades(BaseModel):

    cols = {
        'descricao': 6,
        'ativo': 6,}
    
    descricao = models.CharField(
        'Descrição', 
        max_length=255, 
        blank=True, 
        null=True, )
    ativo = models.BooleanField(
        'Ativo', 
        blank=True, )
    

    def __str__(self):
        return '{}'.format(self.descricao)

    class Meta:
        verbose_name = 'Universidade'
        verbose_name_plural = 'Universidades'
