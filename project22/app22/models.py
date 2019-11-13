from django.db import models

class SavimgsAccountmodel(models.Model):
    acno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    type=models.CharField(max_length=10)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    o_bal=models.DecimalField(max_digits=10,decimal_places=2)
    photo=models.ImageField(upload_to="paramesh/",default=False)

