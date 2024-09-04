"""
URL configuration for ecommerceproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from ecommerceapp import views as ec
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ec.index),
    path('items/', ec.listitems, name='listitems'),
    path('details/<int:id>', ec.details,name='details'),
    path('addtocart/',ec.add_to_cart,name='add_to_cart'),   #مشكلتي
    path('checkout/',ec.checkout,name='checkout'),
    path('auth_register/',ec.auth_register,name='auth_register'),
    path('auth_login/',ec.auth_login,name='auth_login'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

