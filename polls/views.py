from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def search(request, retez):
    return HttpResponse("The id found: " + str(retez))
