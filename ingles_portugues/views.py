from django.shortcuts import render, redirect
from .models import Palavras
from django.contrib import messages

# Create your views here.
def home(request):
    return render (request, 'home.html')

def palavras(request):
    resultado = request.session.get('resultado')
    palavras = Palavras.objects.all()[:12]
    return render(request, 'palavras.html', {'palavras':palavras, 'resultado': resultado})


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

    return redirect('palavras')  

def ouvir_audio_portugues(request):
    print('oi')