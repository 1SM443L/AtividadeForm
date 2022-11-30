from django.shortcuts import render
from main.forms import AlunoForm

# Create your views here.

def cadastrar(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            form = AlunoForm()
    else:
        form = AlunoForm()
    
    return render (request,"formulario.html", {'form' : form })
