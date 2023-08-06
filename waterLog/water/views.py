from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from water.models import WaterConsumption
from django.contrib.auth.decorators import login_required
from water.forms import WaterConsumptionForm

@login_required
def top(request, username ):
    waters=WaterConsumption.objects.filter(user__username=username) #filter by the user
    context= {"waters":waters}
    return render(request, "water/top.html", context)

# @login_required


# def top_new(request):
#     if request.method == "POST":
#         form = WaterConsumptionForm(request.POST)
#         if form.is_valid():
#             water = form.save(commit=False)
#             water.save()
#             return redirect("water/top.html")  # Correct the redirect argument

#     else:
#         form = WaterConsumptionForm()
#     return render(request, "water/top_new.html", {"form": form})

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

