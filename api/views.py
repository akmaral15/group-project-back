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

@api_view(['GET', 'POST'])
def food_list_view(request):
    if request.method == 'GET':
        try:
            food_list = Food.objects.all()
        except:
            return JsonResponse({"404": "no food"}, safe=False)
        serializer = FoodSerializer(food_list, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        try:
            category = Category.objects.get(name = request.data.get('category'))
        except:
            category = Category.objects.create(name = request.data.get('category'))
        
        try:
            food = Food.objects.create(
                name = request.data.get('name'),
                category = category,
                price = request.data.get('price'),
                description = request.data.get('name'),
                ingredients = request.data.get('name'),
                images = request.data.get('image')
            )
        except:
            return JsonResponse({"500": "cant create food"}, safe=False)

        return JsonResponse(FoodSerializer(food).data, safe=False)
        
class FoodsByCategory(APIView):
    def get(self, request, id):
        try:
            category = Category.objects.get(id=id)
            food_list = category.food_set.all()
        except:
            return JsonResponse({"404": "no food"}, safe=False)
        serializer = FoodSerializer(food_list, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def food_detailed_view(request, id):
    if request.method == 'GET':
        try:
            food_detailed = Food.objects.get(id=id)
        except:
            return JsonResponse({"404": "no food"}, safe=False)
        serializer = FoodSerializer(food_detailed)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        try:
            food_detailed = Food.objects.get(id=id)
        except:
            return JsonResponse({"404": "no food"}, safe=False)
        food_detailed.name = request.data.get('name')
        food_detailed.price = request.data.get('price')
        food_detailed.description = request.data.get('description')
        food_detailed.ingredients = request.data.get('ingredients')
        food_detailed.save()
        serializer = FoodSerializer(food_detailed)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'DELETE':
        try:
            food_detailed = Food.objects.get(id=id)
        except:
            return JsonResponse({"404": "no food"}, safe=False)
        food_detailed.delete()
        return JsonResponse({"204": "deleted food"}, safe=False)
        

@api_view(['POST'])
def food_create_admin(request):
    try:
        category = Category.objects.get(name = request.data.get('category'))
    except:
        category = Category.objects.create(name = request.data.get('category'))
    
    try:
        food = Food.objects.create(
            name = request.data.get('name'),
            category = category,
            price = request.data.get('price'),
            description = request.data.get('name'),
            ingredients = request.data.get('name'),
            images = request.data.get('image')
        )
    except:
        return JsonResponse({"500": "cant create food"}, safe=False)

    return JsonResponse(FoodSerializer(food).data, safe=False)