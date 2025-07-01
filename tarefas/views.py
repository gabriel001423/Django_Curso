from django.shortcuts import render

# Create your views here.
def listaTarefas(request):
    return render(request, 'tarefas/list.html')