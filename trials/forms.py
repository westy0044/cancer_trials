from xml.dom.minidom import Attr
from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo, trial, cancerTypes

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        # check fields may want additional info first name and last name
        fields = ('username', 'first_name', 'last_name', 'email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('phone_number',)

class trialForm(forms.ModelForm):
    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta():
        model = trial
        fields = '__all__'
       
        widgets = {            
            'name': forms.Textarea(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class updateForm(forms.ModelForm):

    class Meta():
        model = trial
        fields = '__all__'


class selectedTrialForm(forms.ModelForm):
    email = forms.EmailField()
    contact = forms.CharField()
    
    class Meta():
        model = trial
        exclude = ('Trial_ended',)

class searchForm(forms.ModelForm):

    class Meta():
        model = trial       
        fields = ('body_region', 'Trial_ended')   

class searchForm1(forms.ModelForm):

    class Meta():
        model = trial       
        fields = ('body_region', 'Trial_ended')
    # overriding the default init method, and setting the queryset of the cancer_type field 
    # to an empty list of cancer types
    # https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['cancer_type'].queryset = cancerTypes.objects.none()

        