# Generated by Django 4.1.2 on 2022-11-17 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_remove_serie_comments_alter_movie_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serie',
            name='owner',
        ),
    ]
