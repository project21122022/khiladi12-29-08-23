# Generated by Django 4.2.1 on 2023-06-29 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tbl_blog_icon', models.CharField(max_length=50)),
                ('tbl_blog_cat', models.CharField(max_length=255)),
                ('tbl_blog_blog', models.TextField()),
                ('tbl_blog_date', models.DateTimeField(auto_now=True)),
                ('tbl_blog_status', models.IntegerField(max_length=2)),
            ],
        ),
    ]
