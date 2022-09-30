from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models


# Create your models here.
Status = (
    ('ACTIVE', 'ACTIVE'),
    ('INACTIVE', 'INACTIVE'),
    ('STOCK', 'STOCK'),
    ('DAMAGE', 'DAMAGE'),
)
##


class AccessoriesGroup(models.Model):
    AccessoriesName = models.CharField(max_length=150, null=True, unique=True)
    Status = models.CharField(max_length=10, choices=Status, default='ACTIVE', null=True)
    def __str__(self):
        return f'{self.AccessoriesName}'
    




class Category(models.Model):
    category = models.CharField(max_length=150, null=True)
    AGroupName = models.ForeignKey(AccessoriesGroup, models.CASCADE, null=True)
    Status = models.CharField(max_length=10, choices=Status,default='ACTIVE', null=True)
    use_quantity = models.PositiveIntegerField(default='0')
    stock_quantity = models.PositiveIntegerField(default='0')
    damage_quantity = models.PositiveIntegerField(default='0')
    total_quantity = models.PositiveIntegerField(default='0')
    def __str__(self):
        return f'{self.category}'

class Product(models.Model):
    name = models.CharField(max_length=150,null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.ForeignKey(Category, models.CASCADE, null=True)
    Status = models.CharField(max_length=10, choices=Status,default='ACTIVE',null=True)
    def __str__(self):
        return f'{self.name}-{self.category}'

OrStatus = (
    ('NEW', 'NEW'),
    ('SEND','SEND'),
    ('DELIVER', 'DELIVER'),
)

class Order(models.Model):
    AccessoriesName = models.ForeignKey(AccessoriesGroup, models.CASCADE, null=True)
    product = models.ForeignKey(Category, models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True, blank=True)
    order_quantity = models.PositiveIntegerField(null=True)
    OrStatus = models.CharField(max_length=10, choices=OrStatus, default='NEW', null=True)
    date=models.DateField(auto_now_add=True)
    #re_other = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.product} order by {self.staff.username}'



    

