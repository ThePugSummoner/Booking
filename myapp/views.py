from django.shortcuts import render
from .forms import MenuForm, BookingForm
from .models import Menu, Booking
from django.http import JsonResponse, HttpResponse
from datetime import datetime
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
import logging

# Create your views here.

def form_view(request):
    if (request.method == 'POST'):
        form = MenuForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            mf = Menu(
                item_name = cd['item_name'],
                category = cd['category'],
                description = cd['description'],

            )
            mf.save()
            return JsonResponse({'message':'success'})
        return JsonResponse({'message': 'error', 'errors': form.errors})
    else:
        form = MenuForm
        return render(request, 'menu_items.html', {'form':form})
    
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def reservations(request):
  
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html', {"bookings": booking_json})
    #return JsonResponse({'bookings':booking_json}, safe=False)
    #return HttpResponse(booking_json, content_type='application/json')
  
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

@csrf_exempt
def bookings(request):
    if (request.method == 'POST'):
        data = json.load(request)
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if exist == False:
            booking = Booking(
                first_name = data['first_name'],
                reservation_date = data['reservation_date'],
                reservation_slot = data['reservation_slot'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)
    return HttpResponse(booking_json, content_type='application/json')
    

        
