from django.db import models

# Create your models here.

LISTA_SEXO= [   
    ('Masculino', 'Masculino'),
    ('Feminino',  'Feminino')
]


class Curso(models.Model):
    nome = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.nome

class MiniCursos(models.Model):
    nome = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    email = models.EmailField()
    endereço = models.CharField(max_length=150)
    sexo =  models.CharField(max_length=100, choices=LISTA_SEXO)
    curso = models.ForeignKey(Curso, null=True, on_delete=models.CASCADE)
    mini_cursos: models.ManyToManyField(MiniCursos)
    
    def __str__(self) -> str:
        return self.nome
