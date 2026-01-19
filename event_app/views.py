from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import signupData
from .models import feedbackData
from .models import BookingData
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date
from django.conf import settings

# Create your views here.


def generate_invoice(booking):
    # Create a HttpResponse with PDF content type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="Invoice_{booking.id}.pdf"'

    # Create PDF
    pdf = canvas.Canvas(response)
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, 800, "AUROO EVENTS INVOICE")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 750, f"Booking ID: {booking.id}")
    pdf.drawString(50, 730, f"Name: {booking.name}")
    pdf.drawString(50, 710, f"Email: {booking.email}")
    pdf.drawString(50, 690, f"Event Type: {booking.event_type}")
    pdf.drawString(50, 670, f"Date: {booking.date}")
    pdf.drawString(50, 650, f"Guests (Total Count (approx)): {booking.guestsc}")
    pdf.drawString(50, 630, f"Guests (Veg Count (approx)): {booking.guestsv}")
    pdf.drawString(50, 610, f"Guests (Non-Veg Count (approx)): {booking.guestsn}")
    pdf.drawString(50, 590, f"Message: {booking.message}")

    pdf.drawString(50, 550, "Thank you for booking with AUROO EVENTS!")
    pdf.showPage()
    pdf.save()
    return response

@login_required(login_url='signup')
def feedback_Data(request):
    if request.method =='POST':
        name1=request.POST.get('name')
        email1=request.POST.get('email')
        feedback1=request.POST.get('feedback')

        obj=feedbackData()
        obj.name=name1
        obj.email=email1
        obj.feedback=feedback1
        data = feedbackData(name=name1, email=email1, feedback=feedback1)
        data.save()
        messages.success(request," THANK YOU, Your FeedBack Submitted Successfully.")
        return redirect('feed')
    return redirect('feed')



def signup(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        # contact=request.POST.get('contact')
        psw=request.POST.get('psw')
        rpsw=request.POST.get('rpsw')
        
        #new
        if User.objects.filter(email=email).exists():
            messages.error(request, "User with this email already exists. Please signin.")
            return redirect('signup')

        if psw!=rpsw:
            messages.error(request,"Password not matched.")
            return redirect('signup')
        
        # user=User.objects.create(
        #     email=email,
        #     password=psw,
        #     first_name=name
        
        # )
        user=User.objects.create_user(username=email,email=email,password=psw,first_name=name)
        user.set_password(psw)
        user.save()
        
        
        
        # obj=signupData()
        # obj.name=name
        # obj.email=email
        # obj.contact=contact 
        # obj.psw=make_password(psw)
        # obj.save()

        messages.success(request,"Sign-up Successfull")
        return redirect('signin')
    return render(request,'signup.html')



def signin(request):
    if request.method == 'POST':
        emailn = request.POST.get('email')
        passwordn = request.POST.get('psw')

        # authenticate expects username, so we pass username=email
        user = authenticate(username=emailn, password=passwordn)
        if user is None:
            messages.error(request, "Invalid email or password")
            return redirect('signin')

        login(request, user)
        return redirect('home')

    return render(request, 'index.html')


# def signin(request):
#     if request.method == 'POST':
#         emailn=request.POST.get('email')
#         passwordn=request.POST.get('psw')
        
#         user = authenticate(email=emailn , password=passwordn)
#         if not User.objects.filter(email=emailn,password=passwordn).exists():
#             messages.error(request,"invalid user")
#             return redirect('signin')
#         else:
#             login(request,user)
#             return  redirect('home')
        
        
        
#     return render(request, 'signin.html')

    #     try:
    #         user_obj = signupData.objects.get(email=emailn)
    #         if check_password(password, user_obj.psw):  
    #             messages.success(request, "signin successful!")
    #             # return render(request,'booking.html')
    #             return render(request,'home.html')
    #         else:
    #             messages.error(request, "Invalid password. Please try again.")
    #     except signupData.DoesNotExist:
    #         messages.error(request, "User does not exist. Please sign up first.")
    # return render(request, 'signin.html')
@login_required(login_url='signup')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='signup')
def home(request):
    return render(request,'home.html')

# def events(request):
#     return render(request,'events.html')

@login_required(login_url='signup')
def booking(request):
    return render(request,'booking.html')

@login_required(login_url='signup')
def booking1(request):
    return render(request,'booking1.html')

@login_required(login_url='signup')
def booking2(request):
    return render(request,'booking2.html')

@login_required(login_url='signup')
def booking3(request):
    return render(request,'booking3.html')

