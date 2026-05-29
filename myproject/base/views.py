from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    data = Flights.objects.all()
    return render(request, 'home.html', {'data': data})
def booking(request):
    data = user_tickets.objects.all()
    return render(request,'booking.html', {'data': data})
def history(request):
    data = user_tickets.objects.all()
    return render(request,'history.html', {'data': data})
def profile(request):
    return render(request,'profile.html')
def logout(request):
    return redirect('home')
def support(request):
    return render(request,'support.html')
def about(request):
    return render(request,'about.html')

def ticketbooking(request , pk):
    flight = Flights.objects.get(id = pk)
    if request.method == 'POST':
        flight_name  = request.POST['flight_name']
        flight_source = request.POST['flight_source']
        flight_dest = request.POST.get('flight_dest')
        flight_timming = request.POST['flight_timming']
        ticket_price = request.POST['ticket_price']
        date = request.POST['date']
        user_name = request.POST['user_name']
        user_age = request.POST['user_age']
        user_phone = request.POST['user_phone']
        user_email = request.POST['user_email']
        seat_class = request.POST['seat_class']

        user_tickets.objects.create(
            flight_name = flight.flight_name,
            flight_source = flight.flight_source,
            flight_dest = flight.flight_dest,
            flight_timming = flight.flight_timming,
            ticket_price = flight.ticket_price,
            date = flight.date,
            user_name = user_name,
            user_age = user_age,
            user_phone = user_phone,
            user_email = user_email,
            seat_class = seat_class
        )
        return redirect('booking')
    return render(request , 'ticketbooking.html' , {'flight' : flight})


def tupdate(request , pk):
    flight = user_tickets.objects.get(id = pk)
    if request.method == 'POST':
        new_flight_name = request.POST['flight_name']
        new_flight_source = request.POST['flight_source']
        new_flight_dest = request.POST['flight_dest']
        new_flight_timming = request.POST['flight_timming']
        new_ticket_price = request.POST['ticket_price']
        new_date = request.POST['date']
        new_user_name = request.POST['user_name']
        new_user_age = request.POST['user_age']
        new_user_phone = request.POST['user_phone']
        new_user_email = request.POST['user_email']
        new_seat_class = request.POST['seat_class']
        new_seat_number = request.POST['seat_number']
        
        flight.flight_name = new_flight_name
        flight.flight_source = new_flight_source
        flight.flight_dest =new_flight_dest
        flight.flight_timming = new_flight_timming
        flight.ticket_price = new_ticket_price
        flight.date = new_date
        flight.user_name = new_user_name
        flight.user_age = new_user_age
        flight.user_phone = new_user_phone
        flight.user_email = new_user_email
        flight.seat_class = new_seat_class
        flight.seat_number = new_seat_number
        flight.save()
        return redirect('booking')
    return render(request , 'update.html' , {'flight' : flight})

def tdelete(request , pk):
    flight = user_tickets.objects.get(id = pk)
    flight.delete()
    return redirect('booking')

def viewticket(request , pk):
    data = user_tickets.objects.get(id = pk)
    return render(request , 'viewticket.html' , {'data' : data})
