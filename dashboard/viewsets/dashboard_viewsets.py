from rest_framework.views import APIView
from rest_framework.response import Response
from services.serializers.service_serializer import ServiceSerializer
from services.models import Service
from inquiries.models import Inquiry
from inquiries.serializers.inquiries_serializer import InquirySerializer
from appointments.models import Appointment
from appointments.serializers.appointment_serializer import AppointmentListSerializer
from rest_framework.permissions import IsAdminUser

class DashboardView(APIView):
    parser_classes= [IsAdminUser,]
    def get(self, request):
        services = Service.objects.all()
        appointment = Appointment.objects.all()
        inquiry = Inquiry.objects.all()

        service_data = ServiceSerializer(services, many=True).data
        appointment_data = AppointmentListSerializer(appointment, many=True).data
        inquiry_data = InquirySerializer(inquiry, many=True).data
        

        return Response({
            'services': service_data,
            'appointments': appointment_data,
            'inquiry_data': inquiry_data,
        })
