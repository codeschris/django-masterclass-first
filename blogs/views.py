from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse("Hello, this is a test response from the blogs app.")

def home(request):
    return render(request, 'pages/index.html')