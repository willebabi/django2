from django.shortcuts import render, redirect
from .models import Transacao
from .forms import transForm
from django.http import HttpResponse
import datetime

def home(request):
    data = {}
    data['trans'] = ['t1', 't2', 't3']
    data['now'] = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacao'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)    

def novatransacao (request):
    form = transForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listagem')
    data = {}
    data['form'] = form
    return render(request, 'contas/form.html', data)

def update (request, pk):
    trans = Transacao.objects.get(pk=pk)
    form = transForm(request.POST or None, instance=trans)
    if form.is_valid():
        form.save()
        return redirect('listagem')
    data = {}
    data['form'] = form
    data['trans'] = trans
    return render(request, 'contas/form.html', data)

def delete (request, pk):
    trans = Transacao.objects.get(pk=pk)
    trans.delete()
    return redirect('listagem')
