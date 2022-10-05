from django.shortcuts import render
from django.views.generic import View
from vigenere.cifra_vigenere import vigenere_cipher
# Create your views here.

class HomeIndex(View):
    def get(self, request):
        return render(request, 'home.html')

def encode(request):
    infor = request.POST['text']
    key = request.POST['key']
    _modo = request.POST['modo']
    
    if _modo == 'Criptografar':
        text = vigenere_cipher(infor,key,True)
        modo = True 
    elif _modo == 'Descriptografar':
        text = vigenere_cipher(infor,key,False)
        modo = False

    return render(request, 'home.html', {'text':text, 'infor':infor,'key':key, 'modo':modo})
