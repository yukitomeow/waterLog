from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseForbidden
from water.models import WaterConsumption
from django.contrib.auth.decorators import login_required
from water.forms import WaterConsumptionForm
from django.db.models import Sum
from django.contrib.auth.models import User
from datetime import date

@login_required
def top(request, username ):
    # waters=WaterConsumption.objects.filter(user__username=username) #filter by the user
    # context= {"waters":waters}
    
    # username = "username_here"  # Replace with actual username
    today = date.today() # Replace with actual date

# Retrieve the user
    user = User.objects.get(username=username)

# Calculate the total water consumed by the user on a specific date
    water_consumption = WaterConsumption.objects.filter(user=user, date=today).aggregate(total_water_drank=Sum('amount_drank'))
    total_water = water_consumption.get('total_water_drank') or 0  # Assign 0 if None

    if total_water > 0:
        context = {
            "water_consumption": water_consumption,
            "username": username,
            "date": today,
        }
        return render(request, "water/top.html", context)
    else:
        # Redirect to 'drink_more' view if total_water_drank is not greater than 0
        return redirect('top_new')


@login_required
def top_new(request):
    if request.method == "POST":
        form = WaterConsumptionForm(request.POST)
        if form.is_valid():
            water = form.save(commit=False)
            water.user = request.user  # Associate the current user with the WaterConsumption object
            water.save()
            return redirect("top", username=request.user.username)  # Redirect to the user's top view

    else:
        form = WaterConsumptionForm()
    return render(request, "water/top_new.html", {"form": form})   



@login_required
def edit_water_consumption(request, water_id):
    # 既存のWaterConsumptionオブジェクトを取得する
    water = get_object_or_404(WaterConsumption, id=water_id)

    # リクエストのユーザーがオブジェクトの所有者でない場合は、エラーページを表示するなどの処理を追加できます
    if water.user != request.user:
        return HttpResponseForbidden("You don't have permission to edit this.")

    # POSTリクエストの場合、データを保存する
    if request.method == "POST":
        form = WaterConsumptionForm(request.POST, instance=water)
        if form.is_valid():
            form.save()
            return redirect("top", username=request.user.username)  # 編集後のリダイレクト先を指定

    # GETリクエストの場合、既存のデータでフォームを表示する
    else:
        form = WaterConsumptionForm(instance=water)

    return render(request, "water/edit_water_consumption.html", {"form": form})


