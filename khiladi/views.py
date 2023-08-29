from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render
from post_management.models import category
from post_management.models import sub_category
from post_management.models import post
from Ad_management.models import ad_category
from Ad_management.models import ad
from service.models import videopost

def home(request):
    blogdata=post.objects.all().order_by('-id')
    
    adtopid=ad_category.objects.get(ads_cat_slug='leaderboard')
    adtop=ad.objects.get(ads_cat_id=adtopid.id, is_active=1)
    
    adleftid=ad_category.objects.get(ads_cat_slug='skyscraper')
    adleft=ad.objects.get(ads_cat_id=adleftid.id, is_active=1)
    
    adrightid=ad_category.objects.get(ads_cat_slug='mrec')
    adright=ad.objects.get(ads_cat_id=adrightid.id, is_active=1)
    # slider=post.objects.filter(id=1).order_by('id')[:5] use for filter value
    Category=category.objects.all()
    slider=post.objects.filter().order_by('-id')[:5]
    latestnews=post.objects.all().order_by('-id')[:5]
    data={
            'BlogData':blogdata,
            'Slider':slider,
            'Blogcat':Category,
            'latnews':latestnews,
            'adtop':adtop,
            'adleft':adleft,
            'adright':adright,
        }
   
    return render(request,'index.html',data)
    #return render(request, 'index.html')
def newsdetails(request,catlink,slug):
    blogdetails=post.objects.get(slug=slug)
    blogdata=post.objects.all().order_by('-id')
    Category=category.objects.all()
    latestnews=post.objects.all().order_by('-id')[:5]
    
    adtopid=ad_category.objects.get(ads_cat_slug='leaderboard')
    adtop=ad.objects.get(ads_cat_id=adtopid.id, is_active=1)
    
    adleftid=ad_category.objects.get(ads_cat_slug='skyscraper')
    adleft=ad.objects.get(ads_cat_id=adleftid.id, is_active=1)
    
    adrightid=ad_category.objects.get(ads_cat_slug='mrec')
    adright=ad.objects.get(ads_cat_id=adrightid.id, is_active=1)
    data={
            'blogdetails':blogdetails,
            'latestnews':blogdata,
            'Blogcat':Category,
            'latnews':latestnews,
            'adtop':adtop,
            'adleft':adleft,
            'adright':adright,
        }

    return render(request,'newsdetails.html',data)


def Category(request,slug):
    cat=category.objects.get(cat_slug=slug)
    blogdata=post.objects.filter(post_cat=cat.id).order_by('-id')
    
    Category=category.objects.all()
    slider=post.objects.filter(post_cat=cat.id).order_by('-id')[:5]
    latestnews=post.objects.all().order_by('-id')[:5]
    
    adtopid=ad_category.objects.get(ads_cat_slug='leaderboard')
    adtop=ad.objects.get(ads_cat_id=adtopid.id, is_active=1)
    
    adleftid=ad_category.objects.get(ads_cat_slug='skyscraper')
    adleft=ad.objects.get(ads_cat_id=adleftid.id, is_active=1)
    
    adrightid=ad_category.objects.get(ads_cat_slug='mrec')
    adright=ad.objects.get(ads_cat_id=adrightid.id, is_active=1)
    
    data={
            'BlogData':blogdata,
            'Slider':slider,
            'Blogcat':Category,
            'latnews':latestnews,
             'adtop':adtop,
            'adleft':adleft,
            'adright':adright,
        }

    return render(request,'category.html',data)
        

def videocategory(request,slug):
    viddata=videopost.objects.filter(videotype=slug).order_by('-id')
    
    Category=category.objects.all()
    latestnews=post.objects.all().order_by('-id')[:5]
    
    adtopid=ad_category.objects.get(ads_cat_slug='leaderboard')
    adtop=ad.objects.get(ads_cat_id=adtopid.id, is_active=1)
    
    adleftid=ad_category.objects.get(ads_cat_slug='skyscraper')
    adleft=ad.objects.get(ads_cat_id=adleftid.id, is_active=1)
    
    adrightid=ad_category.objects.get(ads_cat_slug='mrec')
    adright=ad.objects.get(ads_cat_id=adrightid.id, is_active=1)
    
    data={
            'vidpost':viddata,
            'Blogcat':Category,
            'latnews':latestnews,
             'adtop':adtop,
            'adleft':adleft,
            'adright':adright,
        }

    return render(request,'videocategory.html',data)

def aboutUs(request):
    Category=category.objects.all()
    latestnews=post.objects.all().order_by('-id')[:5]
    
    adtopid=ad_category.objects.get(ads_cat_slug='leaderboard')
    adtop=ad.objects.get(ads_cat_id=adtopid.id, is_active=1)
    
    adleftid=ad_category.objects.get(ads_cat_slug='skyscraper')
    adleft=ad.objects.get(ads_cat_id=adleftid.id, is_active=1)
    
    adrightid=ad_category.objects.get(ads_cat_slug='mrec')
    adright=ad.objects.get(ads_cat_id=adrightid.id, is_active=1)
    
    data={
            'Blogcat':Category,
            'latnews':latestnews,
            'adtop':adtop,
            'adleft':adleft,
            'adright':adright,
        }
    return render(request, 'aboutus.html',data)

def login(request):
    Category=category.objects.all()
    latestnews=post.objects.all().order_by('-id')[:5]
    
    adtopid=ad_category.objects.get(ads_cat_slug='leaderboard')
    adtop=ad.objects.get(ads_cat_id=adtopid.id, is_active=1)
    
    adleftid=ad_category.objects.get(ads_cat_slug='skyscraper')
    adleft=ad.objects.get(ads_cat_id=adleftid.id, is_active=1)
    
    adrightid=ad_category.objects.get(ads_cat_slug='mrec')
    adright=ad.objects.get(ads_cat_id=adrightid.id, is_active=1)
    
    data={
            'Blogcat':Category,
            'latnews':latestnews,
            'adtop':adtop,
            'adleft':adleft,
            'adright':adright,
        }
    return render(request, 'login.html',data)




def Services(request):
    return render(request, 'services.html')

def WebDevelopment(request):
    return render(request, 'web-development.html')

def AppDevelopment(request):
    return render(request, 'mobile-app-development.html')

def UiUxDesign(request):
    return render(request, 'ui-ux-design.html')

def DigitalMarketing(request):
    return render(request, 'digital-marketing.html')

def OttCampaigns(request):
    return render(request, 'ott-campaigns.html')

def Portfollio(request):
    return render(request, 'portfollio.html')
def contact(request):
    return render(request, 'contact.html')




    
# def pagename(request, data):
#     return HttpResponse(data)
   





    #def aboutUs(request):
    #    return HttpResponse('welcome about us')
