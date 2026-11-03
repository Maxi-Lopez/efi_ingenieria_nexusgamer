
from rest_framework import permissions

class PermissionVendedor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.groups.filter(name__in=['Vendedor']).exists() or request.user.is_superuser)

class PermissionCliente(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        # Permitir clientes Y vendedores (para la wishlist)
        return request.user.groups.filter(name__in=['Cliente', 'Vendedor']).exists()
