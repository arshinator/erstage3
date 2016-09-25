from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from django.template.defaultfilters import slugify


# Create your views here.
@login_required()
def settings(request):

    if hasattr(request.user, 'profile'):
        profiles = Profile.objects.all()
        return render(request, 'settings.html', {'profiles': profiles, })
    else:
        return render(request, 'settings1.html')


@login_required
def profile_detail(request, slug):

    if hasattr(request.user, 'profile'):
        # grab the object
        profile = Profile.objects.get(slug=slug)
        if profile.user != request.user:
            raise Http404
        return render(request, 'profiles/profile_detail.html', {'profile': profile, })
    else:
        return render(request, 'settings1.html')


@login_required
def edit_profile(request, slug):
    # grab the object
    profile = Profile.objects.get(slug=slug)

    if profile.user != request.user:
        raise Http404
    # set the form we are using
    form_class = ProfileForm

    # if we're coming to this view from a sbmitted form
    if request.method == 'POST':
        # grab the data from the submitted form and apply to the form
        form = form_class(data=request.POST, instance=profile)
        if form.is_valid():
            # save the new data
            form.save()
            messages.success(request, 'Profile is Updated.')
            return redirect('profile_detail', slug=profile.slug)
            # otherwise just create the form
    else:
        form = form_class(instance=profile)

        # and render the template
        return render(request, 'profiles/edit_profile.html', {'profile': profile, 'form': form, })

@login_required
def create_profile(request):

    if hasattr(request.user, 'profile'):
        profiles = Profile.objects.all()
        return render(request, 'settings.html', {'profiles': profiles, })
    else:
        form_class = ProfileForm
        # if we're coming from a submitted form, do this
        if request.method == 'POST':
            # grab the data from the submitted form and apply to the form
            form = form_class(request.POST)

            if form.is_valid():

                # create an instance but dont save yet
                profile = form.save(commit=False)
                # set the additional details
                profile.user = request.user
                profile.slug = slugify(profile.pan)

                # save the object
                profile.save()
                messages.success(request, 'Profile Created.')
                # redirect to our newly created profile
                return redirect('profile_detail', slug=profile.slug)

                # otherwise just create the form
        else:
            form = form_class()

        return render(request, 'profiles/create_profile.html', {'form': form, })
