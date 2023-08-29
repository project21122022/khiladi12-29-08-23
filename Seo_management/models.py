from django.db import models

# Create your models here.


class seo_optimization(models.Model):
    pagename=models.CharField(max_length=255, verbose_name="Page Name",null=True,default=None)
    metatitle=models.CharField(max_length=60, verbose_name="Page Meta Title",null=True,default=None)
    metadescription=models.TextField(max_length=160, verbose_name="Page Meta Des",null=True,default=None)
    pageslug=models.CharField(max_length=160, verbose_name="Page Url",null=True,default=None)
    post_date=models.DateTimeField(auto_now=True)
    post_status=models.IntegerField(null=True,default=0)