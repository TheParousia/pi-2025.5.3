# Generated by Django 4.2.16 on 2025-03-24 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='static/imagem/produtos/'),
        ),
    ]
