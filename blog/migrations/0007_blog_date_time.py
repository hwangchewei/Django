# Generated by Django 4.2.13 on 2024-07-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
