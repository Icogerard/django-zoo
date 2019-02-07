from django.urls import path
from . import views

app_name = 'zoo'

urlpatterns = [
    path('', views.animal_list, name='animal_list'),
    path('<slug:category_slug>/', views.animal_list, name='animal_list_by_category'),
    path('<int:id>/<slug:slug>/', views.animal_detail,name='animal_detail'),
]
