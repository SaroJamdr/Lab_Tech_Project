from django.shortcuts import render, redirect, get_object_or_404

from .models import Team
from .forms import TeamForm
# Create your views here.
def team_list(request):
      team = Team.objects.all().order_by('-created_date')
      return render(request, 'team.html', {'team': team})


def create_team_view(requrest):
    if requrest.method == 'POST':
        form = TeamForm(requrest.POST,requrest.FILES)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm()

    return render(requrest, 'create_team.html', {'form': form,})

def team_edit(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == "POST":
        team.name = request.POST.get("name")
        team.position = request.POST.get("position")
        if 'image' in request.FILES:
            team.image = request.FILES['image']
        team.save()
        return redirect('team_list')  
    return redirect('team_list')

def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == "POST":
        team.delete()
        return redirect('team_list')