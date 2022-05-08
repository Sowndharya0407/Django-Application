from django.shortcuts import render,redirect

from .models import BlogPost
from .forms import BlogPostForm,CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


# --------Register Page---------
def Register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form_filled = CreateUserForm(request.POST)
            if form_filled.is_valid():
                form_filled.save()
                user = form_filled.cleaned_data.get('username')
                messages.success(request,"Account has been created for "+user)
                return redirect('login')

        context = {'form':form,}
        return render(request,'blogApp/register.html',context)


# --------Login Page---------
def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            user_name = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=user_name,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,"Username or password is incorrect")

        return render(request,'blogApp/login.html')

# --------------Logout----------
def Logout(request):
    logout(request)
    return redirect('login')

# ------Dashboard Page------------
@login_required(login_url='login')
def home(request):
    blogs = BlogPost.objects.all()
    context = {'blogs':blogs,}
    return render(request,'blogApp/dashboard.html',context)



# -------------Create Blog info-----------
@login_required(login_url='login')
def CreateBlog(request):
    form = BlogPostForm()
    button = "Create"

    if request.method == 'POST':
        form_data = BlogPostForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('home')

    context = {'form':form,'btn':button}
    return render(request,'blogApp/display.html',context)

# -----Update Blog info----------
@login_required(login_url='login')
def UpdateBlog(request,idval):
    form_rec = BlogPost.objects.get(id=idval)
    form = BlogPostForm(instance=form_rec)
    button = "Update"

    if request.method == 'POST':
        updated_form = BlogPostForm(request.POST,instance = form_rec)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('home')

    context = {'form':form,'btn':button,}
    return render(request,'blogApp/display.html',context)


# ------------delete blog info--------
@login_required(login_url='login')
def DeleteBlog(request,pk):
    form_rec = BlogPost.objects.get(id=pk)
    title = form_rec.title
    if request.method == 'POST':
        form_rec.delete()
        return redirect('home')

    context = {'title':title}
 
    return render(request,'blogApp/delete.html',context)
