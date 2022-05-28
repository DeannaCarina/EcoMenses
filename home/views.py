from django.shortcuts import render
from django.core import mail
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.contrib import messages

# Create your views here.

def index(request):
    """ A view to render the home page """
    return render(request, 'home/index.html')

def contact(request):
    """ A view to render the home page """

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and message:
            try:
                send_mail(
                    subject=f"New message from {name} via EcoMenses",
                    message=f"Subject: {subject}\n\nMessage: {message}\n\nPlease contact {name} on {email}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER])
                send_mail(
                    subject=f"New message from EcoMenses",
                    message=f"You sent a message to EcoMenses, we aim to respond within 24 hours. Here is what you sent:\n\nSubject: {subject}\n\nMessage: {message}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('thanks')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

    return render(request, 'home/contact.html')