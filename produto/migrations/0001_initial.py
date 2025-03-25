# Generated by Django 4.2.16 on 2025-03-25 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='static/imagem/produtos/')),
                ('imagem2', models.ImageField(blank=True, null=True, upload_to='static/imagem/produtos/')),
                ('imagem3', models.ImageField(blank=True, null=True, upload_to='static/imagem/produtos/')),
                ('imagem4',models.ImageField(blank=True, null=True, upload_to='static/imagem/produtos/')),
                ('descrição', models.TextField()),
                ('preço', models.DecimalField(decimal_places=2, max_digits=15)),
                ('quantidade_estoque', models.IntegerField()),
            ],
        ),
    ]
