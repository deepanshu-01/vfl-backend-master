from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import VendorViewSerializer, VendorCreateSerializer, VendorListSerializer, VendorSpecificListSerializer
from .models import Vendor
from django.http import Http404
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class VendorView(generics.GenericAPIView):
    serializer_class = VendorViewSerializer  
    permission_classes= (permissions.AllowAny,)
    def get_object(self, pk):
        try:
            vendor = Vendor.objects.filter(pk=pk)
            print(vendor[0])
            return vendor[0]
        except:
            raise Http404

    def get(self, request, pk):
        vendor = self.get_object(pk)
        serializer = self.get_serializer(vendor)
        return Response(serializer.data,status=status.HTTP_200_OK)

   
    def put(self,request,pk):
        pass

    def patch(self, request, pk):
        vendor = self.get_object(pk)
        print(vendor.creator)
        print(self.request.user)
        if(vendor.creator == self.request.user):
            serializer = VendorViewSerializer(vendor, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status = status.HTTP_401_UNAUTHORIZED)

    def delete(self,request,pk):
        pass

class VendorCreateView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = VendorCreateSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

class VendorListView(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorListSerializer
    # filter_backends = [DjangoFilterBackend]
    def get_queryset(self):
        pincode = self.request.query_params.get('pincode')
        products= self.request.query_params.get('products')
        queryset = Vendor.objects.filter(pincode__iexact = pincode,products__icontains = products)
        return queryset

class VendorSpecificListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = VendorSpecificListSerializer

    def get(self, request):
        queryset = Vendor.objects.filter(creator=request.user)
        response = self.get_serializer(queryset, many=True)
        print(response.data)
        return Response(response.data, status.HTTP_200_OK)

