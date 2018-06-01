from django.urls import path
from . import views
from gpf.views import PermitListView

app_name = 'gpf'
urlpatterns = [
    path('', views.index, name='index'),
    path('actor/add', views.actorAddPopup, name='ActorAdd'),
    path('actor/change', views.actorChangePopup, name='ActorChange'),
    path('add/', views.permitRequestAdd, name='permit-request-add'),
    path('change/', views.permitRequestChange, name='permit-request-change'),
    path('listpermit/', PermitListView.as_view(), name='permit-list'),
    ]
