from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
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

@api_view(['GET'])
def food_list_view(request):
    try:
        food_list = Food.objects.all()
    except:
        return JsonResponse({"404": "no food"}, safe=False)
    serializer = FoodSerializer(food_list, many=True)
    return JsonResponse(serializer.data, safe=False)
        
class FoodsByCategory(APIView):
    def get(self, request, id):
        try:
            category = Category.objects.get(id=id)
            food_list = category.food_set.all()
        except:
            return JsonResponse({"404": "no food"}, safe=False)
        serializer = FoodSerializer(food_list, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def food_detailed_view(request, id):
    try:
        food_detailed = Food.objects.get(id=id)
    except:
        return JsonResponse({"404": "no food"}, safe=False)
    serializer = FoodSerializer(food_detailed)
    return JsonResponse(serializer.data, safe=False)
        
