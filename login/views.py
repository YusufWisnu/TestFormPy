from django.shortcuts import render
from .forms import loginForm
# Create your views here.
def index(request):
    formLogin = loginForm()
    context = {
        'FormLogin' : formLogin
    }
    return render(request, 'login/index.html', context)