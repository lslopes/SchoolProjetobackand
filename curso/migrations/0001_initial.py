# Generated by Django 2.2.1 on 2019-05-01 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alunos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomecurso', models.CharField(max_length=90, verbose_name='nomecurso')),
                ('horas', models.CharField(max_length=90, verbose_name='horas')),
                ('descrição', models.CharField(max_length=1000, verbose_name='descrição')),
                ('sigal', models.CharField(max_length=3, verbose_name='sigal')),
            ],
        ),
    ]
