
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('automobiliai/', views.automobiliai, name='automobiliai'),
    path('automobilis/<int:automobilis_id>', views.automobilis, name='automobilis'),
]