# Generated by Django 4.2.1 on 2023-07-24 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0019_ads_category_remove_blog_image_crop_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ads',
            new_name='ad',
        ),
        migrations.RenameModel(
            old_name='ads_category',
            new_name='ad_category',
        ),
    ]