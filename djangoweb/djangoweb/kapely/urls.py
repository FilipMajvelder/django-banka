from django.urls import path
from . import views

urlpatterns = [
    path('vypis/', views.vypis, name='vypis'),
    path('kapela/<int:kapela_id>/', views.detail_kapela, name='detail-kapela'),
]
