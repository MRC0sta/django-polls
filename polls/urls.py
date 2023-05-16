from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index, name = "index" ),
    path("sobre/", views.sobre, name="sobre")
]

# .\venv\Scripts\activate.bat
# python manage.py runserver