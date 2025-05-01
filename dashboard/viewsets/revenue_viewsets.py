from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from appointments.models import Appointment

class RevenueChartAPIView(APIView):
    def get(self, request):
        bookings = Appointment.objects.all()
        revenue_by_month = {}

        for booking in bookings:
            month = booking.created_date.strftime('%b %Y')
            revenue_by_month.setdefault(month, 0)
            revenue_by_month[month] += booking.total_price

        data = {
            'Date': list(revenue_by_month.keys()),
            'values': list(revenue_by_month.values())
        }
        return Response(data)