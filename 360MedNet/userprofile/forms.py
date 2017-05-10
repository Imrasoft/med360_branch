from django import forms
from django.contrib.auth.models import User
from userprofile.models import Doctor, SocialSite
from material import *


class VerifyForm(forms.Form):
    registration_number = forms.CharField(required=False)
    surname = forms.CharField(required=False)
    other_name = forms.CharField(required=False)

    layout = Layout(Row('registration_number', 'surname', 'other_name'))


# class RegistrationForm(forms.Form):
#     username = forms.CharField()
#     email = forms.EmailField(label="Email Address")
#     password = forms.CharField(widget=forms.PasswordInput)
#     password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password")
#     first_name = forms.CharField(required=False)
#     last_name = forms.CharField(required=False)
#     gender = forms.ChoiceField(choices=((None, ''), ('F', 'Female'), ('M', 'Male'), ('O', 'Other')))
#     receive_news = forms.BooleanField(required=False, label='I want to receive news and special offers')
#     agree_toc = forms.BooleanField(required=True, label='I agree with the Terms and Conditions')
#
#     layout = Layout('username', 'email',
#                     Row('password', 'password_confirm'),
#                     Fieldset('Pesonal details',
#                              Row('first_name', 'last_name'),
#                              'gender', 'receive_news', 'agree_toc'))


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(help_text=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('first_name', 'last_name', 'qualification', 'profession', 'specialization', 'country')


class SocialSiteForm(forms.ModelForm):
    class Meta:
        model = SocialSite
        fields = ('doctor', 'social_site', 'username')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('first_name', 'middle_name', 'last_name', 'gender', 'date_of_birth', 'qualification', 'profession',
                  'specialization', 'country', 'city', 'year_of_first_medical_certification', 'mobile_number',
                  'about_me', 'hospital', 'work_number', 'avatar')
