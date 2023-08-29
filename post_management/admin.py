from django.contrib import admin
from post_management.models import category
from post_management.models import sub_category
from post_management.models import post
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