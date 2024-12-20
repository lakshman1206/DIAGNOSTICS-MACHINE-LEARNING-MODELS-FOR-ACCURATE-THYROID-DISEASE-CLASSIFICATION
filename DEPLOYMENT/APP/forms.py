from django import forms 
from . models import UserPersonalModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UserPersonalForm(forms.ModelForm):
    
    class Meta:
        model = UserPersonalModel
        fields = '__all__'

from . models import UserPredictModel

class UserPredictDataForm(forms.ModelForm):
    class Meta:
        model = UserPredictModel
        fields = ['Age', 'Gender', 'Smoking', 'Hx_Smoking', 'Hx_Radiothreapy',
       'Thyroid_Function', 'Physical_Examination', 'Adenopathy', 'Pathology',
       'Focality', 'Response', 'Recurred']