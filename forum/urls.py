from django.urls import path

from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('quem-somos/', views.QuemSomosView.as_view(), name='quem_somos'),
    path('sobre-o-projeto/', views.SobreProjetoView.as_view(),
         name='sobre_projeto'),
    path('fale-conosco/', views.FaleConoscoView.as_view(),
         name='fale_conosco'),
]
