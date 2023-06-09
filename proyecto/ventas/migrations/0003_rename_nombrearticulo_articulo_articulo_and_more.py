# Generated by Django 4.1.2 on 2023-06-10 04:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_articulo_delete_articulos_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='nombreArticulo',
            new_name='articulo',
        ),
        migrations.RemoveField(
            model_name='articulo',
            name='activo',
        ),
        migrations.AddField(
            model_name='cliente',
            name='idA',
            field=models.ForeignKey(db_column='idArticulo', default=datetime.datetime(2023, 6, 10, 4, 4, 50, 388429, tzinfo=datetime.timezone.utc), on_delete=django.db.models.deletion.CASCADE, to='ventas.articulo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(default=datetime.datetime(2023, 6, 10, 4, 5, 1, 511020, tzinfo=datetime.timezone.utc), max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articulo',
            name='idA',
            field=models.AutoField(db_column='idArticulo', primary_key=True, serialize=False),
        ),
    ]
