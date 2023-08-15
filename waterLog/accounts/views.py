from django.shortcuts import render, redirect
from .forms import RegistrationForm
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required


from django.contrib.auth import authenticate, login






@login_required
def redirect_to_user_profile(request):
    # Redirect to the logged in user's profile page
    return redirect(f"/{request.user.username}/")



def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create UserProfile and link it to the user
            profile = UserProfile(user=user, unit=form.cleaned_data['unit'])
            profile.save()

            # Log the user in
            authenticated_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if authenticated_user is not None:
                login(request, authenticated_user)
                # Redirect to a success page, for instance the homepage or user's dashboard
                return redirect('top')

    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/registration.html', context)

