# Generated by Django 4.0.1 on 2022-02-02 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.CharField(max_length=30)),
                ('Phone', models.CharField(max_length=15)),
                ('Email', models.CharField(max_length=30)),
                ('Skype', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=30)),
                ('Langages', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('FirstName', models.CharField(max_length=30)),
                ('Nationality', models.CharField(max_length=30)),
                ('Freelance', models.CharField(default='Disponible', max_length=30)),
            ],
        ),
    ]
