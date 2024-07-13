from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    shopname = forms.CharField(max_length=20)
    icon = forms.IntegerField(min_value=1, max_value=100)  # Adjust according to the number of icons
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('shopname', 'icon')

    def clean_shopname(self):
        shopname = self.cleaned_data['shopname']
        if CustomUser.objects.filter(shopname=shopname).exists():
            raise forms.ValidationError("This shop name is already in use.")
        return shopname