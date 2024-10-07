from rest_framework import permissions

class AppointmentsPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.has_perm('appointments.view_appointment')
        elif request.method == "POST":
            return request.user.has_perm('appointments.add_appointment')
        elif request.method == "PUT" or request.method == "PATCH":
            return request.user.has_perm('appointments.change_appointment')
        elif request.method == "DELETE":
            return request.user.has_perm('appointments.delete_appointment')