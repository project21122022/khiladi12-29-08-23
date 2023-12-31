# Generated by Django 4.2.1 on 2023-07-19 10:28

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0017_blog_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image_crop',
            field=image_cropping.fields.ImageRatioField('blog_image', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='image crop'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=image_cropping.fields.ImageCropField(upload_to='blog/'),
        ),
    ]
