from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login , authenticate
# Create your views here.

from . forms import Userform, PostForm, FormProfileUser
from . models import Posts, Category, Comment, ProfileUser
def index(request):
    prof = ProfileUser.objects.all()
    posts = Posts.objects.all()
    context = {
        'posts': posts,
        'prof': prof
    }
    return render(request, 'index.html',context)

def add_post(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST,)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()    
    return render(request, 'post/post.html', {'form': form})

def edit_post(request, pk):
    posts = get_object_or_404(Posts, id=pk)
    form =  PostForm(instance=posts)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=posts)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'post/edit_post.html', {'form':  form, 'posts': posts })    

def delete_post(request, pk):
    posts = get_object_or_404(Posts, id=pk)
    posts.delete()
    return redirect('index')
       

def singup(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form= Userform()        
    return render(request, 'accounts/singup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        user.save()
        login(request, user)
        return redirect('index')
    return render(request, 'accounts/login.html')


def user_profile(request):
    if request.method == "POST":
        form = FormProfileUser()
        if form.is_valid():
            form.save()
        return redirect('index')
    else :
        form = FormProfileUser()    
    return render(request, 'accounts/profile.html', {'form': form})    
