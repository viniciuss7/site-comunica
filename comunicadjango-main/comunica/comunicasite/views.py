from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Comentario
from .forms import ComentarioForm
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comentarios')
    else:
        form = ComentarioForm()

    comentarios = Comentario.objects.all()

    context = {
        'form': form,
        'comentarios': comentarios
    }

    return render(request, './site/index.html', context)


def comentarios(request):
    comentarios_aprovados = Comentario.objects.filter(aprovado=True)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.status = 'pendente'
            comentario.save()

            messages.success(request, 'Comentário enviado com sucesso! Aguardando aprovação.')

            return redirect('comentarios')

    else:
        form = ComentarioForm()

    context = {
        'form': form,
        'comentarios': comentarios_aprovados
    }

    return render(request, 'site/index.html', context)
