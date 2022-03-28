
from django.urls import path

from pet.pet.views import HomeView, DashboardView, PetPhotoDetailsView, CreatePetPhotoView, EditPetPhotoView, \
    CreatePetView, EditPetView, DeletePetView

urlpatterns = [
    path('', HomeView.as_view(), name='home page'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('photo/details/<int:pk>/', PetPhotoDetailsView.as_view(), name='photo details'),
    path('photo/create/', CreatePetPhotoView.as_view(), name='create photo'),
    path('photo/edit/', EditPetPhotoView.as_view(), name='edit pet photo'),
    path('photo/create/', CreatePetPhotoView.as_view(), name='create photo'),



    path('pet/add/', CreatePetView.as_view(), name='create pet'),
    path('pet/edit/<int:pk>/', EditPetView.as_view(), name='edit pet'),
    path('pet/delete/<int:pk>/', DeletePetView.as_view(), name='delete pet'),

]
