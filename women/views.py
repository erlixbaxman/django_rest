from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .models import Women
from .serializers import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet): #mixins from rest
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

