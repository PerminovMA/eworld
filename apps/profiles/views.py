from django.shortcuts import HttpResponse, render, Http404
from forms import RegistrationForm, EmailAuthorizationForm
from models import UserProfile
from django.views.decorators.csrf import csrf_exempt


def user_registration(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, 'profiles/registration.html', {"form": form})
    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_obj = UserProfile(username=form.cleaned_data.get("username"),
                                   phone_number=form.cleaned_data.get("phone_number"),
                                   email=form.cleaned_data.get("email"), first_name=form.cleaned_data.get("first_name"),
                                   last_name=form.cleaned_data.get("last_name"))
            user_obj.set_password(form.cleaned_data.get("password"))
            user_obj.save()
            return HttpResponse(str("USER CREATED!"))  # TODO render to some page
        else:
            return render(request, 'profiles/registration.html', {"form": form})
    else:
        raise Http404


# @csrf_exempt
def user_authorization(request):
    print "USER_AUTHORIZATION"
    if request.method == "GET":
        print "USER_AUTHORIZATION GET"
        form = EmailAuthorizationForm()
        return render(request, 'profiles/authorization_modal.html', {"form": form})
    elif request.method == "POST":
        form = EmailAuthorizationForm(request.POST)
        if form.is_valid():
            user_obj = UserProfile.objects.get(email=form.cleaned_data.get("email"))
            print "AUTH"
            # TODO add auth script
            return render(request, 'profiles/authorization_modal.html', {"form": form})
        else:
            print "FORM NOT VALID"
            return render(request, 'profiles/authorization_modal.html', {"form": form})
    else:
        raise Http404