from django.contrib import admin
from .models import Professor, Aluno
# Register your models here.

class ProfessorAdmin(admin.ModelAdmin):
  list_display = 'nome', 'email', 'salario', 'carga_horaria'

class AlunoAdmin(admin.ModelAdmin):
  list_display = 'nome', 'email', 'telefone_responsavel'

admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Aluno, AlunoAdmin)