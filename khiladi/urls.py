"""
URL configuration for khiladi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from khiladi import views
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header="12thkhiladi Admin"
admin.site.site_title="12thkhiladi Admin"
admin.site.index_title="Dasboard"

urlpatterns = [
    path('', views.home, name="home"),
    path('about-us', views.aboutUs, name="about-us"),
    path('login', views.login, name="login"),
    
    path('video/<slug>', views.videocategory, name="videocategory"),
    path('<slug>', views.Category, name="category"),
    path('<str:catlink>/<slug>', views.newsdetails, name="newsdetails"),
    
    
    path('services', views.Services, name="services"), 
    path('web-development', views.WebDevelopment, name="web-development"), 
    path('mobile-app-development', views.AppDevelopment, name="mobile-app-development"), 
    path('ui-ux-design', views.UiUxDesign, name="ui-ux-design"), 
    path('digital-marketing', views.DigitalMarketing, name="digital-marketing"), 
    path('ott-campaigns', views.OttCampaigns, name="ott-campaigns"),
    path('portfollio', views.Portfollio, name="portfollio"),  
    path('contact', views.contact, name="contact"),
    
    
    # path('<data>', views.pagename),
    
    path('adminview/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls'))
   
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
