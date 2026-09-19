from django.db import models


class SecaoConteudo(models.Model):
    """Bloco de texto exibido em uma das paginas do site."""

    PAGINA_INDEX = 'index'
    PAGINA_QUEM_SOMOS = 'quem_somos'
    PAGINA_SOBRE_PROJETO = 'sobre_projeto'

    PAGINA_CHOICES = [
        (PAGINA_INDEX, 'Início'),
        (PAGINA_QUEM_SOMOS, 'Quem Somos'),
        (PAGINA_SOBRE_PROJETO, 'Sobre o Projeto'),
    ]

    pagina = models.CharField('Página', max_length=20, choices=PAGINA_CHOICES)
    titulo = models.CharField('Título', max_length=150)
    texto = models.TextField('Texto')
    ordem = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        verbose_name = 'Seção de conteúdo'
        verbose_name_plural = 'Seções de conteúdo'
        ordering = ['pagina', 'ordem']

    def __str__(self):
        return f'{self.get_pagina_display()}: {self.titulo}'


class MembroEquipe(models.Model):
    """Integrante da equipe, exibido na pagina Quem Somos."""

    nome = models.CharField('Nome completo', max_length=150)
    email = models.EmailField('E-mail da school')
    curso = models.CharField('Curso e turma', max_length=100,
                             default='Ciências da Computação - Turma A')
    ordem = models.PositiveIntegerField('Ordem', default=0)
    ativo = models.BooleanField('Membro ativo', default=True)

    class Meta:
        verbose_name = 'Membro da equipe'
        verbose_name_plural = 'Membros da equipe'
        ordering = ['ordem', 'nome']

    def __str__(self):
        return self.nome

    @property
    def inicial(self):
        return self.nome[:1].upper()


class Pilar(models.Model):
    """Pilar do ESG: Ambiental, Social e Governanca."""

    sigla = models.CharField('Sigla', max_length=2)
    nome = models.CharField('Nome', max_length=60)
    descricao = models.TextField('Descrição')
    ordem = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        verbose_name = 'Pilar ESG'
        verbose_name_plural = 'Pilares ESG'
        ordering = ['ordem']

    def __str__(self):
        return f'{self.sigla} - {self.nome}'


class ItemLista(models.Model):
    """Item de lista exibido na pagina Sobre o Projeto."""

    CATEGORIA_OBJETIVO = 'objetivo'
    CATEGORIA_PRATICA_FDS = 'pratica_fds'
    CATEGORIA_BENEFICIO = 'beneficio'

    CATEGORIA_CHOICES = [
        (CATEGORIA_OBJETIVO, 'Objetivo do produto'),
        (CATEGORIA_PRATICA_FDS, 'Conceito aplicado de FDS'),
        (CATEGORIA_BENEFICIO, 'Ganho para o estúdio'),
    ]

    categoria = models.CharField('Categoria', max_length=20,
                                 choices=CATEGORIA_CHOICES)
    texto = models.CharField('Texto', max_length=255)
    ordem = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        verbose_name = 'Item de lista'
        verbose_name_plural = 'Itens de lista'
        ordering = ['categoria', 'ordem']

    def __str__(self):
        return f'{self.get_categoria_display()}: {self.texto[:40]}'


class Tecnologia(models.Model):
    """Tecnologia usada no desenvolvimento do produto."""

    nome = models.CharField('Nome', max_length=60)
    descricao = models.TextField('Descrição')
    ordem = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        verbose_name = 'Tecnologia'
        verbose_name_plural = 'Tecnologias'
        ordering = ['ordem', 'nome']

    def __str__(self):
        return self.nome


class PraticaEstudio(models.Model):
    """Prática de ESG aplicada à rotina de um estúdio de tatuagem.

    Cada prática pertence a um pilar (Ambiental, Social ou Governança). A
    chave estrangeira permite listar as práticas de um pilar no template com
    pilar.praticas.all.
    """

    pilar = models.ForeignKey(
        Pilar,
        on_delete=models.CASCADE,
        related_name='praticas',
        verbose_name='Pilar',
    )
    titulo = models.CharField('Título', max_length=120)
    descricao = models.TextField('Por que importa')
    ordem = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        verbose_name = 'Prática do estúdio'
        verbose_name_plural = 'Práticas do estúdio'
        ordering = ['pilar', 'ordem']

    def __str__(self):
        return f'{self.pilar.sigla} - {self.titulo}'


class Contato(models.Model):
    """Mensagem gravada pelo formulario da pagina Fale Conosco."""

    ASSUNTO_DUVIDA = 'duvida'
    ASSUNTO_PARCERIA = 'parceria'
    ASSUNTO_SUGESTAO = 'sugestao'
    ASSUNTO_SUPORTE = 'suporte'
    ASSUNTO_OUTRO = 'outro'

    ASSUNTO_CHOICES = [
        (ASSUNTO_DUVIDA, 'Dúvida sobre a plataforma'),
        (ASSUNTO_PARCERIA, 'Proposta de parceria'),
        (ASSUNTO_SUGESTAO, 'Sugestão de melhoria'),
        (ASSUNTO_SUPORTE, 'Suporte técnico'),
        (ASSUNTO_OUTRO, 'Outro assunto'),
    ]

    nome = models.CharField('Nome', max_length=120)
    email = models.EmailField('E-mail')
    empresa = models.CharField('Empresa', max_length=120, blank=True)
    assunto = models.CharField('Assunto', max_length=20,
                               choices=ASSUNTO_CHOICES,
                               default=ASSUNTO_DUVIDA)
    mensagem = models.TextField('Mensagem')
    data_envio = models.DateTimeField('Data de envio')
    respondido = models.BooleanField('Respondido', default=False)

    class Meta:
        verbose_name = 'Contato recebido'
        verbose_name_plural = 'Contatos recebidos'
        ordering = ['-data_envio']

    def __str__(self):
        return f'{self.nome} - {self.get_assunto_display()}'
