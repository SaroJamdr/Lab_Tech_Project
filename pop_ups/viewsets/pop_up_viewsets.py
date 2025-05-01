from rest_framework import viewsets
from ..serializers.popup_serializer import PopUpSerializer,  PopUpDataSerializer
from ..models import PopUp,PopUpData

class PopUpViewSet(viewsets.ModelViewSet):
    queryset= PopUp.objects.all().order_by('-id')
    serializer_class = PopUpSerializer

class PopUpDataViewSet(viewsets.ModelViewSet):
    queryset = PopUpData.objects.all()
    serializer_class = PopUpDataSerializer