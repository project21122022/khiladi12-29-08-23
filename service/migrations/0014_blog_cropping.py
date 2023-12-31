# Generated by Django 4.2.1 on 2023-07-19 08:39

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0013_rename_blog_category_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('blog_image', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
