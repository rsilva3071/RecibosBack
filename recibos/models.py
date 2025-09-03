from django.db import models
from django.contrib.auth.models import User

class Recibo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recibos")
    concepto = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    creado_en = models.DateTimeField(auto_now_add=True)
    pagado=models.BooleanField(default=False)

    def __str__(self):
        return f"Recibo {self.id} - {self.usuario.username}"


class Pago(models.Model):
    recibo = models.ForeignKey(Recibo, on_delete=models.CASCADE, related_name="pagos")
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    pagado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago {self.id} de {self.recibo}"