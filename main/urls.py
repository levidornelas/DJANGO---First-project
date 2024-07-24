from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('professor/<int:id>', views.professor, name='professor'),
    path('aluno/<int:id>', views.alunos, name='aluno'),
    path('contato', views.contato, name='contato')
]
