from django.urls import path
from . import views

app_name = 'gpf'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.actorAdd, name='actor_add'),
    path('actor/<int:pk>/change', views.actorChange, name='ActorChange'),
    path('add/<int:project_owner_id>/', views.permitRequestAdd, name='permit-request-add'),
    path('change/', views.permitRequestChange, name='permit-request-change'),
    path('list/', views.PermitRequestListView.as_view(), name='list'),
    path('listexport/', views.PermitExportView.as_view(), name='listexport'),
    path('permitdetail/<int:pk>', views.permitdetail, name='permitdetail')
    ]
