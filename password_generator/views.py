from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request) :
    return render(request, 'env1/home.html')

def about(request) :
    return render(request, 'env1/about.html')

def password(request) :

        charactors = list('abcdefghijklmnopqrstuvwxyz')

        if request.GET.get('uppercase'):
            charactors.extend(list('ABCDFGHIJKLMNOPQRSTUVWXYZ'))
        if request.GET.get('special'):
            charactors.extend(list('!@#$%^&*()?'))
        if request.GET.get('numbers'):
            charactors.extend(list('0123456789'))

        length = int(request.GET.get('length',12))

        thepassword = ''
        for x in range(length) :
            thepassword += random.choice(charactors)

        return render(request, 'env1/password.html', {'password':thepassword})
