# Generated by Django 4.1.6 on 2023-02-18 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ThirdBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='plan/')),
                ('name1', models.CharField(max_length=255, verbose_name='Название ')),
                ('desc1', models.TextField(verbose_name='Описание')),
                ('img2', models.ImageField(upload_to='plan/')),
                ('name2', models.CharField(max_length=255, verbose_name='Название ')),
                ('desc2', models.TextField(verbose_name='Описание')),
                ('img3', models.ImageField(upload_to='plan/')),
                ('name3', models.CharField(max_length=255, verbose_name='Название ')),
                ('desc3', models.TextField(verbose_name='Описание')),
                ('img4', models.ImageField(upload_to='plan/')),
                ('name4', models.CharField(max_length=255, verbose_name='Название ')),
                ('desc4', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name_plural': 'План',
            },
        ),
    ]
