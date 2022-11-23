from django.contrib import admin
from formulario.models import Curso, Aluno, MiniCursos

# Register your models here.

class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'cpf']
    search_list = ['nome']

class CursoAdmin(admin.ModelAdmin):
    search_fields = ['nome']

admin.site.register(Curso, CursoAdmin) 
admin.site.register(MiniCursos)
admin.site.register(Aluno)
