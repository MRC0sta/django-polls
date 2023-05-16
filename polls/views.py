from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

print()
def index(request):
    return HttpResponse('Olá... bem vindo a enquete')

def sobre(request):
<<<<<<< HEAD
    return HttpResponse('Este é um app de enquete!')

=======
    return HttpResponse("Este é um app de enquete!")
>>>>>>> a8b2d639e791d4da7542be219c78e0fb07b4f3f3
