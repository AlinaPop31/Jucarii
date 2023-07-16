from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from . models import  Jucarie
from . serializers import JucarieSerializer



class JucarieViewSet(ModelViewSet):
 queryset = Jucarie.objects.all()
 serializer_class = JucarieSerializer
 permission_classes = [permissions.AllowAny]





