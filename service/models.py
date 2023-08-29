from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from image_cropping import ImageCropField, ImageRatioField
from PIL import Image
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
#from django import forms

# class YourModelAdminForm(forms.ModelForm):
#     class Meta:
#         model = models.Model
#         fields = '__all__'
#         widgets = {
#             'post_title': forms.TextInput(attrs={'placeholder': 'Your Placeholder Text'}),
#             # Add other fields and their respective placeholder texts here if needed
#         }
        
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
    
    
class ad_category(models.Model):
    ads_cat_name=models.CharField(verbose_name="Ad Type",max_length=255,unique=True,null=True,default=None)
    ads_cat_slug=AutoSlugField(populate_from='ads_cat_name',unique=True,null=True,default=None)
    ads_cat_status=models.IntegerField(null=True,default=0)
    
    def __str__(self):
        return self.ads_cat_name

class ad(models.Model):
    ads_cat=models.ForeignKey("ad_category", verbose_name="Select Ad Type",null=True,default=None,on_delete=models.CASCADE)
    ad_url=models.CharField(max_length=255, verbose_name="Link URL",null=True,default=None)
    from_date=models.DateField()
    to_date=models.DateField()
    ad_image = models.FileField(upload_to='ads/')
    ad_counter=models.IntegerField(verbose_name="Counter",null=True,default=None)
    is_active=models.BooleanField(verbose_name="Is Active", default=False)
    post_date=models.DateTimeField(auto_now=True)
    post_status=models.IntegerField(null=True,default=0)

class seo_management(models.Model):
    pagename=models.CharField(max_length=255, verbose_name="Page Name",null=True,default=None)
    metatitle=models.CharField(max_length=60, verbose_name="Page Meta Title",null=True,default=None)
    metadescription=models.TextField(max_length=160, verbose_name="Page Meta Des",null=True,default=None)
    pageslug=models.CharField(max_length=160, verbose_name="Page Url",null=True,default=None)
    post_date=models.DateTimeField(auto_now=True)
    post_status=models.IntegerField(null=True,default=0)
    
    
class videopost(models.Model):
    VTYPE_CHOICES = (
        ('cricket','Cricket'),
('pridictions','Pridictions'),
('horseracing','Horseracing'),
('football','Football'),
('esports','Esports'),
('fantasy','Fantasy'),
    )
    videotype = models.CharField(verbose_name="Video Type", max_length=255, choices=VTYPE_CHOICES, default='active')
    video_title=models.CharField(max_length=60, verbose_name="Title (Lenth 60 Char)",null=True,default=None)
    video_short_des=models.CharField(max_length=160, verbose_name="Meta/Short Des",null=True,default=None)
    video_des=HTMLField(null=True,default=None)
    video_url=models.CharField(verbose_name="Youtube Video URL",max_length=255,default=True,null=True)
    # post_image=models.FileField(upload_to="blog/", max_length=255,null=True,default=None)
    thumnail = ImageCropField(upload_to='vidimage/', max_length=255,null=True,default=None)
    #image_crop = ImageRatioField('post_image', '430x360')
    
    def save(self, *args, **kwargs):
        # Override the save method to resize the image before saving
        super(videopost, self).save(*args, **kwargs)
        # Open the image
        img = Image.open(self.thumnail.path)
        # Set the desired size for cropping (width, height)
        desired_size = (300, 168)
        # Resize the image while maintaining the aspect ratio
        img.thumbnail(desired_size)
        # Save the resized image back to the original path
        img.save(self.thumnail.path)
    
    slug=AutoSlugField(populate_from='video_title',unique=True,null=True,default=None)
    video_tag=models.CharField(max_length=255,null=True,default=0)
   
    is_active=models.BooleanField(verbose_name="Is Active", default=True)
    video_date=models.DateTimeField(auto_now=True)
    video_status=models.IntegerField(null=True,default=0)
       
# Create your models here.
