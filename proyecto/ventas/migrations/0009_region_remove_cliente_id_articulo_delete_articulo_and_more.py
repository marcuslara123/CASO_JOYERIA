# Generated by Django 4.1.2 on 2023-06-19 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0008_rename_nombre_articulo_articulo_articulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.AutoField(db_column='idRegion', primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='id_articulo',
        ),
        migrations.DeleteModel(
            name='Articulo',
        ),
       migrations.AddField(
        model_name='cliente',
        name='id_region',
        field=models.ForeignKey(db_column='idRegion', default=0, on_delete=django.db.models.deletion.CASCADE, to='ventas.region'),
        preserve_default=False,
        ),
    ]
