from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from .models import *



# Create your views here.
def welcome(request):
    return render(request,"main/welcome.html")

def register(request):
    '''
    Function to register new users to the database.
    '''
    if request.method == 'POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"You have succesfully created an account. Proceed to Login")
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request,"users/sign-up.html",context)

#@login_required
def Index_view(request):
    '''will show products around the user
    '''
    current_user = request.user
    profile = request.user.profile
    current_area_product = request.user.profile.area
    products = Product.objects.filter(area=current_area_product)
    
    
    context = {
        "products":products,
        "profile":profile,
        "current_user":current_user
    }
    return render(request,"main/index.html",context)

def user_info(request):
    '''
    will show users profile and their neighbours
    '''
    current_user = request.user
    profile = request.user.profile
    context = {
       # "neighbours":neighbours.exclude(user=current_user),
        "profile":profile,
        "current_user":current_user
    }

    return render(request,"users/my_profile.html",context)
#@login_required
def profile(request):
    '''
    This method handles the user profile 
    '''
    title = 'Profile'
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"You Have Successfully Updated Your Profile!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'title':title,
        'u_form':u_form,
        'p_form':p_form 
    }
    return render(request,'users/profile.html',context)