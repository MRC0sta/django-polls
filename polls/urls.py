from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index, name = "index" ),
    path("sobre/", views.sobre, name="sobre"),
    path('pergunta/<int:question_id>', views.exibe_questao, name='exibe_questao'),
    path('perguntas', views.ultimas_perguntas, name='ultimas_perguntas'),
    path('cadastrar', views.QuestionCreateView.as_view(),
         name= 'question-create')


]



# .\venv\Scripts\activate.bat
# python manage.py runserver