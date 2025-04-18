from django.shortcuts import render
from .models import Produto
import uuid
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

def index(request):
    
    produtos=Produto.objects.all()
    
    context = {
        'curso': 'Programação Web com Django Framework',
        'outraVar': 'Testando!!!!',
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def produto(request, id):
    # prod=Produto.objects.get(id=id)    
    # context = {        
    #     'produto': prod
    # }
    # return render(request, 'produto.html', context)
    
    prod = get_object_or_404(Produto, id=id)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)


def contato(request):
    return render(request, 'contato.html')

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404) 

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500) 

