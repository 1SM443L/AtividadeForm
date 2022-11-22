from django.contrib import admin
from formulario.models import Curso, Aluno, MiniCursos

# Register your models here.

admin.site.register(Curso) 
admin.site.register(MiniCursos)
admin.site.register(Aluno)