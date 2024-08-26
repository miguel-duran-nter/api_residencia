from rest_framework import exceptions

class LoggedInCookieMixin:
    def check_logged_in(self, request):
        logged_in = request.COOKIES.get('logged_in')
        if logged_in != 'true':
            raise exceptions.PermissionDenied("You must be logged in to access this resource.")
