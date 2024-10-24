# Generated by Django 5.1.1 on 2024-10-24 10:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.CharField(max_length=1)),
                ('ponteiro', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('tamanho', models.IntegerField()),
                ('endereco_inicial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerenciamento_arquivos.bloco')),
            ],
        ),
    ]