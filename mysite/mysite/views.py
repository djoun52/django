from django.http import HttpResponse


def index(request):
    result = "<h1>welcome to my site</h1>"
    return HttpResponse(result)


