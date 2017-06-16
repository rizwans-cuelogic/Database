# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from snippets.models import Product
from snippets.serializers import ProductSerializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
	return render(request,"snippets/home.html")

class productlist(APIView):
	def get(self,request):
		products=Product.objects.all()
		serialized = ProductSerializers(products,many=True)
		return Response(serialized.data,status.HTTP_200_OK)
	@csrf_exempt
	def post(self,request):
		serialized=ProductSerializers(data=request.data)
		if serialized.is_valid():
			serialized.save()
			return Response(serialized.data,status=status.HTTP_201_CREATED)
		else:
			return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)


class productdetail(APIView):
	def get_objects(self,pk):
		try:
			return Product.objects.get(pk=pk)
		except product.DoesNotExist:
			raise Http404	

	def get(self,request,pk):
		try:
			products=Product.objects.get(pk=pk)
			serialized=ProductSerializers(products)
			return Response(serialized.data)
		except Stock.DoesNotExist:
			raise Http404
	@csrf_exempt
	def patch(self, request, pk):
		product = self.get_objects(pk)
		serializer = ProductSerializers(product, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def review_submit(request):
	if request.method == 'POST':
		data = json.loads(request.body)


def add_product(request):
	return render(request,"snippets/addproduct.html")