# Generated by Django 4.0.4 on 2022-05-03 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_genre_post_genero'),
    ]

    operations = [
        migrations.CreateModel(
            name='me_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(null=True, upload_to='imgs')),
                ('name', models.CharField(max_length=20)),
                ('ig', models.ImageField(null=True, upload_to='imgs')),
                ('fb', models.ImageField(null=True, upload_to='imgs')),
                ('tw', models.ImageField(null=True, upload_to='imgs')),
                ('yt', models.ImageField(null=True, upload_to='imgs')),
            ],
        ),
    ]