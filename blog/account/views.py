from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from . import form as fm
from .models import Profile
from django.contrib.auth.decorators import login_required
from articles.models import Article

def selection_view(request):
    return render(request,"account/selection.html")

@login_required(login_url="/account/selection/")
def profile_view(request,user):
    profile=Profile.objects.get(user=request.user)
    articles = Article.objects.all().filter(author=profile.user)
    return render(request,'account/profile.html',{'profile':profile,'articles':articles})

def profile_search_result(request,user):
    if request.method == "GET":
        search = request.GET.get('result')
        print(search)
        profile = Profile.objects.get(profile_name=search)
        return render(request,'account/profile_search_result.html',{'profile':profile})

@login_required(login_url="/account/selection/")
def profile_edit_view(request):
    if request.method == 'POST':
        instance = Profile.objects.get(user=request.user)
        forms = fm.CreateAccount(request.POST,request.FILES,instance=instance)
        if forms.is_valid():
            forms.save()
            return redirect("account:profile",request.user)
    else:
        form = fm.CreateAccount()
        return render(request,"account/profile_edit.html",{'form':form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user =form.save()
            login(request,user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
        return render(request,"account/signup.html",{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')

    else:
        form = AuthenticationForm()
    return render(request,'account/login.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')
