from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from pet.accounts.views import UserLoginView, UserRegisterView, ChangeUserPasswordView
from pet.pet.views import ProfileDetailsView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('profile/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),

    path('edit-password/', ChangeUserPasswordView.as_view(), name='edit password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password_change_done'),

    path('create/', UserRegisterView.as_view(), name='create profile'),
    # path('profile/edit/', edit_profile, name='edit profile'),
    # path('profile/delete/', delete_profile, name='delete profile'),
)
