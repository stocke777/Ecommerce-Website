
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name = "home"),
    path('list/<int:pk>/', views.productlist, name='list'),
    path('product_details/<int:pk>/', views.product_details, name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
