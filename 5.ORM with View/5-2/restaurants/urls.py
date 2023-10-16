from django.urls import path
from restaurants import views

app_name = 'restaurants'
urlpatterns = [
    path('',views.restaurants, name='restaurants'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]