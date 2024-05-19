from django.shortcuts import render, redirect
from .models import Palavras
from django.contrib import messages
from deep_translator import GoogleTranslator
import pyttsx3
from django.http import JsonResponse
import requests
import os
import pygame
import base64
# Create your views here.
def home(request):
    return render (request, 'home.html')

def palavras(request):
    resultado = request.session.get('resultado')
    palavras = Palavras.objects.all()[:12]
    return render(request, 'treinamento.html', {'palavras':palavras, 'resultado': resultado})



def verifica_resposta(request):
    palavra_user = request.POST.get('resposta_usuario')
    palavra_correta = request.POST.get('resposta_correta')
    id_palavra = request.POST.get('id_palavra')
    
    if palavra_user.lower() == palavra_correta.lower():
        request.session['resultado'] = {'id': id_palavra, 'correta': True}
        
        messages.success(request, 'Resposta correta!')

    else:
        request.session['resultado'] = {'id': id_palavra, 'correta': False}
       
        messages.error(request, 'Resposta incorreta!')

    return redirect('treinamento')





def get_pronunciation(text, language):
    """Obtém o áudio de pronúncia e o codifica em base64."""
    google_tts_url = "https://translate.google.com/translate_tts"
    params = {
        "ie": "UTF-8",
        "q": text,
        "tl": language,
        "client": "tw-ob",
    }

    response = requests.get(google_tts_url, params=params)
    if response.status_code == 200:
        audio_base64 = base64.b64encode(response.content).decode('utf-8')
        return audio_base64
    else:
        return None

def get_audio(request, id_palavra, language):
    if language == 'en':
        palavra = Palavras.objects.get(id=id_palavra).palavra_ingles.lower()
    elif language == 'pt':
        palavra = Palavras.objects.get(id=id_palavra).palavra_portugues.lower()
    elif language == 'ptt':
        palavra = Palavras.objects.get(id=id_palavra).palavra_pronuncia.lower()
        language = 'en'
    print(palavra,id_palavra, language)
    audio_base64 = get_pronunciation(palavra, language)
    return JsonResponse({'audio': audio_base64})

