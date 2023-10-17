from django.urls import path
from restaurants import views

app_name = 'restaurants'
urlpatterns = [
    path('',views.restaurants, name='restaurants'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]