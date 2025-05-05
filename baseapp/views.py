from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello, world. You're at the polls page.</h1>")