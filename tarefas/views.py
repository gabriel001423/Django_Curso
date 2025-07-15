from django.shortcuts import get_object_or_404, redirect, render
from tarefas.forms import TarefasForm
from .models import Tarefas
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def listaTarefas(request):
    tarefas_list = Tarefas.objects.all().order_by('-created_at').filter(usuario=request.user)
    return render(request, 'tarefas/list.html', {'tarefas':tarefas_list})

# funçao adiciona uma nova tarefa
@login_required
def novaTarefa(request):

    if request.method == 'POST':
        form = TarefasForm(request.POST)
        if form.is_valid():
            tf = form.save(commit=False)
            tf.usuario = request.user
            tf.save
        return redirect('/')
    
    else:
        form = TarefasForm()
        return render(request, 'tarefas/addTarefa.html', {'form':form})
    
# funçao pra edita a tarefa adcionada
@login_required
def tarefaView(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    return render(request, 'tarefas/tarefa.html', {'tarefa':tarefa})

@login_required
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
@login_required
def deleteTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    tarefa.delete()
    return redirect('/')