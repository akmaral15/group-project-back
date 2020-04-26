from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from api import views
urlpatterns = [
    path('categories/', views.CategoriesListView.as_view()),
    path('foods/', views.food_list_view),
    path('foods/category/<int:id>/', views.FoodsByCategory.as_view()),
    path('foods/<int:id>/', views.food_detailed_view),
    path('login/', obtain_jwt_token)
    
]