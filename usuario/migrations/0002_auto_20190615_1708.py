# Generated by Django 2.2.2 on 2019-06-15 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recurso', '0002_auto_20190615_1423'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ('usuario',), 'verbose_name': 'Usuário', 'verbose_name_plural': 'Usuários'},
        ),
        migrations.AddField(
            model_name='usuario',
            name='recursos',
            field=models.ManyToManyField(to='recurso.Recurso'),
        ),
    ]
