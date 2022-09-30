from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Create your models here.
OFFICE_LOCATION = (
    ('HQT FSL', 'HQT FSL'),
    ('BRL', 'BRL'),
    ('FSL', 'FSL'),
)
Department = (
    ('IT', 'IT'),
    ('Admin, HR & Compliance', 'Admin, HR & Compliance'),
    ('MERCHANDISING', 'MERCHANDISING'),
    ('ACCOUNTS','ACCOUNTS'),
)



class Profile(models.Model):
    loginuser = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    officeID = models.CharField(max_length=20)
    officeLocation = models.CharField(max_length=10, choices=OFFICE_LOCATION, null=True)
    #department=models.ForeignKey(department)
    #models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    department=models.CharField(max_length=50, choices=Department, null=True)
    #department=models.CharField(max_length=20)
    designation=models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    image = models.ImageField(default='default.png',upload_to='profile_images')
    signature=models.ImageField(default='default.png',upload_to='signature_images')

    def __str__(self):
       return f'{self.loginuser.username}-Profile'

