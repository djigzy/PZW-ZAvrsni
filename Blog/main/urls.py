from django.urls import path
from . import views
from main.views import *

app_name='main'

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', KorisnikList.as_view(), name='users'),
    path('reputations/', ReputacijaList.as_view(), name='reputations'),
    path('blogs/', BlogList.as_view(), name='blogs'),
    path('comments/', KomentarList.as_view(), name='comments'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('formaNoviKorisnik/', views.noviKorisnik, name='formaNoviKorisnik'),
    path('formaNovaReputacija/', views.novaReputacija, name='formaNovaReputacija'),
    path('formaNoviKomentar/', views.noviKomentar, name='formaNoviKomentar'),
    path('formaNoviBlog/', views.noviBlog, name='formaNoviBlog')
]
