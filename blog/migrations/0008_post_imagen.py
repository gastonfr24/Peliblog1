# Generated by Django 4.0.4 on 2022-05-03 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(null=True, upload_to='peliculas'),
        ),
    ]