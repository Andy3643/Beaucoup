from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth import login,authenticate,logout


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

#@login_required
# def new_product(request):
#     '''
#     upload new product
#     '''
#     current_user = request.user
#     current_area_user = request.user.profile.area
#     if current_area_user:
#         if request.method == "POST":
#             form = ProductUpload(request.POST) 
#             if form.is_valid():
#                 product_name = form.save(commit=False)
#                 product_name.seller = current_user
#                 product_name.area = current_area_user
#                 product_name.save()
#                 return redirect(Index_view)
            
#             else:
#                 form = ProductUpload()
#                 return render(request,"product/upload-product.html",{"form":form})


def new_product(request):
    '''
    upload new product
    '''
    current_user = request.user
    if request.method == "POST":
        form = ProductUpload(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = current_user
            product.save()
            return redirect('home')
    else:
        form = ProductUpload()
    context = {
        "form":form
    }

    return render(request,"product/upload-product.html",context)


def signout(request):
    logout(request)
    messages.success(request,"You have logged out, we will be glad to have you back again")
    return redirect ("login")

def chat (request):
    username = request.GET.get('username')
    
    
    
    
    return render (request,'product/chat.html',{'username':username})

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    new_message = Message.objects.create(value=message, user=username)
    new_message.save()
    return HttpResponse('Message sent successfully')
