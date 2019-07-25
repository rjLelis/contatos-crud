# Generated by Django 2.2.3 on 2019-07-24 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=254)),
                ('data_nascimento', models.DateField()),
            ],
        ),
    ]
