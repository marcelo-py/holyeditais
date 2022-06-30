from django.shortcuts import render, redirect
from json import load
from .models import Menssagens, FormMenssage, Edital
import subprocess
from subprocess import PIPE
import datetime

hora = datetime.datetime.today().hour
def index(request):
    form = FormMenssage()
    print(hora)
    if hora in (7, 8, 23, 0, 1, 2):
        subprocess.run('scrapy runspider editais.py -O edital.json', stderr=PIPE, stdout=PIPE)

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

