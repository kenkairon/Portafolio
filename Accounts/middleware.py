# accounts/middleware.py

from django.shortcuts import redirect
from django.urls import reverse

class RedirectAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Si el usuario está autenticado y accede a login o register, lo redirigimos
        if request.user.is_authenticated:
            if request.path in [reverse('login'), reverse('register')]:
                return redirect('dashboard')
        
        response = self.get_response(request)
        return response
