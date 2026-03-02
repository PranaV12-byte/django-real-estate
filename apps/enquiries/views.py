from django.conf import settings
from django.core.mail import send_mail
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Enquiry


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def send_enquiry_email(request):
    data = request.data

    try:
        subject = data.get('subject')
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.DEFAULT_FROM_EMAIL]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        enquiry = Enquiry(name=name, email=email, subject=subject, message=message)
        enquiry.save()

        return Response({"success": 'Your Enquiry was successfully submitted'})

    except Exception as e:
        return Response({"fail": f"Enquiry was not sent. Error: {str(e)}"})

    
