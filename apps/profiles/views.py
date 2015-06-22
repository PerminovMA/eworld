from django.shortcuts import HttpResponse, render, Http404
from forms import RegistrationForm, EmailAuthorizationForm
from models import UserProfile


def user_registration(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, 'profiles/registration.html', {"form": form})
    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_obj = UserProfile(phone_number=form.cleaned_data.get("phone_number"),
                                   email=form.cleaned_data.get("email"), first_name=form.cleaned_data.get("first_name"),
                                   last_name=form.cleaned_data.get("last_name"))
            user_obj.set_password(form.cleaned_data.get("password"))
            user_obj.save()
            return HttpResponse(str("USER CREATED!"))  # TODO render to some page
        else:
            return render(request, 'profiles/registration.html', {"form": form})
    else:
        raise Http404


def user_authorization(request):
    if request.method == "GET":
        form = EmailAuthorizationForm()
        return render(request, 'profiles/registration.html', {"form": form})  # TODO need to change template
    elif request.method == "POST":
        form = EmailAuthorizationForm(request.POST)
        if form.is_valid():
            # TODO auth script
            return HttpResponse("pass")
        else:
            return render(request, 'profiles/registration.html', {"form": form})  # TODO auth script
    else:
        raise Http404