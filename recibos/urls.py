from django.urls import path
from .views import lista_recibos, crear_recibo, crear_pago, user_info, register_user, lista_usuarios

urlpatterns = [
    path("recibos/", lista_recibos, name="recibos-lista"),
    path("recibos/crear/", crear_recibo, name="recibos-crear"),
    path('pagos/crear/', crear_pago ,name="crear_pago"),
    path("user/", user_info, name="user_info"),
    path('CreateUser/', register_user, name="register_user"),
    path('usuarios/', lista_usuarios, name='lista_usuarios'),
]