from django.shortcuts import render

def index(request):
    context = {
        'judul': 'Welcome'
    }

    return render(request, 'index.html', context)