# Generated by Django 4.2.1 on 2023-08-08 10:27

import autoslug.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0024_alter_blog_blog_des'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(default=None, max_length=65, null=True, verbose_name='Title')),
                ('post_short_des', models.CharField(default=None, max_length=160, null=True, verbose_name='Meta Des')),
                ('post_des', ckeditor_uploader.fields.RichTextUploadingField(default=0, null=True)),
                ('post_image', image_cropping.fields.ImageCropField(default=None, max_length=255, null=True, upload_to='blog/')),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='post_title', unique=True)),
                ('post_tag', models.TextField(default=0, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=8)),
                ('is_active', models.BooleanField(default=False, verbose_name='Make Banner')),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('post_status', models.IntegerField(default=0, null=True)),
                ('post_cat', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.category', verbose_name='Select Cetegory')),
            ],
        ),
        migrations.DeleteModel(
            name='blog',
        ),
    ]
