from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from water.models import WaterConsumption
from accounts.models import UserProfile
from water.forms import WaterConsumptionForm
from django.db.models import Sum
from datetime import date
from django.http import HttpResponseForbidden
from collections import defaultdict


@login_required
def top(request):
    print(request)  # This will print a summary
    print(
        request.user.__dict__
    )  # This will print the full dictionary representation of the request object
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

    userprofile = UserProfile.objects.filter(user=request.user).first()
    unit = userprofile.unit if userprofile and userprofile.unit else 'ml'
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
        "unit":unit,
    }

    return render(request, "water/top.html", context)

@login_required
def dashboard(request):
    current_month = date.today().month
    user_water_records = WaterConsumption.objects.filter(user=request.user, date__month=current_month)
    
    # Create a dictionary to hold the total consumption for each day of the month.
    daily_consumption = defaultdict(float)
    for record in user_water_records:
        daily_consumption[record.date.day] += record.amount_drank
    
    context = {
        'daily_consumption': sorted(daily_consumption.items())
    }
    return render(request, 'dashboard.html', context)


@login_required
def dashboard(request):
    current_month = date.today().month
    user_water_records = WaterConsumption.objects.filter(user=request.user, date__month=current_month)
    userprofile = UserProfile.objects.filter(user=request.user).first()
    unit = userprofile.unit if userprofile and userprofile.unit else 'ml'
    # Create a dictionary to hold the total consumption for each day of the month.
    daily_consumption = defaultdict(float)
    for record in user_water_records:
        daily_consumption[record.date.day] += record.amount_drank
    
    context = {
        'daily_consumption': sorted(daily_consumption.items()),
        'unit':unit
    }
    return render(request, 'water/dashboard.html', context)