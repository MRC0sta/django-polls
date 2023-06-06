from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index, name = "index" ),
    path("sobre/", views.sobre, name="sobre"),
    path('pergunta/<int:question_id>', views.exibe_questao, name='exibe_questao')
]

# .\venv\Scripts\activate.bat
# python manage.py runserver