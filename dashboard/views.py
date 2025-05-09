from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from appointments.models import Appointment
from inquiries.models import Inquiry
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    inquiries = Inquiry.objects.all().order_by('-created_at')

    offline_appointments = Appointment.objects.filter(payment_method='offline')
    online_appointments = Appointment.objects.filter(payment_method='online')
    return render(request, 'dashboard.html', {
        'offline_appointments': offline_appointments,
        'online_appointments': online_appointments,
         'inquiries': inquiries
    })

