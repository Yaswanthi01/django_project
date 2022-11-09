from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from .models import Asset1
from myapp.serializers import AssetSerializer
from myapp.models import Asset1

class AssetViewSet(APIView):

    def post(self, request):
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
	
    def get(self, request, id=None):
        if id:
            item = Asset1.objects.get(id=id)
            serializer = AssetSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Asset1.objects.all()
        serializer = AssetSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    
    def patch(self, request, id=None):
        item = Asset1.objects.get(id=id)
        serializer = AssetSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
            


# 
#    queryset = Asset.objects.all()
#    serializer_class = AssetSerializer




# Create your views here.
