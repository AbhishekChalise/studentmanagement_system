from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        # Check if user is None (authentication failed)
        if user is None:
            print("Authentication failed")
            # You can add a message here to notify the user (e.g., invalid username/password)
            return render(request, 'Login.html', {'error': 'Invalid credentials'})
        # Check if the user is a superuser
        if user.is_superuser:
            print("Hey SuperUser")
        print(user)
        # Log in the user
        login(request, user)
        print(f'{username} successfully logged in')

        # Redirect to the admin page or wherever you want after login
        return redirect('student_registration')

    else:
        return render(request, 'Login.html')
    
def log_out(request):
    logout(request)
    return redirect('login')




