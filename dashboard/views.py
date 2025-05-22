from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from appointments.models import Appointment
from inquiries.models import Inquiry
from services.models import Service
from categories.models import Category
from django.contrib.auth.decorators import login_required


@login_required
def admin_view(request):
    admin_name = request.user.get_full_name() or request.user.username
    admin_email = request.user.email
    context = {
        'admin_name': admin_name,
        'admin_email': admin_email,
    }
    return render(request, 'sidebar.html', context)


@login_required
def dashboard_view(request):
    inquiries = Inquiry.objects.all().order_by('-created_at')
    
    offline_appointments = Appointment.objects.filter(payment_method='ofline')
    online_appointments = Appointment.objects.filter(payment_method='online')
    return render(request, 'dashboard.html', {
        'offline_appointments': offline_appointments,
        'online_appointments': online_appointments,
         'inquiries': inquiries
    })

def appointment_view(request):
    appointments= Appointment.objects.all()
    return render(request, 'appointment.html', {
        'appointments': appointments
    })


def group_list(request):
    groups= Category.objects.all().order_by('-created_date')
    return render(request, 'group.html', {'groups': groups})
