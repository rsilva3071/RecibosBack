from rest_framework import serializers
from .models import Recibo, Pago

class ReciboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recibo
        fields = '__all__'
        read_only_fields = ["id", "creado_en"]


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'