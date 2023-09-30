from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
def home1(request):
    data = {"Hello" : "World"}
    return JsonResponse(data)

def home2(request):
    return HttpResponse("World Hello")

def home3(request):
    context = {
        "item1" : "An Object-Relational Mapping (ORM) system for database interaction.",
        "item2" : "A built-in admin interface for managing application data.",
        "item3" : "A powerful templating system for creating dynamic web pages.",
        "item4" : "Integrated authentication and authorization systems for user management.",
        "item5" : "Automatic URL routing and request handling.",
        "item6" : "Extensive documentation and a supportive community.",
    }
    return render(request, "myapp/index.html", context)