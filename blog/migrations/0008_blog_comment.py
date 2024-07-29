# Generated by Django 4.2.13 on 2024-07-29 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_date_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=100, unique=True)),
                ('date_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('blog_ky', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
    ]
