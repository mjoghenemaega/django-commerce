from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator ,EmptyPage
from apps.store.models import Product, Category
from django.db import models

def frontpage(request):
    products = Product.objects.filter(is_featured=True)
    flashsale = Product.objects.filter(flashsale=True)
    top_picks = Product.objects.filter(top_picks=True)
    New_arrival = Product.objects.filter(New_arrival=True)
    discount = Product.objects.filter(discount=True)
    featured_categories = Category.objects.filter(is_featured=True)
    popular_products = Product.objects.all().order_by('-num_visits')[0:4]
    recently_viewed_products = Product.objects.all().order_by('-last_visit')[0:4]
    

    context = {
        'products': products,
        'flashsale': flashsale,
        'top_picks': top_picks,
        'discount': discount,
        'New_arrival': New_arrival,
        'featured_categories': featured_categories,
        'popular_products': popular_products,
        'recently_viewed_products': recently_viewed_products

    
    }

    return render(request, 'frontpage.html', context)



def all_products(request):
    all_products = Product.objects.all()
    p=Paginator(all_products, 12)
    
    page_num = request.GET.get('page',1)

    try:
        page =p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    
    context = {
        'all_products': page,
    }

    return render(request, 'all_products.html', context)




def contact(request):
    return render(request, 'contact.html')

def allcategories(request):
    return render(request, 'allcategories.html')


def about(request):
    return render(request, 'about.html')


def autosuggest(request):
    print(request.GET) 
    query_original =request.GET.get('term')
    queryset =Product.objects.filter(title__icontains=query_original)
    mylist=[]
    mylist += [x.title for x in queryset]
    return JsonResponse(mylist, safe=False)   


def custom_page_not_found_view(request, exception):
    return render(request, "404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "404.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "404.html", {})    