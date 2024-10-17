"""
URL configuration for base project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from bas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('busPark_list/', views.BusParkList.as_view(), name='park_list'),
    path('busPark/<int:pk>/', views.BusParkDetail.as_view(), name='park_detail'),
    path('busPark/<int:pk>/update/', views.BusParkUpdate.as_view(), name='park_update'),
    path('busPark/<int:pk>/delete/', views.BusParkDelete.as_view(), name='park_delete'),
    path('busPark/create/', views.BusParkCreate.as_view(), name='park_create'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
