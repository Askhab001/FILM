from django.shortcuts import render


def index(request):
    users = ["Admin", "User", "Guest"]
    return render(request, 'register.html', {'users': users})


