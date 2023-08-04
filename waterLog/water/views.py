from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from water.models import WaterConsumption
from django.contrib.auth.decorators import login_required
@login_required
def top(request, ):
    
    waters=WaterConsumption.objects.all()
    context= {"waters":waters}
    return render(request, "water/top.html", context)

def top_new(request):
    return HttpResponse(b"top new")
