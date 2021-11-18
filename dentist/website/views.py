from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter 

# Create your views here.

# Generate a PDF file 
def letter_pdf(request):
    # Create Bytestream buffer
    buf = io.BytesIO()
    # Create canvas 
    canva = canvas.Canvas(buf, pagesize = letter, bottomup=0)
    # Create text object 
    textObject = canva.beginText()
    textObject.setTextOrigin(inch,inch)
    textObject.setFont("Helvetica", 14)

    # Add some lines of text  
    lines = [
        appointment()
    ]

    # Loop 
    for line in lines:
        textObject.textLine(line)

    # Finish up 
    canva.drawText(textObject)
    canva.showPage()
    canva.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='letter.pdf')

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method =='POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            'message_from' + message_name, # subject
            message, # message
            message_email,  # from email
            ['rivaldokat25@gmail.com'], # to email     
        )

        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html',{})


def about(request):
    return render(request, 'about.html', {})


def service(request):
    return render(request, 'service.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})


def appointment(request):
    if request.method =='POST':
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email= request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']

        # send an email

        
        # send_mail(
            # 'Appointment Request', # subject
            # appointment, # message
            # your_email,  # from email
            # ['rivaldokat25@gmail.com'], # to email     
        # )

        return render(request, 'appointment.html', {
            
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_schedule': your_schedule,
            'your_message': your_message,
            'your_date': your_date
        
        })

    else:
        return render(request, 'home.html',{})