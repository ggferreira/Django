# Generated by Django 3.1.7 on 2021-03-31 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aperitivos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(max_length=32),
        ),
    ]
