# Generated by Django 3.2.6 on 2021-08-21 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_receita', models.CharField(max_length=255)),
                ('tempo_preparo', models.TextField()),
                ('rendimento', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('modo_preparo', models.TextField()),
                ('ingredientes', models.TextField()),
                ('data_receita', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
