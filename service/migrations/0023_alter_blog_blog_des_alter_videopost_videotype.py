# Generated by Django 4.1 on 2023-08-07 10:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0022_videopost_alter_seo_management_metadescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_des',
            field=ckeditor.fields.RichTextField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='videopost',
            name='videotype',
            field=models.CharField(choices=[('cricket', 'Cricket'), ('pridictions', 'Pridictions'), ('horseracing', 'Horseracing'), ('football', 'Football'), ('esports', 'Esports'), ('fantasy', 'Fantasy')], default='active', max_length=255, verbose_name='Video Type'),
        ),
    ]
