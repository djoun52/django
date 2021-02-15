from django.http import HttpResponse


def index(request):
    result = "<h1>Hello, world. You're at the polls index.</h1>"
    return HttpResponse(result)


def page_1(request):
    result = "<h1>First Page</h1>"
    return HttpResponse(result)