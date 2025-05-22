from django.shortcuts import render, redirect
from .forms import InquiryForm
from inquiries.models import Inquiry
# Create your views here.
def inquiry_view(request):
    inquiries = Inquiry.objects.all().order_by('-created_at')
    return render(request, 'inquiry.html', {
        'inquiries': inquiries
        })



def create_inquiry_view(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inquiries')
    else:
        form = InquiryForm()
    return render(request, 'create_inquiry.html', {'form': form})