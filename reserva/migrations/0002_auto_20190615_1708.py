# Generated by Django 2.2.2 on 2019-06-15 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reserva',
            options={'ordering': ('data_solicitacao',), 'verbose_name': 'Reserva', 'verbose_name_plural': 'Reservas'},
        ),
    ]
