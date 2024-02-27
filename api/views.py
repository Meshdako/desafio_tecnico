from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializer import *
from .models import *
from .forms import *

# Create your views here.
class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

def Inicio(request):
    reglas = Rules.objects.all()
    word_form = WordForm()
    
    # Envío de la palabra.
    if request.method == "POST":
        word_form = WordForm(request.POST)
        
        ids = []
        
        if word_form.is_valid():
            # Se captan las palabras.
            in_word = word_form.cleaned_data['input_word']
            
            words = in_word.split(", ")
            print (len(words))
            
            nuevasReglas, nuevasPalabras = pluralizador(words)
            
            print (nuevasReglas)
            print (nuevasPalabras)
            
            uno, dos, tres, cuatro = nuevasReglas
            
            rule = Rules.objects.create(
                rule_1 = uno,
                rule_2 = dos,
                rule_3 = tres,
                rule_4 = cuatro,
            )
            
            count = len(words)
            
            for i in range(count):
                word = Word.objects.create(
                    input_word = words[i],
                    output_word = nuevasPalabras[i],
                )
                ids.append(word.pk)
        print (ids)
        return Resultado(request, id = rule.pk, ini = ids[0], fin = ids[len(ids) - 1])
    
    return render(request=request, template_name="index.html", context={'reglas': reglas, 'word_form': word_form})

def Resultado(request, id, ini, fin):
    regla = Rules.objects.get(id = id)
    
    words = []
    i = ini
    while i < fin + 1:
        words.append(Word.objects.get(id = i))
        i += 1

    return render(request=request, template_name="result.html", context={'regla': regla, 'words': words})

def SingularToPlural(palabra):
    palabra = palabra.lower()
    vocales = ["a", "e", "i", "o", "u"]
    ultima = palabra[len(palabra) - 1]
    # CASO 1
    for vocal in vocales:
        if ultima == vocal:
            return (1, palabra + "s")
    # CASO 2
    if ultima == "x" or ultima == "s":
        return (2, palabra)
    # CASO 3
    if ultima == "z":
        palabra = palabra.replace("z", "ces")
        return (3, palabra)
    # CASO 4
    else:
        return (4, palabra + "es")

def pluralizador(lasPalabras):
    cantidadesPorRegla = [0, 0, 0, 0]
    nuevasPalabras = []
    
    # Recorremos las Palbras ingresadas
    for laPalabra in lasPalabras:
        regla, nuevaPalabra = SingularToPlural(laPalabra)
        nuevasPalabras.append(nuevaPalabra)
        cantidadesPorRegla[regla - 1] += 1
    
    return cantidadesPorRegla, nuevasPalabras