from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('palavras/' , views.palavras, name='treinamento'),
    path('verifica_resposta/', views.verifica_resposta, name='verifica_resposta'),
    path('get_audio/<int:id_palavra>/<str:language>', views.get_audio, name='falando'),
]
