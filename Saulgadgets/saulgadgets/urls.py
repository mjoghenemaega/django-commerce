from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views
from django.contrib.auth import views as auth_views

from apps.cart.views import cart_detail, success,checkout
from apps.core.views import frontpage, contact, about,all_products,allcategories,autosuggest,custom_page_not_found_view,custom_error_view,custom_bad_request_view,custom_permission_denied_view
from apps.order.views import admin_order_pdf
from apps.store.views import product_detail, category_detail, search
from apps.userprofile.views import signup, myaccount, password_reset_request

from apps.newsletter.api import api_add_subscriber
from apps.coupon.api import api_can_use
from apps.store.api import api_add_to_cart, api_remove_from_cart,api_checkout

from .sitemaps import StaticViewSitemap, CategorySitemap, ProductSitemap

handler404 = 'apps.core.views.custom_page_not_found_view'
handler500 = 'apps.core.views.custom_error_view'
handler403 = 'apps.core.views.custom_permission_denied_view'
handler400 = 'apps.core.views.custom_bad_request_view'


# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']


sitemaps = {'static': StaticViewSitemap, 'product': ProductSitemap, 'category': CategorySitemap}
app_name ='store'
app_name ='userprofile'
urlpatterns = [
    path('', frontpage, name='frontpage'),
     
    path('all_products/', all_products, name='all_products'),
    path('search/', search, name='search'),
    path('cart/', cart_detail, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('cart/success/', success, name='success'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('autosuggest/',autosuggest , name='autosuggest'),
    path('allcategories/', allcategories, name='allcategories'),
    path('admin/', admin.site.urls),
    path('admin/admin_order_pdf/<int:order_id>/', admin_order_pdf, name='admin_order_pdf'),
    
    path("password_reset/", password_reset_request, name="password_reset"),


    # Auth

    path('myaccount/', myaccount, name='myaccount'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    

    
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),      
    # API

    path('api/can_use/', api_can_use, name='api_can_use'),
    path('api/checkout/',  api_checkout, name=' api_checkout'),
   
    path('api/add_to_cart/', api_add_to_cart, name='api_add_to_cart'),
    path('api/remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),
    path('api/add_subscriber/', api_add_subscriber, name='api_add_subscriber'),

    # Store

    path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
    path('<slug:slug>/', category_detail, name='category_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
