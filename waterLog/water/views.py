from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from water.models import WaterConsumption
from water.forms import WaterConsumptionForm
from django.db.models import Sum
from datetime import date
from django.http import HttpResponseForbidden


@login_required
def top(request):
    username = request.user.username
    # Ensure the logged-in user can only see their records
    if request.user.username != username:
        return HttpResponseForbidden("You don't have permission to view this.")

    today = date.today()

    # Retrieve today's total water consumption for the user
    water_today = (
        WaterConsumption.objects.filter(user=request.user, date=today).aggregate(
            total=Sum("amount_drank")
        )["total"]
        or 0
    )

    if request.method == "POST":
        form = WaterConsumptionForm(request.POST)
        if form.is_valid():
            water = form.save(commit=False)
            water.user = request.user
            water.date = today  # set today's date
            water.save()

            # Recalculate the water consumed today after saving the new record
            water_today = (
                WaterConsumption.objects.filter(
                    user=request.user, date=today
                ).aggregate(total=Sum("amount_drank"))["total"]
                or 0
            )

    form = (
        WaterConsumptionForm()
    )  # Always provide an empty form for adding new water consumption

    context = {
        "total_water_today": water_today,
        "username": username,
        "date": today,
        "form": form,
    }

    return render(request, "water/top.html", context)


@login_required
def top_new(request):
    today = date.today()

    # If there's a POST request, try to save the new water consumption
    if request.method == "POST":
        form = WaterConsumptionForm(request.POST)
        if form.is_valid():
            water = form.save(commit=False)
            water.user = request.user
            water.date = today  # set today's date
            water.save()
            return redirect("top", username=request.user.username)

    else:
        form = WaterConsumptionForm()

    return render(request, "water/top_new.html", {"form": form})
