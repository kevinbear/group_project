from django import forms
from restaurant.models import CustomUser, UserProfile

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    
    # Custom validation to check if password and confirm password match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
        
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise forms.ValidationError("Email does not exist.")
        return email

class PaymentForm(forms.Form):
    card_number = forms.CharField(max_length=19, label="Card Number")
    card_name = forms.CharField(max_length=100, label="Name on Card")
    expiry_date = forms.CharField(max_length=5, label="Expiry Date")

    def clean_card_number(self):
        data = self.cleaned_data['card_number'].replace(" ", "")
        if not data.isdigit() or len(data) != 16:
            raise forms.ValidationError("Card number must be 16 digits.")
        return data

    def clean_expiry_date(self):
        data = self.cleaned_data['expiry_date']
        if not data or len(data) != 5 or '/' not in data:
            raise forms.ValidationError("Expiry must be in MM/YY format.")
        return data
    
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address', 'date_of_birth', 'profile_picture']  # or any fields from UserProfile