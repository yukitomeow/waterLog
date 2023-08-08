from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from water.models import WaterConsumption
from water.forms import WaterConsumptionForm
from django.db.models import Sum
from datetime import date
from django.http import HttpResponseForbidden

@login_required
def top(request, username):
    # Ensure the logged-in user can only see their records
    if request.user.username != username:
        return HttpResponseForbidden("You don't have permission to view this.")

    today = date.today()
    # Retrieve today's total water consumption for the user
    water_today = WaterConsumption.objects.filter(user=request.user, date=today).aggregate(total=Sum('amount_drank'))['total'] or 0

    # If no water consumed yet, redirect to the input form
    if not water_today:
        return redirect('top_new')

    context = {
        "total_water_today": water_today,
        "username": username,
        "date": today,
    }
    return render(request, "water/top.html", context)


@login_required
def top_new(request):
    today = date.today()
    
    # Check if water has already been logged for today and if yes, redirect to top view
    total_water_today = WaterConsumption.objects.filter(user=request.user, date=today).aggregate(total=Sum('amount_drank'))['total'] or 0
    if total_water_today:
        return redirect("top", username=request.user.username)

    if request.method == "POST":
        form = WaterConsumptionForm(request.POST)
        if form.is_valid():
            water = form.save(commit=False)
            water.user = request.user
            water.save()
            return redirect("top", username=request.user.username)

    else:
        form = WaterConsumptionForm()

    return render(request, "water/top_new.html", {"form": form})


@login_required
def edit_water_consumption(request, water_id):
    water_instance = get_object_or_404(WaterConsumption, id=water_id)

    # Ensure that users can only edit their records
    if water_instance.user != request.user:
        return HttpResponseForbidden("You don't have permission to edit this.")

    if request.method == "POST":
        form = WaterConsumptionForm(request.POST, instance=water_instance)
        if form.is_valid():
            form.save()
            return redirect("top", username=request.user.username)

    else:
        form = WaterConsumptionForm(instance=water_instance)

    return render(request, "water/edit_water_consumption.html", {"form": form})