@login_required(login_url='signup')
def booking4(request):
    return render(request,'booking4.html')

@login_required(login_url='signup')
def booking5(request):
    return render(request,'booking5.html')

@login_required(login_url='signup')
def booking6(request):
    return render(request,'booking6.html')

@login_required(login_url='signup')
def booking7(request):
    return render(request,'booking7.html')

@login_required(login_url='signup')
def feed(request):
    return render(request,'feed.html')

@login_required(login_url='signup')
def myrgs(request):
    return render(request,'myrgs.html')

@login_required(login_url='signup')
def contact(request):
    return render(request,'contact.html')

@login_required(login_url='signup')
def book_event(request):
    return render(request, 'book_event.html')

@login_required(login_url='signup')
def submit_booking(request):
    mydata=BookingData.objects.filter(user=request.user)
    if request.method == "POST":
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        event_type1 = request.POST.get('event_type')
        date1 = request.POST.get('date')
        guestsc1=request.POST.get('guestsc')
        guestsv1=request.POST.get('guestsv')
        guestsn1=request.POST.get('guestsn')
        message1 = request.POST.get('message')

        
        booking=BookingData.objects.create(user=request.user,name=name1, email=email1, event_type=event_type1, date=date1,guestsc=guestsc1,guestsv=guestsv1,guestsn=guestsn1, message=message1)

        messages.success(request, f"Thank you {name1}, your booking for {event_type1} on {date1} was submitted successfully!")
        # return redirect('home')
        return generate_invoice(booking)
        
    return redirect('booking')

@login_required(login_url='signup')
def submit_booking1(request):
    if request.method == "POST":
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        event_type1 = request.POST.get('event_type')
        date1 = request.POST.get('date')
        guestsc1=request.POST.get('guestsc')
        guestsv1=request.POST.get('guestsv')
        guestsn1=request.POST.get('guestsn')
        message1 = request.POST.get('message')

        
        booking=BookingData.objects.create(user=request.user,name=name1, email=email1, event_type=event_type1, date=date1,guestsc=guestsc1,guestsv=guestsv1,guestsn=guestsn1, message=message1)

        messages.success(request, f"Thank you {name1}, your booking for {event_type1} on {date1} was submitted successfully!")
        # return redirect('home')
        return generate_invoice(booking)
        
    return redirect('booking1')

@login_required(login_url='signup')
def submit_booking2(request):
    if request.method == "POST":
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        event_type1 = request.POST.get('event_type')
        date1 = request.POST.get('date')
        guestsc1=request.POST.get('guestsc')
        guestsv1=request.POST.get('guestsv')
        guestsn1=request.POST.get('guestsn')
        message1 = request.POST.get('message')

        
        booking=BookingData.objects.create(user=request.user,name=name1, email=email1, event_type=event_type1, date=date1,guestsc=guestsc1,guestsv=guestsv1,guestsn=guestsn1, message=message1)

        messages.success(request, f"Thank you {name1}, your booking for {event_type1} on {date1} was Registered successfully!")
        # return redirect('booking2')
        return generate_invoice(booking)
        
    return redirect('booking2')

@login_required(login_url='signup')
def submit_booking3(request):
    if request.method == "POST":
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        event_type1 = request.POST.get('event_type')
        date1 = request.POST.get('date')
        guestsc1=request.POST.get('guestsc')
        guestsv1=request.POST.get('guestsv')
        guestsn1=request.POST.get('guestsn')
        message1 = request.POST.get('message')

        
        booking=BookingData.objects.create(user=request.user,name=name1, email=email1, event_type=event_type1, date=date1,guestsc=guestsc1,guestsv=guestsv1,guestsn=guestsn1, message=message1)

        messages.success(request, f"Thank you {name1}, your booking for {event_type1} on {date1} was Registered successfully!")
        # return redirect('booking3')
        return generate_invoice(booking)
        
    return redirect('booking3')

@login_required(login_url='signup')
def submit_booking4(request):
    if request.method == "POST":
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        event_type1 = request.POST.get('event_type')
        date1 = request.POST.get('date')
        guestsc1=request.POST.get('guestsc')
        guestsv1=request.POST.get('guestsv')
        guestsn1=request.POST.get('guestsn')
        message1 = request.POST.get('message')

        
        booking=BookingData.objects.create(user=request.user,name=name1, email=email1, event_type=event_type1, date=date1,guestsc=guestsc1,guestsv=guestsv1,guestsn=guestsn1, message=message1)

        messages.success(request, f"Thank you {name1}, your booking for {event_type1} on {date1} was Registered successfully!")
        # return redirect('booking4')
        return generate_invoice(booking)
        
    return redirect('booking4')

