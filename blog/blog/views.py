from django.http import HttpResponse
from django.shortcuts import render
from account.models import Profile

def home(request):
    #return HttpResponse("Home")
    return render(request,"homepage.html")

def about(request):
    #return HttpResponse("about")
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def search_view(request):
    if request.method == "GET":
        search = request.GET.get('search')
        post = Profile.objects.all().filter(profile_name=search)
        return render(request,'search.html',{'post':post})