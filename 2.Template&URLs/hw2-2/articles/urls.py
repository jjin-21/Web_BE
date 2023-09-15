from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('catch/', views.catch, name='catch'),
    path('introduce/<str:name>/<int:age>/', views.introduce, name='introduce'),
]
