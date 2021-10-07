from django.db import models
from django.conf import settings



# Create your models here.
class Person(models.Model):  
    id = models.BigAutoField(primary_key=True)
    firstName = models.CharField (max_length=40)
    lastName = models.CharField (max_length=40)
    bday = models.DateField(null=True)
   
    def __str__(self):
       return "%s %s" % (self.lastName, self.firstName)

    class Meta:  
        db_table = "person"  

class Referral(models.Model):
    referrer = models.CharField (max_length=40)
    referralDate= models.DateField(null=True)
    note = models.TextField(blank=True)
    person = models.ForeignKey(to=Person, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.referrer

    class Meta:  
        db_table = "referral" 