from django.shortcuts import get_object_or_404, redirect, render

from tarefas.forms import TarefasForm
from .models import Tarefas

# Create your views here.
def listaTarefas(request):
    tarefas_list = Tarefas.objects.all().order_by('-created_at')
    return render(request, 'tarefas/list.html', {'tarefas':tarefas_list})

# funçao adiciona uma nova tarefa
def novaTarefa(request):
    if request.method == 'POST':
        form = TarefasForm(request.POST)
        form.save()
        return redirect('/')
    
    else:
        form = TarefasForm()
        return render(request, 'tarefas/addTarefa.html', {'form':form})
    
# funçao pra edita a tarefa adcionada
def tarefaView(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    return render(request, 'tarefas/tarefa.html', {'tarefa':tarefa})

def editTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    form = TarefasForm(request.POST)

    if(request.method == 'POST'):
        form = TarefasForm(request.POST, instance=tarefa)
        
        if(form.is_valid()):
            tarefa.save()
            return redirect('/')
        else:
            return render(request, 'tarefas/editTarefa.html', {'form':form, 'tarefa':tarefa})
    else:
        return render(request, 'tarefas/editTarefa.html', {'form':form, 'tarefa':tarefa})

# funçao pra deleta a tarefa selecionada
def deleteTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    tarefa.delete()
    return redirect('/')