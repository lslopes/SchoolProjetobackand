# Generated by Django 2.2.1 on 2019-05-01 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='professores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=90, verbose_name='nome')),
                ('especialidades', models.CharField(max_length=90, verbose_name='especialidades')),
                ('graduacoes', models.CharField(max_length=1000, verbose_name='graduacoes')),
                ('vinculo_dsicipilnas', models.CharField(max_length=90, verbose_name='vinculo_dsicipilnas')),
            ],
        ),
    ]
