from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('gpf/', include('gpf.urls')),
    path('admin/', admin.site.urls),
    path('accounts/profile/', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
]
