from django.shortcuts import HttpResponse, render


def user_registration(request):
    context = {}
    return render(request, 'profiles/registration.html', context)


def user_authorization(request):
    return HttpResponse("user_authorization")