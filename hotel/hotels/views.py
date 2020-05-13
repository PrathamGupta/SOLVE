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
    
    card_list= Card.objects.all()
    state_list = Card.objects.order_by().values('state').distinct()
    date_list = Card.objects.order_by().values('date').distinct()
    print(state_list)
    logged_in = False
    if 'username' in request.session:
        logged_in = True
    if 'username' not in request.session:
        logged_in = False
    context = {
        'card_list' : card_list,
        'state_list': state_list,
        'date_list' : date_list,
        'logged_in': logged_in,
        'error_message': error_message,
    }
    print("LOGGGEDDDD INNN ISSS")
    print(logged_in)
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
                request.session.set_expiry(0)
                response_data = {'login' : "Success"}
            else:
                response_data = {'user':"password wrong"}
        except Register.DoesNotExist:
            response_data = {'user':"nouser"}
    else:
        username = password = ''
        response_data = {'login': "Failed"}
    return JsonResponse(response_data)


def register(request):
    first_name = last_name = email = checkpassword = password = h = ''
    response_data = {'user' : '', 'passmatch': '', 'login': ''}
    if request.POST and request.is_ajax:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        checkpassword = request.POST['checkpassword']
        h = request.POST['hotel']
        if password != checkpassword:
            response_data = {'passmatch' : 'did not match'}
        try:
            get_user = Register.objects.get(email=email)
            response_data={'user': 'already present'}
        except Register.DoesNotExist:
            hotel = False
            if h == 'hotel':
                hotel=True
            user = Register(first_name=first_name, last_name= last_name, email= email, password= password, hotel=True)
            user.save()
            request.session['username'] = email
            request.session.set_expiry(0)
            response_data = {'login' : "Success"}
    else:
        first_name = last_name = email = checkpassword = password = h = ''
        response_data = {'login': 'Failed'}
    return JsonResponse(response_data)