from django.urls import path
from api import views
urlpatterns = [
    path('categories/', views.CategoriesListView.as_view()),
    path('foods/', views.food_list_view),
    path('foods/category/<int:id>/', views.FoodsByCategory.as_view()),
    path('foods/<int:id>/', views.food_detailed_view),
    
]