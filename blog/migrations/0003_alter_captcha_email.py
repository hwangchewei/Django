# Generated by Django 4.2.13 on 2024-07-19 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_captcha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='captcha',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