@login_required(login_url='signup')
def submit_booking5(request):
    if request.method == "POST":
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        event_type1 = request.POST.get('event_type')
        date1 = request.POST.get('date')
        guestsc1=request.POST.get('guestsc')
        guestsv1=request.POST.get('guestsv')
        guestsn1=request.POST.get('guestsn')
        message1 = request.POST.get('message')

        
        booking=BookingData.objects.create(user=request.user,name=name1, email=email1, event_type=event_type1, date=date1,guestsc=guestsc1,guestsv=guestsv1,guestsn=guestsn1, message=message1)

        messages.success(request, f"Thank you {name1}, your booking for {event_type1} on {date1} was Registered successfully!")
        # return redirect('booking5')
        return generate_invoice(booking)
        
    return redirect('booking5')

@login_required(login_url='signup')
def submit_booking6(request):
    if request.method == "POST":
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        event_type1 = request.POST.get('event_type')
        date1 = request.POST.get('date')
        guestsc1=request.POST.get('guestsc')
        guestsv1=request.POST.get('guestsv')
        guestsn1=request.POST.get('guestsn')
        message1 = request.POST.get('message')

        
        booking=BookingData.objects.create(user=request.user,name=name1, email=email1, event_type=event_type1, date=date1,guestsc=guestsc1,guestsv=guestsv1,guestsn=guestsn1, message=message1)

        messages.success(request, f"Thank you {name1}, your booking for {event_type1} on {date1} was Registered successfully!")
        # return redirect('booking6')
        return generate_invoice(booking)
        
    return redirect('booking6')

@login_required(login_url='signup')
def submit_booking7(request):
    if request.method == "POST":
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        event_type1 = request.POST.get('event_type')
        date1 = request.POST.get('date')
        guestsc1=request.POST.get('guestsc')
        guestsv1=request.POST.get('guestsv')
        guestsn1=request.POST.get('guestsn')
        message1 = request.POST.get('message')

        
        booking=BookingData.objects.create(user=request.user,name=name1, email=email1, event_type=event_type1, date=date1,guestsc=guestsc1,guestsv=guestsv1,guestsn=guestsn1, message=message1)

        messages.success(request, f"Thank you {name1}, your booking for {event_type1} on {date1} was Registered successfully!")
        # return redirect('booking7')
        return generate_invoice(booking)
        
    return redirect('booking7')



    
@login_required(login_url='signup')
def my_registrations(request):
    if not request.user.is_authenticated:
        return render(request, 'signup.html')
    
    today = date.today()

    # Only user's bookings
    user_bookings = BookingData.objects.filter(user=request.user)

    # Upcoming / Not completed
    upcoming = user_bookings.filter(date__gte=today)

    # Completed Events
    completed = user_bookings.filter(date__lt=today)

    return render(request, 'myrgs.html', {
        'upcoming': upcoming,
        'completed': completed
    })


# @login_required
# def my_registrations(request):
#     bookings = BookingData.objects.filter(user=request.user)
#     return render(request, 'myrgs.html', {'bookings': bookings})

# def my_registrations(request):
#     bookings = BookingData.objects.all()

#     return render(request, 'myrgs.html', {'bookings': bookings})

@login_required(login_url='signup')
def deleteData(request,id):
    if request.method == "POST":
        mydata=BookingData.objects.get(id=id)
        mydata.delete()
    return redirect('myrgs')


@login_required(login_url='signup')
def updateData(request, id):
    mydata = BookingData.objects.get(id=id)
    if request.method == 'POST':
        name1 = request.POST['name']
        email1 = request.POST['email']
        event_type1 = request.POST['event_type']
        date1 = request.POST['date']
        guestsc1 = request.POST['guestsc']
        guestsv1 = request.POST['guestsv']
        guestsn1 = request.POST['guestsn']
        message1 = request.POST['message']

        mydata.name = name1
        mydata.email = email1
        mydata.event_type =event_type1
        mydata.date = date1
        mydata.guestsc =guestsc1
        mydata.guestsv =guestsv1
        mydata.guestsn =guestsn1
        mydata.message =message1

        mydata.save()
        return redirect('myrgs')
    return render(request, 'update.html', {'data': mydata})

@login_required(login_url='signup')
def signout(request):
    logout(request)
    return redirect('signup')
