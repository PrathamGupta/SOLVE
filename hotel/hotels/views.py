# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse

from .models import Register, Card


# Create your views here.
def index(request):
    error_message=''
    # if request.method=='POST':
    #     username = request.POST['email']
    #     password = request.POST['password']
    #     post = Register.objects.get(email=username)
    #     if post:
    #         if password == post.password:
    #             error_message='Wrong Password Entered'
    #             request.session['username'] = username
    #             return HttpResponseRedirect(reverse('hotels:index'))
    #         else :
    #             error_message='Wrong Username Entered'
    #             return HttpResponseRedirect(reverse('hotels:index'))
    #     else:
    #         return HttpResponseRedirect(reverse('hotels:index'))
    
    card_list= Card.objects.all()
    logged_in = False
    if 'username' in request.session:
        logged_in = True
    if 'username' not in request.session:
        logged_in = False
    context = {
        'card_list' : card_list,
        'logged_in': logged_in,
        'error_message': error_message,
    }
    return render(request, 'hotels/base.html', context)

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
    
def logoutPage(request):
    try: 
        del request.session['username']
    except:
        pass
    return HttpResponseRedirect(reverse('hotels:index'))

def loginPage(request):
    username = password = ''
    response_data = {'user': '', 'login' : "Failed"}
    if request.POST and request.is_ajax:
        username = request.POST['email']
        password = request.POST['password']
        try:
            get_user = Register.objects.get(email=username)
            if get_user.password==password:
                request.session['username'] = username
                response_data = {'login' : "Success"}
            else:
                response_data = {'user':"password wrong"}
        except Register.DoesNotExist:
            response_data = {'user':"nouser"}
    else:
        username = password = ''
        response_data = {'login': "Failed"}
    return JsonResponse(response_data)
