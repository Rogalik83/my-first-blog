from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def bye(request):
    return HttpResponse('au revoir')
