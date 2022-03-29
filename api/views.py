from django.shortcuts import render
from .models import Model
from .serializers import ModelSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView



# Create your views here.


class All_Cars(APIView):


	def get(self, request):
		Cars = Model.objects.all()
		serializer = ModelSerializer(Cars, many=True)

		return Response(serializer.data)

#------------------------------------------------------------------------------#


class Specific_Car(APIView):


	def get(self, request, name):
		Cars = Model.objects.get(Name=name)
		serializer = ModelSerializer(Cars, many=False)

		return Response(serializer.data)

#------------------------------------------------------------------------------#


class Brand(APIView):


	def get(self, request, brand):
		Cars = Model.objects.filter(Brand=brand)
		serializer = ModelSerializer(Cars, many=True)

		return Response(serializer.data)

#------------------------------------------------------------------------------#


class Top_Speed(APIView):


	def get(self, request):
		Cars = Model.objects.order_by('-Top_Speed')
		serializer = ModelSerializer(Cars, many=True)

		return Response(serializer.data)




