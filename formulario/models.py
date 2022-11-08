from django.db import models

# Create your models here.

LISTA_SEXO= [   
    ('Masculino', 'Masculino'),
    ('Feminino',  'Feminino')
]

LISTA_CURSO= [
    ('Curso técnico', 'Curso técnico'),
    ('Curso superior',  'Curso superior')
]


class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    email = models.EmailField()
    endereço = models.CharField(max_length=150)
    sexo =  models.CharField(max_length=100, choices=LISTA_SEXO)
    curso = models.CharField(max_length=150, choices=LISTA_CURSO)
    mini_cursos: models.BooleanField()
    
    def __str__(self) -> str:
        return self.nome
