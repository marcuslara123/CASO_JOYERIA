# Generated by Django 4.1.2 on 2023-06-10 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_rename_ida_cliente_articulo_remove_articulo_ida_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='id',
            new_name='rut',
        ),
    ]
