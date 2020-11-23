from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import form
import time
from account.models import Profile


def article_list(request):
    articles = Article.objects.all().order_by('date')

    return render(request,'articles/article_list.html',{'articles':articles})


def article_details(request,slug):
    #return HttpResponse(slug)

    article =Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article':article})


@login_required(login_url="/account/selection/")
def article_create(request):
    if request.method == 'POST':
        forms = form.CreateArticle(request.POST,request.FILES)
        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.author = request.user
            instance.save()
            update = Profile.objects.get(user=instance.author)
            last = instance.date - update.last_update
            
            if last.total_seconds() <= 300:
                update.artilce_num = update.artilce_num + 1
                if update.artilce_num == 3:
                    print("stfp")
                    update.artilce_num = 0
                    return render(request,"articles/warning.html")

            else:
                update.artilce_num = 0    
                
            return redirect("articles:list")
    else:
        forms = form.CreateArticle()
        return render(request,"articles/article_create.html",{'form':forms})