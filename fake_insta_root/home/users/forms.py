from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name")

class EditProfileForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = (
            'username',
            'email',
            'first_name',
            'last_name'
        )




