import django_filters
from appointments.models import Appointment

class AppointmentFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="created_date", lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name="created_date", lookup_expr='lte')

    class Meta:
        model = Appointment
        fields = ['start_date', 'end_date']