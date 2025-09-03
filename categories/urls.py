from django.urls import path
from . import views

urlpatterns = [
    path("crear/", views.crear_recibo, name="crear_recibo"),
    path("lista/", views.lista_recibos, name="lista_recibos"),
    path("pagar/<int:recibo_id>/", views.pagar_recibo, name="pagar_recibo"),
]