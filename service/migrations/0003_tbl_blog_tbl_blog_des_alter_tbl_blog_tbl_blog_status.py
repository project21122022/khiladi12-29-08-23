# Generated by Django 4.2.1 on 2023-06-29 12:59

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_tbl_blog_tbl_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_blog',
            name='tbl_blog_des',
            field=tinymce.models.HTMLField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='tbl_blog',
            name='tbl_blog_status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
