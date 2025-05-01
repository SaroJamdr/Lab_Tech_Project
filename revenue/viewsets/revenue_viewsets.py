from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, F
from django.db.models.functions import TruncMonth
from django_filters.rest_framework import DjangoFilterBackend
from appointments.models import Appointment
from ..utilities.filters import AppointmentFilter
from ..serializers.revenue_serializer import RevenueChartSerializer

class RevenueViewSet(viewsets.ViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = AppointmentFilter

    @action(detail=False, methods=['get'])
    def chart(self, request):
        queryset = self.filter_queryset(Appointment.objects.all())

        # Group by month and aggregate the revenue
        monthly_revenue = (
            queryset
            .annotate(month=TruncMonth('created_date'))
            .values('month')
            .annotate(total=Sum(F('service__price')))
            .order_by('month')
        )

        # Prepare the response data
        data = {
            'Date': [entry['month'].strftime('%b %Y') for entry in monthly_revenue],
            'values': [entry['total'] for entry in monthly_revenue],
        }

        # Return the data using the custom serializer
        serializer = RevenueChartSerializer(data)
        return Response(serializer.data)
