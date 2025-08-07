from django.http import HttpResponse

def test(request):
    return HttpResponse("Hello, this is a test response from the blogs app.")
