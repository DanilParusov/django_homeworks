# Generated by Django 4.2.3 on 2023-08-11 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(max_length=150, verbose_name='Slug'),
        ),
    ]
