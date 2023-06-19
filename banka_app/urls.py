from django.urls import path
from . import views

urlpatterns = [
    path('uzivatele/', views.uzivatele, name='uzivatele'),
    path('uzivatele/<int:uzivatel_id>/', views.detail_uzivatele, name='detail-uzivatele'),
    path('pridat-uzivatele/', views.add_user, name='pridat-uzivatele'),
    path('podminky/', views.podminky, name='podminky'),
    path('', views.banka_aplikace, name='banka_aplikace'),
]