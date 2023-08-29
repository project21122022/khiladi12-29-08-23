from django.db import models
from autoslug import AutoSlugField
from image_cropping import ImageCropField, ImageRatioField
from PIL import Image
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class category(models.Model):
    cat_name=models.CharField(max_length=255,unique=True,null=True,default=None)
    cat_slug=AutoSlugField(populate_from='cat_name',unique=True,null=True,default=None)
    cat_status=models.IntegerField(null=True,default=0)
    
    def __str__(self):
        return self.cat_name

class sub_category(models.Model):
    sub_cat=models.ForeignKey("category", verbose_name="Select Cetegory",null=True,default=None,on_delete=models.CASCADE)
    subcat_name=models.CharField(max_length=255,unique=True,null=True,default=None)
    subcat_slug=AutoSlugField(populate_from='subcat_name',unique=True,null=True,default=None)
    subcat_status=models.IntegerField(null=True,default=0)
    
    def __str__(self):
        return self.sub_cat.cat_name + "=>" + self.subcat_name
    
class post(models.Model):
    post_cat=models.ForeignKey("sub_category", verbose_name="Select Cetegory",null=True,default=None,on_delete=models.CASCADE)
    post_title=models.CharField(max_length=65, verbose_name="Title",null=True,default=None)
    post_short_des=models.CharField(max_length=160, verbose_name="Meta Des",null=True,default=None)
    post_des=RichTextUploadingField(null=True,default=0)
    # post_image=models.FileField(upload_to="blog/", max_length=255,null=True,default=None)
    post_image = ImageCropField(upload_to='blog/', max_length=255,null=True,default=None)
    #image_crop = ImageRatioField('post_image', '430x360')
    
    def save(self, *args, **kwargs):
        # Override the save method to resize the image before saving
        super(post, self).save(*args, **kwargs)
        # Open the image
        img = Image.open(self.post_image.path)
        # Set the desired size for cropping (width, height)
        desired_size = (940, 528)
        # Resize the image while maintaining the aspect ratio
        img.thumbnail(desired_size)
        # Save the resized image back to the original path
        img.save(self.post_image.path)
    
    slug=AutoSlugField(populate_from='post_title',unique=True,null=True,default=None)
    post_tag=models.TextField(null=True,default=0)
    
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='active')
    
    is_active=models.BooleanField(verbose_name="Make Banner", default=False)
    post_date=models.DateTimeField(auto_now=True)
    post_status=models.IntegerField(null=True,default=0)