from django.urls import path
from . import views

app_name = 'gpf'
urlpatterns = [
    path('', views.index, name='index'),
    path('actor/add', views.actorAddPopup, name='ActorAdd'),
    path('actor/change', views.actorChangePopup, name='ActorChange'),
    path('add/', views.permitRequestAdd, name='permit-request-add'),
    path('change/', views.permitRequestChange, name='permit-request-change'),
    path('listpermit/', views.listpermit, name='list-permit'),
    path('permitdetail/<int:pk>', views.permitdetail, name='permitdetail')
    ]
