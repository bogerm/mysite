# Generated by Django 5.1.6 on 2025-02-11 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='movie_type',
            field=models.CharField(default='action', max_length=200),
        ),
    ]
