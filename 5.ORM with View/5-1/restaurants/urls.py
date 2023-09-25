from django.urls import path
from restaurants import views

app_name = 'restaurants'
urlpatterns = [
    path('',views.restaurants, name='restaurants'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]