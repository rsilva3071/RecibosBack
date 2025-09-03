from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

@api_view(['GET'])
def hola(request):
    return Response({"mensaje": "Hola desde Django"})

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        print(username)
        print(password)
        # 👇 lógica de validación
        if username == "admin" and password == "1234":
            return Response({"success": True, "message": "Login exitoso"}, status=status.HTTP_200_OK)
        else:
            return Response({"success": False, "message": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
        
        