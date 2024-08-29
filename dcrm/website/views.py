from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Records

def home(request):
    records = Records.objects.all()

    #check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authentication
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been Logged In!!!")
            return redirect('home')
        else:
            messages.success(request,"There was an Error in Login!!!")
            return redirect('home')
    

    return render(request,'home.html',{'records':records})




def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged In!!!")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfully registerd!!!")           

            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record = Records.objects.get(id=pk)
        return render(request, 'record.html',{'customer_record':customer_record})
    else:
        messages.success(request,"You Must be logged in to view that details...")
        return redirect('home')


def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_id = Records.objects.get(id=pk)
        delete_id.delete()
        messages.success(request,"Record Deleted Successfully...")
        return redirect('home')
    else:
        messages.success(request,"You Must be logged in to view that details...")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request,"Record Added successfully...")
                return redirect('home')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,"You Must be logged in to add details...")
        return redirect('home')
    
def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Records.objects.get(id=pk)
        form = AddRecordForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record Has been Updated!...")
            return redirect('home')
        return render(request,'update_record.html',{'form':form})
    else:
        messages.success(request,"You Must be logged in to update details...")
        return redirect('home')





    