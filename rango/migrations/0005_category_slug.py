# Generated by Django 2.1.5 on 2019-01-15 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_page_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
