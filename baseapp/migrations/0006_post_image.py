# Generated by Django 3.2.11 on 2022-05-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0005_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]