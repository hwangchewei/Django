# Generated by Django 4.2.13 on 2024-07-19 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_captcha_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='valid_p',
        ),
    ]