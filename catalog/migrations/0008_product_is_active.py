# Generated by Django 4.2.3 on 2023-08-20 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_product_creation_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
