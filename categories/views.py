
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForm

def category_list(request):
    categories = Category.objects.all().order_by('-created_date')
    return render(request, 'category.html', {'categories': categories})



def create_category_view(requrest):
    if requrest.method == 'POST':
        form = CategoryForm(requrest.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_list')
    else:
        form = CategoryForm()
    categories = Category.objects.all()
    return render(requrest, 'create_category.html', {'form': form, 'categories': categories})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.title = request.POST.get("category")
        category.description = request.POST.get("parent")
        category.save()
        return redirect('category_list')  # make sure this matches your URL name
    return redirect('category_list')  # fallback

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect('category_list')
