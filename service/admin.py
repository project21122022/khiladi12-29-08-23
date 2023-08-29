from django.contrib import admin
from service.models import post
from service.models import sub_category
from service.models import category
from service.models import ad_category
from service.models import ad
from service.models import videopost
from service.models import seo_management
from django.contrib.auth.models import User


class Post_cat(admin.ModelAdmin):
    list_display=('cat_name','cat_slug','cat_status')
admin.site.register(category,Post_cat)

class Post_subcat(admin.ModelAdmin):
    list_display=('subcat_name','subcat_slug','subcat_status')
admin.site.register(sub_category,Post_subcat)

class Post_Admin(admin.ModelAdmin):
    list_display=('post_title','post_date','slug','post_image','is_active','status','post_cat','post_status')
    cropping_fields = {'image_crop': ('post_image',)}
    #crop_fields = ['post_image'] #tapple
    
    list_editable=('status','is_active',)

admin.site.register(post,Post_Admin)

class Video_Post(admin.ModelAdmin):
    list_display=('video_title','video_url','videotype','thumnail','slug','is_active','video_date')
    
    list_editable=('is_active',)

admin.site.register(videopost,Video_Post)

class Ad_category(admin.ModelAdmin):
    list_display=('ads_cat_name','ads_cat_slug','ads_cat_status')
class Ad_post(admin.ModelAdmin):
    list_display=('ads_cat','ad_url','from_date','to_date','ad_counter','is_active')
    list_editable=('is_active',)

admin.site.register(ad_category,Ad_category)
admin.site.register(ad,Ad_post)

class SEO_Management(admin.ModelAdmin):
    list_display=('pagename','metatitle','metadescription','pageslug','post_date','post_status')

admin.site.register(seo_management,SEO_Management)
# Register your models here.
