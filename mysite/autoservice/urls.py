
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('automobiliai/', views.automobiliai, name='automobiliai'),
    path('automobiliai/<int:automobilis_id>', views.automobilis, name='automobilis'),
    path('uzsakymai/', views.Uzsakymai.as_view(), name='uzsakymai'),
    path('uzsakymai/<int:pk>', views.Uzsakymas.as_view(), name="uzsakymas"),
]