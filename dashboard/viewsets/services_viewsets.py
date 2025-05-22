from services.models import Service
from django.shortcuts import render

# class ServiceCreateView(APIView):
#     def get(self, request):
#         form = ServiceForm()
#         return render(request, 'services/service_form.html', {'form': form})

#     def post(self, request):
#         form = ServiceForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('service-success')  # or list page
#         return render(request, 'services/service_form.html', {'form': form})


def service_view(request):
    services= Service.objects.all().prefetch_related('category', 'sub_category').order_by('-id')
    return render(request, 'services.html', {
        'services': services
    })



    