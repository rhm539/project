
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# Create your models here.
OFFICE_LOCATION = (
    ('HQT FSL', 'HQT FSL'),
    ('BRL', 'BRL'),
    ('FSL', 'FSL'),
    ('FPL', 'FPL'),
)

class Department(models.Model):
    dptName = models.CharField(max_length=50)
    dptHeadName=models.ForeignKey(User,models.CASCADE,null=True)

    def __str__(self):
       return f'{self.dptName}'

class UserType(models.Model):
    utype = models.CharField(max_length=50)

    def __str__(self):
       return f'{self.utype}'

#class DeptHead(models.Model):
#    dptHeadName=models.CharField(max_length=50)
#    department=models.ForeignKey(Department,models.CASCADE, null=True)
#    boss=models.ManyToManyField(User)
#    boss=models.ManyToManyField(User)


#    def __str__(self):
#       return f'{self.dptHeadName}'


class Profile(models.Model):
    loginuser = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    officeID = models.CharField(max_length=20,null=False)
    officeLocation = models.CharField(max_length=10, choices=OFFICE_LOCATION, null=True)
    #department=models.ForeignKey(department)
    #models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    department=models.ForeignKey(Department,models.CASCADE, null=True)
    utype=models.ForeignKey(UserType,models.CASCADE, null=True, default='1')
    #dptHeadName=models.ForeignKey(DeptHead,models.CASCADE, null=True)
    #department=models.CharField(max_length=20)
    designation=models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    image = models.ImageField(default='pdefault.png',upload_to='profile_images')
    signature=models.ImageField(default='sdefault.png',upload_to='signature_images')

    def __str__(self):
       return f'{self.loginuser.username}-Profile'

