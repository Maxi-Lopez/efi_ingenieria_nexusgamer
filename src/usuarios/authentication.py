from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class OptionalJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        try:
            # Intenta autenticar con el token JWT
            return super().authenticate(request)
        except AuthenticationFailed:
            # Si el token es inválido o está vencido, no lanzamos error 401.
            # Devolvemos None para que el usuario sea tratado como anónimo.
            return None
