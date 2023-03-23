from theblog.models import Profile
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.views import PasswordChangeView


class CreateProfilePageView(CreateView, User):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url']
    #form_class = EditProfileForm
    success_url = reverse_lazy('home')



class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        #users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class PasswordsChangeView(PasswordChangeView):
    form_class = PCF
    success_url = reverse_lazy('password_success')


class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

#------------------------------------------------


class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')


    def get_object(self):
        return self.request.user

