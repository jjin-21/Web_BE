<<<<<<< HEAD
from django.urls import path
from . import views

app_name='chattings'
urlpatterns = [
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('<int:pk>/update',views.update,name="update"),
    path('<int:pk>/',views.detail,name='detail'),
    path('create/', views.create, name='create'),
    path('',views.index,name='index'),
=======
from django.urls import path
from . import views

app_name='chattings'
urlpatterns = [
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('<int:pk>/update',views.update,name="update"),
    path('<int:pk>/',views.detail,name='detail'),
    path('create/', views.create, name='create'),
    path('',views.index,name='index'),
>>>>>>> 839d8730f0ca103e47c95ab8477c42cb69f4f5e6
]