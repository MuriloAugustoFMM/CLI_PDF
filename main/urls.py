from django.urls import path,include
from main import views
app_name = 'main'

urlpatterns = [
    path('', views.index),
    path('visualizar-relatorio',views.visualizar_relatorio,name='visualizar-relatorio'),
    path('relatorio-fotografico',views.criar_formulario,name='criar-relatorio-foto')
]