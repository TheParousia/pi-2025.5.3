# Generated by Django 5.1.7 on 2025-04-07 19:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('dataDeNascimento', models.DateField()),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uf', models.CharField(max_length=2)),
                ('rua', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=8)),
                ('numeroDaCasa', models.IntegerField()),
                ('logradouro', models.CharField(max_length=100)),
                ('pontoReferencia', models.CharField(max_length=100)),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
