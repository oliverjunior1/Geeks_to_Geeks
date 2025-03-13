from django.http import HttpResponse

def hellogeeks(request):
    return HttpResponse("Hello Geeks")