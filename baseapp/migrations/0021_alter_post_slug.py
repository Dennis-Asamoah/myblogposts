# Generated by Django 3.2.11 on 2022-05-24 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0020_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]