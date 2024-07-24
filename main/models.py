from django.db import models

# Create your models here.

class Professor(models.Model):
  nome = models.CharField('Nome', max_length=50)
  email = models.EmailField('E-mail', max_length=100)
  salario = models.DecimalField('Salário', max_digits=8, decimal_places=2)
  carga_horaria = models.IntegerField('Carga horária(H)')

  def __str__(self) -> str:
    return self.nome

class Aluno(models.Model):
  nome = models.CharField('Nome', max_length=50)
  email = models.EmailField('E-mail', max_length=100)
  telefone_responsavel = models.CharField('Telefone do responsável', max_length=15)
  curso = models.CharField('Curso', max_length=50)
  
  def __str__(self):
    return self.nome