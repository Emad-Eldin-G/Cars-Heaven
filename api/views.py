from django.shortcuts import render
from .models import Car
from .serializers import CarSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView



# Create your views here.


class All_Cars(APIView):


	def get(self, request):
		Cars = Car.objects.all()
		serializer = CarSerializer(Cars, many=True)

		return Response(serializer.data)

#------------------------------------------------------------------------------#


class Specific_Cars(APIView):


	def get(self, request, pk):
		Cars = Car.objects.get(Car_ID=pk)
		serializer = CarSerializer(Cars, many=False)

		return Response(serializer.data)

#------------------------------------------------------------------------------#


class Brand(APIView):


	def get(self, request, brand):
		Cars = Car.objects.filter(Brand = brand)
		serializer = CarSerializer(Cars, many=True)

		return Response(serializer.data)




