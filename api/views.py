from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
from api.models import Category, Food
from api.serializers import CategorySerializer, FoodSerializer
class CategoriesListView(APIView):
    def get(self, request):
        try:
            category_list = Category.objects.all()
        except:
            return JsonResponse({"404": "no categories"}, safe=False)
        serializer = CategorySerializer(category_list, many=True)
        return JsonResponse(serializer.data, safe=False)
