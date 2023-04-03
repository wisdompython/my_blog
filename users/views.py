from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from . forms import Register, CustomLoginForm, UserUpdateForm, ProfileUpdateForm
from .models import BlogPost, Profile, Category
# Create your views here.


def register(request):
    form = Register()
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            form.save()
            return redirect('home')
            
        else:
            print(form.errors)
           
            

    return render(request, 'account/signup.html',{'form':form})
@login_required
def edit_profile(request):
    user_profile = Profile.objects.filter(user=request.user)
    user_post = BlogPost.objects.filter(author=request.user)
    if request.method =='POST':
        user_update = UserUpdateForm(request.POST, instance=request.user)
        profile_update = ProfileUpdateForm( request.POST,
                                            request.FILES, 
                                            instance=request.user.profile)
        if user_update.is_valid() and profile_update.is_valid():
            user_update.save()
            profile_update.save()
        return redirect('/')
    else:
        user_update = UserUpdateForm(instance=request.user)
        profile_update = ProfileUpdateForm(instance=request.user.profile)

            
            
    
    return render( request, 'users/profile.html',{'user_post':user_post,'user_profile':user_profile,'profile_update':profile_update,'user_update':user_update})

def show_profile(request,username):
    category = Category.objects.all()
    user = User.objects.get(username=username)
    user_profile = Profile.objects.filter(user=user)
    user_post = BlogPost.objects.filter(author=user)
    
    return render(request, 'users/profile_page.html', {'user':user,'category':category,'user_post':user_post,'user_profile':user_profile})


def search_by_category(request):
    search_value = request.GET.get('search-tag')
    data = BlogPost.objects.filter(category=search_value)
    #data['search_input'] = search_input
    print(search_value)
    return render ( request, 'blog/search_result.html', {'data': data})
