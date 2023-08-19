from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from water.models import WaterConsumption
from accounts.models import UserProfile
from water.forms import WaterConsumptionForm
from django.db.models import Sum
from datetime import date
from django.http import HttpResponseForbidden
from collections import defaultdict
from calendar import monthrange
from django.utils.translation import gettext as _
from django.utils import translation
from django.contrib import messages




@login_required
def top(request, ):
   
    username = request.user.username
    # Ensure the logged-in user can only see their records
    if request.user.username != username:
        return HttpResponseForbidden("You don't have permission to view this.")

    today = date.today()

    today_record = WaterConsumption.objects.filter(user=request.user, date=today).first()
    today_record_id = today_record.id if today_record else None

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
    )  
    strings_to_translate = [
        "Water Consumption Log",
        "Water Consumption for Today", 
        "Username", 
        "Date",
        "Total Water Consumed Today",
        "Add More Water Consumption",
        "Add Water Consumption",
        ]
    for string in strings_to_translate:
        translated_string = _(string)
        messages.add_message(request, messages.SUCCESS, translated_string)

    context = {
        "total_water_today": water_today,
        "username": username,
        "date": today,
        "form": form,
        "unit":unit,
        "record_id": today_record_id,
    }

    return render(request, "water/top.html", context)


@login_required
def dashboard(request):
  
    username = request.user.username
    current_month = date.today().month
    current_month_abbr = date.today().strftime('%b')
    current_year = date.today().year
    user_water_records = WaterConsumption.objects.filter(user=request.user, date__month=current_month)
    userprofile = UserProfile.objects.filter(user=request.user).first()
    unit = userprofile.unit if userprofile and userprofile.unit else 'ml'
    # Create a dictionary to hold the total consumption for each day of the month.
    daily_consumption = defaultdict(float)
    for record in user_water_records:
        daily_consumption[record.date.day] += record.amount_drank

    total_consumption = sum(daily_consumption.values())
    days_in_month = monthrange(current_year, current_month)[1]
    average_consumption_per_day = round(total_consumption / days_in_month)
    
    context = {
        "username":username,
        'current_month_abbr':current_month_abbr,
        'daily_consumption': sorted(daily_consumption.items()),
        'unit':unit,
        'current_year':current_year,
        'average_consumption_per_day':average_consumption_per_day,
    }
    return render(request, 'water/dashboard.html', context)


