# Generated by Django 4.2.1 on 2023-07-19 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0016_remove_blog_blog_make_banner_remove_blog_is_banner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=8),
        ),
    ]
