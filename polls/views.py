from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from polls.models import Question, Choice

print()
def index(request):
    return HttpResponse('Olá... bem vindo a enquete')

def sobre(request):

    return HttpResponse('Este é um app de enquete!')


def exibe_questao(request, question_id):
    questao = Question.objects.get(id=question_id)

    if questao is not None:

        return HttpResponse(questao.question_text)

    return HttpResponse('Não existe questão a exibir')
