from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
  
    return render(request, "base.html")
    # name = request.GET.get("name") or "world"
    # return HttpResponse("Hello, {}!".format(name))

def search(request):
    search = request.GET.get("search") or ""
    return render(request, "search.html", {"search": format(search)})