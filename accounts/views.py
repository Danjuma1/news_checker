from django.shortcuts import  render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .forms import NewUserForm
from .models import UserProfile



# View for Registration 
def register_view(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user_form = form.save()
			username = form.cleaned_data.get('username')
			age_range = form.cleaned_data.get('age_range')
			user = User.objects.get(username=username)
			user_data = UserProfile.objects.create(user=user, age_range=age_range)
			user_data.save()
			login(request, user_form)
			messages.success(request, "Registration successful." )
			return redirect("core:dashboard")
		else:
			messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="accounts/register.html", context={"form":form})


# View for Login
def login_view(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("core:dashboard")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="accounts/login.html", context={"form":form})

# Logout View
def logout_view(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("core:homepage")