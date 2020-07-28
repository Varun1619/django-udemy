from django.shortcuts import render
from basic_app.forms import UserProfileInfoForm,UserForm


from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse('You are logged in!!')



@login_required
#Tjis is a Decorator. This '@login_required will tell django that it is necesarry to login first inorder to logout
#Thi will also make sure that only the logged in user is logedout. 
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    # this will log out the user 


def register(request):

    registered = False
    #This variable will tell us if the user has already registred or not, hence we first set ti False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        #The above variables will store the values of the form in these particular functions from form.py

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            #This variable will store the data that the user gave in the form in the database 
            user.set_password(user.password)
            #this will hash the password entered by the user by taking this password into the hassers in the setting.py
            user.save()
            #This will save the password in data base

            profile = profile_form.save(commit=False)
            #This variable will store the profile pic into the data base but currently it wont as 'commit = False'
            profile.user = user 
            #this links forms , models and views together

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()
            #this will save the profile picture

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html', {'user_form': user_form,
                                                           'profile_form' : profile_form,
                                                           'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        #here we are using the get method to get the username of the user, We have given name= username in login.html file
        password = request.POST.get('password')
        #here we are using the get method to get the password of the user, We have given name= password in login.html file

        #here we will django's built in authentication
        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
        #the if condition will check if the user is authenticated or not and if it is 
        #then it will login the user. After loging in the user it will rederect him/her to the index page. 
            else:
                HttpResponse('Account Not Active')
        else:
            print('Failed Log in')
            print('Username : {} and password : {}'.format(username,password))
            return HttpResponse("Invalid Log in detailes supplied")
        #This will print back the information of the user who entered the incorrect password or username into the console. 
    else:
        return render(request, 'basic_app/log_in.html', {})