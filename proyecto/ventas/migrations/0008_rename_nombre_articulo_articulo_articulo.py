# Generated by Django 4.1.2 on 2023-06-19 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0007_rename_articulo_articulo_id_articulo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='nombre_articulo',
            new_name='articulo',
        ),
    ]
