from django.urls import path
from . import views


from django.urls import path
from rest_framework import routers
from api import views
router = routers.SimpleRouter()
router.register(r'api/jucarie', views.JucarieViewSet)
urlpatterns = [
 # path('', views.jucarie_list, name='jucarie_list'),
]
urlpatterns += router.urls


