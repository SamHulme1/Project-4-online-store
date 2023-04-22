from django.shortcuts import render


def index(request):
    """view for the home page"""
    return render(request, 'home/index.html')

