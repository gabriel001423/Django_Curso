from django import forms

from .models import Tarefas

class TarefasForm(forms.ModelForm):

    class Meta:
        model = Tarefas                                                
        fields = ('titulo', 'descricao')