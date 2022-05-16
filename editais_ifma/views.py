from django.shortcuts import render, redirect
from json import load
from .models import Menssagens, FormMenssage, Edital


def index(request):
    form = FormMenssage()

    if request.method != 'POST':
        with open('edital.json', 'r', encoding='utf8') as file:
            dados = load(file)
        
        for titulos in dados:
            if not Edital.objects.filter(edital=titulos['titulo']).exists():
                ed = Edital(edital=titulos['titulo'])
                ed.save()
        
        message_object = Menssagens.objects.order_by('-id')
        return render(request, 'index.html', {
            'dados': dados,
            'menssagens': message_object,
            'form': form
        })

    form = FormMenssage(request.POST)
    if form.is_valid:
        form.save()
        return redirect('index')

