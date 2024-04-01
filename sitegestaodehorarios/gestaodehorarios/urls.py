from django.urls import path
from . import views
# o '.' significa que importa views da mesma directoria)
app_name = 'gestaodehorarios'
urlpatterns = [
    path('', views.index, name='index'),
    path('carregar_salas', views.carregar_salas, name='carregar_salas'),
    path('processar_csv', views.processar_csv, name='processar_csv'),
    path('pagina_horario', views.pagina_horario, name='pagina_horario'),
    path('verificar_salas', views.verificar_salas, name='verificar_salas'),
]
