# Generated by Django 3.2.9 on 2021-11-23 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster_path',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]