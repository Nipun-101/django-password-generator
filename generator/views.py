from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html',)

def password(request):

    character=list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))


    if request.GET.get('special'):
        character.extend(list('@#$&%!'))

    if request.GET.get('number'):
        character.extend(list('0123456789'))

    password=""
    length=int(request.GET.get('length',12))

    for i in range(length):

        password+=random.choice(character)


    return render(request,'generator/password.html',{'password':password})