# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
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
    