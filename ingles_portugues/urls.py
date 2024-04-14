from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('palavras/' , views.palavras, name='palavras'),
    path('verifica_resposta/', views.verifica_resposta, name='verifica_resposta')
]
