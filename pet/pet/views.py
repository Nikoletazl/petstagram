from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView

from pet.common.view_mixins import RedirectToDashboard
from pet.pet.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, CreatePetForm, EditPetForm, \
    DeletePetForm, AddPetPhoto
from pet.pet.models import Profile, PetPhoto, Pet


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]


class HomeView(RedirectToDashboard, TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['hide_additional_nav_items'] = True
        return context


class DashboardView(ListView):
    model = PetPhoto
    template_name = 'dashboard.html'
    context_object_name = 'pet_photos'


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pets = list(Pet.objects.filter(user_id=self.object.user_id))

        pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()

        total_likes_count = sum(pp.likes for pp in pet_photos)
        total_pet_photos_count = len(pet_photos)

        context.update({
            'total_likes_count': total_likes_count,
            'total_pet_photos_count': total_pet_photos_count,
            'is_owner': self.object.user_id == self.request.user_id,
            'pets': pets,
        })

        return context


class PetPhotoDetailsView(LoginRequiredMixin, DetailView):
    model = PetPhoto
    template_name = 'photo_details.html'
    context_object_name = 'pet_photo'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('tagged_pets')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.object.user == self.request.user

        return context


class CreatePetPhotoView(LoginRequiredMixin, CreateView):
    model = PetPhoto
    template_name = 'photo_create.html'
    fields = ('photo', 'description', 'tagged_pets')

    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditPetPhotoView(UpdateView):
    model = PetPhoto
    template_name = 'photo_edit.html'
    fields = ('description',)

    def get_success_url(self):
        return reverse_lazy('photo details', kwargs={'pk': self.object.id})


class CreatePetView(CreateView):
    template_name = 'pet_create.html'
    form_class = CreatePetForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditPetView(UpdateView):
    template_name = 'pet_edit.html'
    form_class = EditPetForm


class DeletePetView(DeleteView):
    template_name = 'pet_delete.html'
    form_class = DeletePetForm
