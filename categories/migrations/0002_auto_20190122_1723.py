# Generated by Django 2.1.5 on 2019-01-22 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='nature',
            field=models.CharField(choices=[('ingreso', 'Ingreso'), ('egreso', 'Egreso')], max_length=2),
        ),
    ]