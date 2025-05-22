from django.shortcuts import render, redirect, get_object_or_404

from FAQs.models import FAQ
from FAQs.forms import FAQForm
# Create your views here.
def faq_list(request):
      faqs = FAQ.objects.all().order_by('-created_at')
      return render(request, 'faq.html', {'faqs': faqs})


def create_faq_view(requrest):
    if requrest.method == 'POST':
        form = FAQForm(requrest.POST)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
    else:
        form = FAQForm()

    return render(requrest, 'create_faq.html', {'form': form})

def faq_edit(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    if request.method == "POST":
        faq.title = request.POST.get("title")
        faq.description = request.POST.get("description")
        faq.save()
        return redirect('faq_list')  # make sure this matches your URL name
    return redirect('faq_list')  # fallback
def faq_delete(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    if request.method == "POST":
        faq.delete()
        return redirect('faq_list')