# Generated by Django 4.2.13 on 2024-07-29 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_blog_comment_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_comment',
            old_name='text',
            new_name='comment',
        ),
    ]