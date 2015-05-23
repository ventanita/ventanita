from django.shortcuts import render


def index(request):
    return render(request, 'demo/index.html')


def candidatos_con_sentencias(request):
    return ''
