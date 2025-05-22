from django.shortcuts import render, redirect, get_object_or_404

from .models import Branch
from .forms import branchForm
# Create your views here.
def branch_list(request):
      branch = Branch.objects.all().order_by('-created_date')
      return render(request, 'branch.html', {'branch': branch})


def create_branch_view(requrest):
    if requrest.method == 'POST':
        form = branchForm(requrest.POST)
        if form.is_valid():
            form.save()
            return redirect('branch_list')
    else:
        form = branchForm()

    return render(requrest, 'create_branch.html', {'form': form})

def branch_edit(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    if request.method == "POST":
        branch.name = request.POST.get("name")
        branch.email = request.POST.get("email")
        branch.phone_number = request.POST.get("phone_number")
        branch.address = request.POST.get("address")
        branch.gps_location = request.POST.get("gps_location")
        branch.is_headbranch = request.POST.get("is_headbranch")
        branch.save()
        return redirect('branch_list')  # make sure this matches your URL name
    return redirect('branch_list')  # fallback
def branch_delete(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    if request.method == "POST":
        branch.delete()
        return redirect('branch_list')