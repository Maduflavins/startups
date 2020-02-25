from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == "POST":
        # user wants an account
        hashed_pw1 = bcrypt.hashed_pw(request.POST['password1'].encode('utf8'), bctypt.gensalt)
        hashed_pw2 = bcrypt.hashed_pw(request.POST['password2'].encode('utf8'), bctypt.gensalt)
        
        if hashed_pw1 == hashed_pw2:
            try:
                
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                User.objects.create_user(request.POST['username'], password=hashed_pw1)
                auth.login(request, user)
                return redirect('home')
        return render(request, 'accounts/signup.html', {'error': 'Password must Match'})
    else:
        #somethin else
        return render(request, 'accounts/signup.html')
    
    
def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',{'error':'username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')
    
    
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
 
 
