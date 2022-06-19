from django.shortcuts import redirect, render 
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views import View
from math import ceil


def BASE(request):
    return render(request,'base.html')

def LOGOUT(request):
    auth.logout(request)
    return render(request,'login.html')

@login_required(login_url='login')
def INDEX(request):
    trending_post = Post.objects.filter(section ='Trending').order_by('date')[0:4]
    popular_post = Post.objects.filter(section ='Popular').order_by('date')[0:5]
    topic = Topic.objects.all()
    context ={
        'trending_post':trending_post,
        'popular_post':popular_post,
        'topic':topic,
    }
    return render(request,'index.html',context)


class Login(View):
    @login_required(login_url='login')
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request,user) 
            print(1)
            
        else:
            # Return an 'invalid login' error message.
            print(username,password)
        return redirect('home')

class Blog(View):
    @login_required(login_url='login')
    def get(self,request,pk):
        p = Post.objects.get(pk=pk)
        print(p)
        context = {
            'data' : p
        }
        return HttpResponse ('<h1>Xin chao<h1>',context)
    def post(self,request):
        pass



class Register(View):
    def get(self,request):
        return render(request,'register.html')
    
    def post(self,request):
        pass

class Single(View):
    def get(self,request,pk):
        p = Post.objects.get(pk=pk)
        popular_post = Post.objects.filter(section ='Popular').order_by('date')[0:5]
        topic = Topic.objects.all()
        context = {
            'data' : p,
            'popular_post':popular_post,
            'topic':topic,
        }
        return render(request,'single.html',context)
    def post(self,request):
        pass

class AddPost(View):
    def get(self,request):
        return render(request,'addPost.html')
    def post(self,request):
        pass

class ManageTopic(View):
    def get(self,request):
        return render(request,'managetopic.html')
    def post(self,request):
        pass

class ManagePost(View):
    def get(self,request):
        return render(request,'managepost.html')
    def post(self,request):
        pass

class AddTopic(View):
    def get(self,request):
        return render(request,'addTopic.html')
    def post(self,request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        temp = Topic.objects.filter(name=title)
        if temp.count() >=1:
            return HttpResponse('<h1>Loi<h1>')
        topic = Topic(name=title,description=description)
        topic.save()
        return render(request,'addTopic.html')
        

class ManageUser(View):
    def get(self,request):
        return render(request,'manageuser.html')
    def post(self,request):
        
        return render(request,'addTopic.html')
        
class AddUser(View):
    def get(self,request):
        return render(request,'addUser.html')
    def post(self,request):
        
        return render(request,'addUser.html')

class TopicView(View):
    def get(self,request,pk,page=1):
        if type(pk) == int:
            tp = Topic.objects.filter(pk=pk).first()
            topic = Topic.objects.all()
            rs = Post.objects.filter(category = tp)
            pages = ceil((rs.count()/5))
            page_list = []
            previous = 1
            next = 1
            if page:
                previous = page - 1
                next = page + 1
                if page <= pages:
                    for i in range(page-2,page+2):
                        if i >=1 and i <= pages:
                            page_list.append(i)
                    if page < pages:
                        rs = rs[int(page-1)*5:(page*5)]
                    else: rs = rs[int(page-1)*5:rs.count()]
                if previous<=0:
                    previous = 1
                if next > pages:
                    next = pages
            context = {
                'pk':pk,
                'page':page,
                'rs':rs,
                'title':tp.name,
                'previous':previous,
                'next':next,
                'page_list':page_list,
                'topic':topic,
            }
            print(context)
        return render(request,'topic.html',context)
    def post(self,request):
        return render(request,'addUser.html')
