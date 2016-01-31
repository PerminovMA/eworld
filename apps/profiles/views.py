# -*- coding: utf-8 -*-

from django.shortcuts import HttpResponse, render, Http404
from forms import RegistrationForm, EmailAuthorizationForm
from models import UserProfile, EventManager, Client
import json
from django import forms
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


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

            user_type = request.POST.get("user_type")
            if user_type == RegistrationForm.CLIENT_LABEL:
                Client.objects.create(user=user_obj)
            elif user_type == RegistrationForm.EVENT_MANAGER_LABEL:
                EventManager.objects.create(user=user_obj)  # TODO add legal_status and categories

            user = authenticate(username=user_obj.email, password=form.cleaned_data.get("password"))

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('eworld:dashboard'))
            return HttpResponse(u"Произошла ошибка. Пожалуйста, обратитесь к администратору.")
        else:
            return render(request, 'profiles/registration.html', {"form": form})
    else:
        raise Http404


def user_authorization(request):
    if request.user.is_authenticated():
        pass  # TODO redirect to success page

    if request.method == "GET":
        form = EmailAuthorizationForm()
        return render(request, 'profiles/authorization_modal.html', {"form": form})
    elif request.method == "POST":
        request_data = json.loads(request.body)  # angular specific
        form = EmailAuthorizationForm(request_data)

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse(json.dumps({'result': 'ok', 'redirect_url': reverse('eworld:dashboard')}))

            form.add_error("password", forms.ValidationError('Email or password not valid'))

        req_data = {'result': 'nok', 'errors': form.errors}
        return HttpResponse(json.dumps(req_data))
    else:
        raise Http404


def logout(request):
    logout(request)
    return HttpResponse('logout')