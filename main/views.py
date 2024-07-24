from django.shortcuts import render
from .models import Professor, Aluno

# Create your views here.
def index(request):
    professores = Professor.objects.all()
    alunos = Aluno.objects.all()
    info = {
       'professores': professores,
       'alunos': alunos
    }
    return render(request, 'index.html', info)

def professor(request, id):
  professores = Professor.objects.get(id = id)

  info = {
    'professores': professores
  }
  return render(request, 'professor.html', info)

def alunos(request,id):
   alunos = Aluno.objects.get(id = id)

   info = {
      'alunos': alunos
   }
   return render(request, 'aluno.html', info)

def contato(request):
   return render(request, 'contato.html')