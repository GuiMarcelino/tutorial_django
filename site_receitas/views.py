from django.shortcuts import get_object_or_404, render
from .models import Receita


def index(request):
    receitas = Receita.objects.all()
    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receitas = get_object_or_404(Receita, pk=receita_id)
    dados = {
        'receita': receitas
    }
    return render(request, 'receita.html', dados)


# Create your views here.

