# Generated by Django 4.1.3 on 2022-11-30 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0003_minicursos'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='minicursos',
            field=models.ManyToManyField(to='formulario.minicursos'),
        ),
    ]
