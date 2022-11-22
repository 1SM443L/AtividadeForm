from django import forms
from formulario.models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model=Aluno
        field= '__all__'
        
        widgets = {
            
            'mini_cursos': forms.CheckboxSelectMultiple(),
            'sexo': forms.RadioSelect(),
            'data_nascimento': forms.TimeInput(attrs={'type' : 'date'})
            
        }