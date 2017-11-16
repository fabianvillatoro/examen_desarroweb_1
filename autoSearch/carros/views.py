# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.template import Template , Context, loader
from .models import Car
from django.views.generic import DetailView, ListView

def home(request):
    tweets = Tweet.objects.all()

    return render(request, "home.html", context={"msg":"esta es una prueba", "tweets":tweets})
def prueba(request):
    Context = locals()
    templates = loader.get_template('home.html')
    #return render(request, 'home.html')
    return HttpResponse(templates.render(Context, request))

class car_list(ListView):
    template_name = "base/estructura.html"
    #template_name = 'templates/basic/car_list.html'
    queryset = Car.objects.all()


class car_detail(DetailView):
     template_name = "basic/car_detail.html"
     queryset = Car.objects.all()


def get_object(self):
        id = self.kwargs.get("id")
        #print id
        return Car.objects.get(id=id)
