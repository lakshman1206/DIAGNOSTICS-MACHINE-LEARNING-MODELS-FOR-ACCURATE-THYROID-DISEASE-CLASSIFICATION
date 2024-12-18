from django.shortcuts import render, redirect
from . models import UserPersonalModel
from . forms import UserPersonalForm, UserRegisterForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import numpy as np
import joblib


def Landing_1(request):
    return render(request, '1_landing.html')

def Register_2(request):
    form = UserRegisterForm()
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('Login_3')

    context = {'form':form}
    return render(request, '2_Register.html', context)


def Login_3(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home_4')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'3_Login.html', context)

def Home_4(request):
    return render(request, '4_Home.html')

def Teamates_5(request):
    return render(request,'5_Teamates.html')

def Domain_Result_6(request):
    return render(request,'6_Domain_Result.html')

def Problem_Statement_7(request):
    return render(request,'7_Problem_Statement.html')
    

def Per_Info_8(request):
    if request.method == 'POST':
        fieldss = ['firstname','lastname','age','address','phone','city','state','country']
        form = UserPersonalForm(request.POST)
        if form.is_valid():
            print('Saving data in Form')
            form.save()
        return render(request, '4_Home.html', {'form':form})
    else:
        print('Else working')
        form = UserPersonalForm(request.POST)    
        return render(request, '8_Per_Info.html', {'form':form})
    
Model = joblib.load('C:/Users/laksh/Videos/last code/ITPML31 - FINAL CODING/DEPLOYMENT/APP/THYROID1.pkl')


    
from . models import UserPredictModel
from .forms import UserPredictDataForm
def Deploy_9(request):
    if request.method == 'POST':
        fields = ['Age', 'Gender', 'Smoking', 'Hx_Smoking', 'Hx_Radiothreapy',
       'Thyroid_Function', 'Physical_Examination', 'Adenopathy', 'Pathology',
       'Focality', 'Response', 'Recurred']
        
        form = UserPredictDataForm(request.POST)
        features = []
        for i in fields:
            info = float(request.POST[i])
            features.append(info)
           
        Final_features = [np.array(features, dtype=int)]
        
        prediction = Model.predict(Final_features)
        actual_output = prediction[0]
        print(actual_output)

        if actual_output == 0:
            actual_output = 'THE NONE OF DISEASE MIGHT OCCUR IN THESE CONDITION'
            
        elif actual_output == 1:
            actual_output = 'THE EUTHYROIDISM OF THYROID DISEASE MIGHT OCCUR IN THESE CONDITION'
            
        elif actual_output == 2:
            actual_output = 'THE  HYPOTHYROIDISM OF THYROID DISEASE MIGHT OCCUR IN THESE CONDITION'
            
        elif actual_output == 3:
            actual_output = 'THE HYPERTHYROIDISM OF THYROID DISEASE MIGHT OCCUR IN THESE CONDITION'
            
        elif actual_output == 4:
            actual_output = 'THE  THYRIOD NODULES  OF THYROID DISEASE MIGHT OCCUR IN THESE CONDITION'
            
        
            
        
        
        
        print(features)
        print(actual_output)
        if form.is_valid():
            print('Saving data in Form')
            form_instance = form.save()  # Save form data but don't commit to DB yet
            form_instance.save()
        data = UserPredictModel.objects.latest('id')
        data.Stage = actual_output
        data.save()
        return render(request, 'output.html', {'form':form, 'prediction_text':actual_output})
    else:
        print('Else working')
        form = UserPredictDataForm(request.POST)    
    return render(request, '9_Deploy.html', {'form':form})

def database(request):
    data = UserPredictModel.objects.all()
    return render(request, 'database.html', {'data': data})

def Per_Database_10(request):
    models = UserPersonalModel.objects.all()
    return render(request, '10_Per_Database.html', {'models':models})

def Logout(request):
    logout(request)
    return redirect('Login_3')
