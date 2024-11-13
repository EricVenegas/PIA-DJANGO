from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    
    path('futuro/', views.futuro, name='futuro'),
    path('nutricional/', views.nutricional, name='nutricional'),
    path('sabores/', views.sabores, name='sabores'),
    path('contacto/', views.contacto, name='contacto'),
    path("todos/", views.todos, name="Todos")
    
    

    
]