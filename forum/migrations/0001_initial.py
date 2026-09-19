from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('empresa', models.CharField(blank=True, max_length=120, verbose_name='Empresa')),
                ('assunto', models.CharField(choices=[('duvida', 'Dúvida sobre a plataforma'), ('parceria', 'Proposta de parceria'), ('sugestao', 'Sugestão de melhoria'), ('suporte', 'Suporte técnico'), ('outro', 'Outro assunto')], default='duvida', max_length=20, verbose_name='Assunto')),
                ('mensagem', models.TextField(verbose_name='Mensagem')),
                ('data_envio', models.DateTimeField(verbose_name='Data de envio')),
                ('respondido', models.BooleanField(default=False, verbose_name='Respondido')),
            ],
            options={
                'verbose_name': 'Contato recebido',
                'verbose_name_plural': 'Contatos recebidos',
                'ordering': ['-data_envio'],
            },
        ),
        migrations.CreateModel(
            name='ItemLista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(choices=[('objetivo', 'Objetivo do produto'), ('pratica_fds', 'Conceito aplicado de FDS')], max_length=20, verbose_name='Categoria')),
                ('texto', models.CharField(max_length=255, verbose_name='Texto')),
                ('ordem', models.PositiveIntegerField(default=0, verbose_name='Ordem')),
            ],
            options={
                'verbose_name': 'Item de lista',
                'verbose_name_plural': 'Itens de lista',
                'ordering': ['categoria', 'ordem'],
            },
        ),
        migrations.CreateModel(
            name='MembroEquipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome completo')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail da school')),
                ('curso', models.CharField(default='Ciências da Computação - Turma A', max_length=100, verbose_name='Curso e turma')),
                ('ordem', models.PositiveIntegerField(default=0, verbose_name='Ordem')),
                ('ativo', models.BooleanField(default=True, verbose_name='Membro ativo')),
            ],
            options={
                'verbose_name': 'Membro da equipe',
                'verbose_name_plural': 'Membros da equipe',
                'ordering': ['ordem', 'nome'],
            },
        ),
        migrations.CreateModel(
            name='Pilar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=2, verbose_name='Sigla')),
                ('nome', models.CharField(max_length=60, verbose_name='Nome')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('ordem', models.PositiveIntegerField(default=0, verbose_name='Ordem')),
            ],
            options={
                'verbose_name': 'Pilar ESG',
                'verbose_name_plural': 'Pilares ESG',
                'ordering': ['ordem'],
            },
        ),
        migrations.CreateModel(
            name='SecaoConteudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagina', models.CharField(choices=[('index', 'Início'), ('quem_somos', 'Quem Somos'), ('sobre_projeto', 'Sobre o Projeto')], max_length=20, verbose_name='Página')),
                ('titulo', models.CharField(max_length=150, verbose_name='Título')),
                ('texto', models.TextField(verbose_name='Texto')),
                ('ordem', models.PositiveIntegerField(default=0, verbose_name='Ordem')),
            ],
            options={
                'verbose_name': 'Seção de conteúdo',
                'verbose_name_plural': 'Seções de conteúdo',
                'ordering': ['pagina', 'ordem'],
            },
        ),
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60, verbose_name='Nome')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('ordem', models.PositiveIntegerField(default=0, verbose_name='Ordem')),
            ],
            options={
                'verbose_name': 'Tecnologia',
                'verbose_name_plural': 'Tecnologias',
                'ordering': ['ordem', 'nome'],
            },
        ),
    ]
