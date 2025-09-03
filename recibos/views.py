from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Recibo
from .serializers import ReciboSerializer
from .serializers import PagoSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser

# Listar todos los recibos
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def lista_recibos(request):
    user = request.user
    if user.is_superuser:
        recibos = Recibo.objects.all()
    else:
        recibos = Recibo.objects.filter(usuario=user)
    serializer = ReciboSerializer(recibos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_recibo(request):
    serializer = ReciboSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(usuario=request.user)  # <--- Aquí se asegura que sea un objeto User
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_pago(request):
    data = request.data.copy()
    
    # Validar que venga recibo y monto
    recibo_id = data.get("recibo")
    monto = data.get("monto")
    
    if not recibo_id or not monto:
        return Response({"error": "Falta recibo o monto"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        recibo = Recibo.objects.get(id=recibo_id)
    except Recibo.DoesNotExist:
        return Response({"error": "Recibo no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    # Crear pago
    serializer = PagoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        
        # Marcar recibo como pagado
        recibo.pagado = True
        recibo.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")

    if not username or not password:
        return Response({"error": "Faltan campos"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({"error": "El usuario ya existe"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password, email=email)
    return Response({"message": "Usuario creado exitosamente"}, status=status.HTTP_201_CREATED)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    user = request.user
    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "is_staff": user.is_staff,
        "is_superuser": user.is_superuser
    })



@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Solo superusuarios pueden ver todos los usuarios
def lista_usuarios(request):
    usuarios = User.objects.all().values('id', 'username', 'email', 'is_staff', 'is_superuser')
    # values() devuelve un queryset de diccionarios
    return Response(list(usuarios), status=status.HTTP_200_OK)