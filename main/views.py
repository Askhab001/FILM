from django.shortcuts import render


def index(request):
    return render(request, 'register.html')


def main(request):
    return render(request, 'assa.html')


def aza(request):
    return render(request, 'aza.html')
