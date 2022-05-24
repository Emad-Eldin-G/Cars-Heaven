from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Brand, Model, blog
from .serializers import BlogSerializer, BrandSerializer, ModelSerializer

# Create your views here.

#General Car information
class All_Cars(APIView):

	queryset = Model.objects.all()

	def get(self, request, *args, **kwargs):
		Cars = Model.objects.all()
		serializer = ModelSerializer(Cars, many=True)

		return Response(serializer.data)

class Specific_Car(APIView):

	queryset = Model.objects.all()

	def get(self, request, name, *args, **kwargs):
		Cars = Model.objects.get(Name=name)
		serializer = ModelSerializer(Cars, many=False)
		view = True

		return Response(serializer.data)
		
class Car_Brand(APIView):


	def get(self, request, brand, *args, **kwargs):
		Cars = Model.objects.filter(Brand=brand)
		serializer = ModelSerializer(Cars, many=True)

		return Response(serializer.data)

class All_brands(APIView):

	def get(self, request, *args, **kwargs):
		Brands = Brand.objects.all().order_by('Name')
		serializer = BrandSerializer(Brands, many=True)

		return Response(serializer.data)


#------------------------------------------------------------------------------#

#Car Speed
class Top_Speed(APIView):


	def get(self, request, *args, **kwargs):
		Cars = Model.objects.order_by('-Top_Speed')
		serializer = ModelSerializer(Cars, many=True)

		return Response(serializer.data)

class Low_Speed(APIView):


	def get(self, request, *args, **kwargs):
		Cars = Model.objects.order_by('Top_Speed')
		serializer = ModelSerializer(Cars, many=True)

		return Response(serializer.data)


#------------------------------------------------------------------------------#

#Car Type
class Type_Sedan(APIView):


	def get(self, request, *args, **kwargs):
		Cars = Model.objects.filter(Type='Sedan')
		serializer = ModelSerializer(Cars, many=True)

		return Response(serializer.data)

class Type_SUV(APIView):


	def get(self, request, *args, **kwargs):
		Cars = Model.objects.f(Type='SUV')
		serializer = ModelSerializer(Cars, many=True)

		return Response(serializer.data)

class Type_Sport(APIView):


	def get(self, request, *args, **kwargs):
		Cars = Model.objects.filter(Type='Sport')
		serializer = ModelSerializer(Cars, many=True)

		return Response(serializer.data)

class Type_Hatchback(APIView):


	def get(self, request, *args, **kwargs):
		Cars = Model.objects.filter(Type='Hatchback')
		serializer = ModelSerializer(Cars, many=True)

		return Response(serializer.data)
#------------------------------------------------------------------------------#

#Car Power/Fuel
class Power_Gas(APIView):


	def get(self, request, *args, **kwargs):
		Cars = Model.objects.filter(Power='Gas')
		serializer = ModelSerializer(Cars, many=True)

		return Response(serializer.data)

class Power_Electric(APIView):


	def get(self, request, *args, **kwargs):
		Cars = Model.objects.filter(Power='Electric')
		serializer = ModelSerializer(Cars, many=True)

		return Response(serializer.data)

class Power_Hybrid(APIView):


	def get(self, request, *args, **kwargs):
		Cars = Model.objects.filter(Power='Hybrid')
		serializer = ModelSerializer(Cars, many=True)

		return Response(serializer.data)

class Power_Hydrogen(APIView):


	def get(self, request, *args, **kwargs):
		Cars = Model.objects.filter(Power='Hydrogen')
		serializer = ModelSerializer(Cars, many=True)

		return Response(serializer.data)
#------------------------------------------------------------------------------#

#Car year of make
class Year_of_make(APIView):


	def get(self, request, year, *args, **kwargs):
		Cars = Model.objects.filter(Year=year)
		serializer = ModelSerializer(Cars, many=True)

		return Response(serializer.data)

class Sort_Newest(APIView):


	def get(self, request, *args, **kwargs):
		Cars = Model.objects.order_by('-Year')
		serializer = ModelSerializer(Cars, many=True)

		return Response(serializer.data)

class Sort_Oldest(APIView):


	def get(self, request, *args, **kwargs):
		Cars = Model.objects.order_by('Year')
		serializer = ModelSerializer(Cars, many=True)

		return Response(serializer.data)


#------------------------------------------------------------------------------#
#The BLOG

class All_blogs(APIView):


	def get(self, request, *args, **kwargs):
		Blogs = blog.objects.all()
		serializer = BlogSerializer(Blogs, many=True)

		return Response(serializer.data)

