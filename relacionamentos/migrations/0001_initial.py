# Generated by Django 2.1.2 on 2019-01-24 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('sexo', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('signo', models.CharField(max_length=50)),
                ('Gosto_musical', models.CharField(max_length=50)),
            ],
        ),
    ]
