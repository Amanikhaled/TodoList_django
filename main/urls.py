from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('detailed/<str:id>', views.detailed, name='detailed'),
    path('update/<str:id>', views.updateTodo, name='update'),
    path('delete/<str:id>', views.delete, name='delete'),


    path('create/', views.createTodo, name='create'),

]
