# Generated by Django 4.1.7 on 2024-01-04 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_cartoes_identificador_linha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartoes',
            name='numero_lote',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
