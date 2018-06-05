from django.urls import path
from . import views

app_name = 'gpf'
urlpatterns = [
    path('', views.index, name='index'),
    path('actor/add', views.actorAddPopup, name='actor_add'),
    path('actor/<int:pk>/change', views.actorChangePopup, name='ActorChange'),
    path('actor/ajax/get_actor_id', views.get_actor_id, name='get_actor_id'),
    path('add/', views.permitRequestAdd, name='permit-request-add'),
    path('change/', views.permitRequestChange, name='permit-request-change'),
    path('listpermit/', views.listpermit, name='list-permit'),
    path('permitdetail/<int:pk>', views.permitdetail, name='permitdetail')
    ]
