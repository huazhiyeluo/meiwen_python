from django.shortcuts import render

# Create your views here.
def login():
    data          = {}
    return render(request, 'index/info.html', data)

def logindoweb():
    data          = {}
    return render(request, 'index/info.html', data)

def loginreturn():
    data          = {}
    return render(request, 'index/info.html', data)

def logindo():
    data          = {}
    return render(request, 'index/info.html', data)

def logout():
    data          = {}
    return render(request, 'index/info.html', data)