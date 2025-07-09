from django.shortcuts import redirect, render

from tarefas.forms import TarefasForm
from .models import Tarefas

# Create your views here.
def listaTarefas(request):
    tarefas_list = Tarefas.objects.all().order_by('-created_at')
    return render(request, 'tarefas/list.html', {'tarefas':tarefas_list})


def novaTarefa(request):
    if request.method == 'POST':
        form = TarefasForm(request.POST)
        form.save()
        return redirect('/')
    
    else:
        form = TarefasForm()
        return render(request, 'tarefas/addTarefa.html', {'form':form})