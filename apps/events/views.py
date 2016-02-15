# -*- coding: utf-8 -*-

from django.shortcuts import render, Http404, HttpResponse
from profiles.models import City
from events.models import Category, Order
from events.forms import AddEventForm
from eworld.models import Attach
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


@login_required
def add_event(request):
    cities_set = City.objects.all()  # TODO remove it
    categories_set = Category.objects.all()  # TODO remove it

    context = {"cities_set": cities_set, "categories_set": categories_set}

    if not request.user.is_client:
        return HttpResponseForbidden(u'Только клиент может создавать проекты')

    if request.method == "GET":
        form = AddEventForm()
        context["form"] = form
        return render(request, 'eworld/add_event.html', context)
    elif request.method == "POST":
        form = AddEventForm(request.POST, request.FILES)
        context["form"] = form
        if form.is_valid():
            order = Order.objects.create(price=form.cleaned_data.get("price"),
                                         name=form.cleaned_data.get("name"),
                                         owner=request.user.client,
                                         city=form.cleaned_data.get("city"),
                                         description=form.cleaned_data.get("description"),
                                         requirements=form.cleaned_data.get("requirements"),
                                         event_date=form.cleaned_data.get("event_date"),
                                         )
            categories = form.cleaned_data.get("categories")
            if categories:
                order.categories.add(*categories)

            file_list = request.FILES.getlist("files")
            for each_file in file_list:
                Attach.objects.create(file=each_file, content_object=order)

            return HttpResponse("All ok!")
        else:
            return render(request, 'eworld/add_event.html', context)
    else:
        raise Http404
