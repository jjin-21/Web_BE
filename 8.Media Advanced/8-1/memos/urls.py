<<<<<<< HEAD

from django.urls import path
from . import views

app_name="memos"
urlpatterns = [
    path('',views.index,name="index"),
    path('create/',views.create,name='create'),
    path('<int:pk>/',views.detail,name='detail'),
    path('<int:pk>/delete',views.delete,name='delete'),
    path('<int:pk>/update',views.update,name='update'),

]
=======

from django.urls import path
from . import views

app_name="memos"
urlpatterns = [
    path('',views.index,name="index"),
    path('create/',views.create,name='create'),
    path('<int:pk>/',views.detail,name='detail'),
    path('<int:pk>/delete',views.delete,name='delete'),
    path('<int:pk>/update',views.update,name='update'),

]
>>>>>>> 839d8730f0ca103e47c95ab8477c42cb69f4f5e6
