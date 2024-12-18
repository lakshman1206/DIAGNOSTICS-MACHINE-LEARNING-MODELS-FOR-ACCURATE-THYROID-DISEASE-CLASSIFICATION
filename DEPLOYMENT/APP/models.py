from django.db import models
from django.contrib.auth.models import User


class UserPersonalModel(models.Model):


    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField(null=True, blank=True)   
    phone = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


def __str__(self):
    return self.firstname, self.lastname, self.age,self.address,self.phone,self.city,self.state,self.country

class UserPredictModel(models.Model):
    Age = models.IntegerField()
    Gender = models.CharField(max_length=100)
    Smoking = models.FloatField()
    Hx_Smoking = models.FloatField()
    Hx_Radiothreapy = models.FloatField()
    Thyroid_Function = models.FloatField()
    Physical_Examination = models.FloatField()
    Adenopathy = models.FloatField()
    Pathology = models.FloatField()
    Focality = models.FloatField()
    Stage = models.CharField(max_length=100)
    Response = models.FloatField()
    Recurred = models.FloatField()
    

    def __str__(self):
        return f"Prediction: {self.Stage}"
    