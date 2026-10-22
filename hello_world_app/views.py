from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import MaintenanceForm
from .models import Maintenance

def home(request):
    records = Maintenance.objects.all().order_by('-date')

    # serch saved maintenance
    search = request.GET.get('search', '')

    if search:
        records = records.filter(
            Q(service__icontains=search) | Q(notes__icontains=search)
        )

    # save a new maintenance record
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MaintenanceForm()

    return render(request, 'home.html', {
        'form': form,
        'records': records
    })

