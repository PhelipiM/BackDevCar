# Generated by Django 4.1.7 on 2023-03-14 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0002_categoria'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Marcas',
            new_name='Marca',
        ),
    ]