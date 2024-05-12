from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def LoginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, "Please try again, your password is wrong!")
                
    return render(request, 'authenticate/LoginUser.html')
