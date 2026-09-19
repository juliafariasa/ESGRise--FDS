import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_conteudo_inicial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemlista',
            name='categoria',
            field=models.CharField(choices=[('objetivo', 'Objetivo do produto'), ('pratica_fds', 'Conceito aplicado de FDS'), ('beneficio', 'Ganho para o estúdio')], max_length=20, verbose_name='Categoria'),
        ),
        migrations.CreateModel(
            name='PraticaEstudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120, verbose_name='Título')),
                ('descricao', models.TextField(verbose_name='Por que importa')),
                ('ordem', models.PositiveIntegerField(default=0, verbose_name='Ordem')),
                ('pilar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='praticas', to='forum.pilar', verbose_name='Pilar')),
            ],
            options={
                'verbose_name': 'Prática do estúdio',
                'verbose_name_plural': 'Práticas do estúdio',
                'ordering': ['pilar', 'ordem'],
            },
        ),
    ]
