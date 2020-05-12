# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Card


# Create your views here.
def index(request):
    card_list= Card.objects.all()
    template = loader.get_template('hotels/index.html')
    context = {
        'card_list' : card_list,
    }
    return render(request, 'hotels/index.html', context)

def makeCard(request):
    context = {
        'error_message': False,
    }
    return render(request, 'hotels/makeCard.html', context)

def addCard(request):
    hotel_name = request.POST['hotel_name']
    city = request.POST['city']
    state = request.POST['state']
    date = request.POST['date']
    price = request.POST['price']
    card = Card(hotel_name=hotel_name, city=city, state=state, date=date, price=price)
    card.save()
    return HttpResponseRedirect(reverse('hotels:index'))