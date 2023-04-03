from django.db import models

# Create your models here.
class Account (models.Model): 
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=60)
    firstname = models.TextField()
    lastname = models.TextField()
    address = models.TextField()
    sdt = models.CharField(max_length=11)
    roles = models.CharField(max_length=10)
    
class TraSua (models.Model): 
    loai = models.TextField()
    kichthuoc = models.CharField(max_length=1)
    gia = models.IntegerField()
    
class DonHang (models.Model):
    idts = models.ForeignKey(TraSua, on_delete=models.CASCADE)
    username = models.ForeignKey(Account, on_delete=models.CASCADE)
    isdeliver = models.BooleanField()