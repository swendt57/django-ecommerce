from django.shortcuts import render


def index(request):
    """Displays the index page"""
    return render(request, 'index.html')
