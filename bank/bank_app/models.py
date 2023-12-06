from django.db import models

# Create your models here.
class UserDetails(models.Model):
    user_name = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=25)
    branch = models.CharField(max_length=25)
    account = models.CharField(max_length=50)
    debit_card = models.BooleanField()
    credit_card = models.BooleanField()
    cheque_book = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.user_name)

