from rest_framework import viewsets
from ..serializers.popup_serializer import PopUpSerializer,  PopUpDataSerializer
from ..models import PopUp,PopUpData
from rest_framework.permissions import IsAdminUser


class PopUpViewSet(viewsets.ModelViewSet):
    queryset= PopUp.objects.all().order_by('-id')
    serializer_class = PopUpSerializer
    # permission_classes= [IsAdminUser,]



class PopUpDataViewSet(viewsets.ModelViewSet):
    queryset = PopUpData.objects.all()
    serializer_class = PopUpDataSerializer
    # permission_classes= [IsAdminUser,]