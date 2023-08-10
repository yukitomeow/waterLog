from django.shortcuts import render, redirect
from .forms import MetricSystemForm
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required


def set_metric_preference(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = MetricSystemForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("wherever_you_want")  # Maybe the user's dashboard?
    else:
        form = MetricSystemForm(instance=profile)

    return render(request, "set_metric_preference.html", {"form": form})


@login_required
def redirect_to_user_profile(request):
    # Redirect to the logged in user's profile page
    return redirect(f"/{request.user.username}/")
