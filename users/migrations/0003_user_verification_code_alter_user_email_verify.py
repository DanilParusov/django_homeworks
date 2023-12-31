# Generated by Django 4.2.3 on 2023-08-18 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_email_verify'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_code',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_verify',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
