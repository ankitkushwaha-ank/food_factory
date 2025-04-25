from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from food_factory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='home'),
    path('home/', views.index_page, name='home_redirect'),
    path('menu/', views.menu_page, name='menu'),
    path('menu_detail/<slug>/', views.menu_detail, name='menu_detail'),
    path('promotions/', views.promotion_page, name='promotions'),
    path('contact/', views.contact_page, name='contact'),
    path('karaoke/', views.karaoke_page, name='karaoke'),
    path('form/', views.form_page, name='form'),
    path('cart/<item_id>', views.addtocart,name='add-to-cart'),
]

# Serving static files during development (only for DEBUG mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
