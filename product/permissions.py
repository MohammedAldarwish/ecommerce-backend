from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    """
    only the admin can Delete/Add/Edit The products
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff