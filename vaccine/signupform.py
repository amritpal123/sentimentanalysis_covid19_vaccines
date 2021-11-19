from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    YEARS= [x for x in range(1980,2021)]


    birth_date = forms.DateField(initial="2020-02-28",widget=forms.SelectDateWidget(years=YEARS),help_text='Required. Format: YYYY-MM-DD')

    SEX = (
    ('M','Male'),
    ('F','Female'),
    ('U','Unsure'),
    )
    sex = forms.ChoiceField(choices= SEX)

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','birth_date','sex','email', 'password1', 'password2')
