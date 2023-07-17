from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class workerform(forms.ModelForm):
    class Meta:
        model = worker
        fields = '__all__'
        widgets = {
            'First_Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Middle_Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Phone' : forms.TextInput(attrs={'class':'form-control'}),
            'Gender' : forms.Select(attrs={'class':'form-control'}),
            'Id_Number' : forms.TextInput(attrs={'class':'form-control'})
        } 
class attendanceform(forms.ModelForm):
    
    class Meta:
        model = attendance
        fields = '__all__'
        widgets = {
            'name' : forms.Select(attrs={'class':'form-control'}),
            'date' : forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'presentstatus' : forms.Select(attrs={'class':'form-control'}),
            'paystatus' : forms.Select(attrs={'class':'form-control'}),
            'salary' : forms.TextInput(attrs={'class':'form-control','type':'float'})
        }  

    def clean_paystatus(self):
        presentstatus = self.cleaned_data.get('presentstatus')
        paystatus = self.cleaned_data.get('paystatus')
        print(f'{presentstatus}')
        print(f'{paystatus}')
        if presentstatus == 'Absent' and  paystatus != 'Absent':
            raise ValidationError('You cannnot be absent and excpect to be paid')
        elif presentstatus == 'Absent' and  paystatus == 'Absent':
            return paystatus
            print(paystatus) 
        elif paystatus == 'Absent' and presentstatus != 'Absent':
            raise ValidationError('incorrect credentials')
        elif paystatus == 'Absent'  and presentstatus == 'Absent':
            return presentstatus   
        else:
            return paystatus

class updateattendance(forms.ModelForm):
    class Meta:
        model = attendance
        fields = '__all__'
        widgets = {
            'name' : forms.Select(attrs={'class':'form-control'}),
            'date' : forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'presentstatus' : forms.Select(attrs={'class':'form-control'}),
            'paystatus' : forms.Select(attrs={'class':'form-control'}),
            'salary' : forms.TextInput(attrs={'class':'form-control','type':'float'})
        }  

class registrationform(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets={
            'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Username'})
        }
       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None   

    def clean_email(self):
        email = self.cleaned_data['email'] 
        if   User.objects.filter(email=email).exists():
            raise ValidationError('a user with this email already exist')
        else:
            return email         

            
              