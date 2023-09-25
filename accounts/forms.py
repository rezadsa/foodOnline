from .models import User
from django import forms


class UserRegisterationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields=['first_name', 'last_name', 'username', 'email', 'password']

              
   

    # def clean(self):
    #     cleaned_data=super(UserRegisterationForm,self).clean()

    #     password=cleaned_data.get('password')
    #     confirm_password=cleaned_data.get('confirm_passwrord')
    #     print(password)
    #     print(confirm_password)
        
    #     if password != confirm_password:
    #        raise forms.ValidationError('Password does\'nt match!')

        