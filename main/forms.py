from django import forms
from formulario.models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
        
        widgets = {
            'sexo': forms.RadioSelect(),
            'minicursos': forms.CheckboxSelectMultiple(),
            'data_nascimento': forms.TimeInput(attrs={'type' : 'date'}),    
        }