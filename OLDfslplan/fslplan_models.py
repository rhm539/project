import datetime
from django.db import models
from dashboard.models import User
# Create your models here.


def increment_booking_number():
  last_booking = SetupDay.objects.all().order_by('DayID').last()
  if not last_booking:
    return 'PRO' + str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + str(datetime.date.today().day).zfill(2) + '000'
  booking_id = last_booking.DayID
  booking_int = int(booking_id[11:14])
  new_booking_int = booking_int + 1
  new_booking_id = 'PRO' + str(str(datetime.date.today().year)) + str(datetime.date.today(
  ).month).zfill(2) + str(datetime.date.today().day).zfill(2) + str(new_booking_int).zfill(3)
  return new_booking_id


datastatus = (
    ('Y', 'YES'),
    ('N', 'NO'),
)


class Unit(models.Model):
    name = models.CharField(max_length=50, null=True)
    def __str__(self):
       return f'{self.name}'
    class Meta:
        db_table = "Unit"




class ProLine(models.Model):
    name = models.CharField(max_length=20, null=True)
    unit = models.ForeignKey(Unit, models.CASCADE, null=True)
    def __str__(self):
       return f'{self.name}'
    class Meta:
        db_table = "ProLine"


class Buyer(models.Model):
    name = models.CharField(max_length=100, null=True)
    def __str__(self):
       return f'{self.name}'
    class Meta:
        db_table = "Buyer"
        

class Style(models.Model):
    name = models.CharField(max_length=150, null=True)
    buyer = models.ForeignKey(Buyer, models.CASCADE, null=True)
    StyleSMV = models.CharField(max_length=5, null=True, blank=True)
    DataLock = models.CharField(max_length=2,default='N',choices=datastatus,null=True)
    def __str__(self):
       return f'{self.name}'
    class Meta:
        db_table = "Style"


class SetupDay(models.Model):
    unit = models.ForeignKey(Unit, models.CASCADE, null=True)
    DayID = models.CharField(max_length=150, default=increment_booking_number, editable=False)
    buyer = models.ForeignKey(Buyer, models.CASCADE, null=True)
    style = models.ForeignKey(Style, models.CASCADE, null=True)
    LineNum = models.ForeignKey(ProLine, models.CASCADE, null=True)
    deleveryDate = models.DateField(editable=True, default='YYYY-MM-DD')
    INputDate = models.DateField(editable=True, default='YYYY-MM-DD')
    sewingEndDate = models.DateField(editable=True, default='YYYY-MM-DD')
    orderQty = models.PositiveSmallIntegerField(default=0)
    planQtyExtra = models.PositiveSmallIntegerField(default=0)
    linePlanQty = models.PositiveSmallIntegerField(default=0)
    DayTerget = models.PositiveSmallIntegerField(default=0)
    HourTerget = models.PositiveSmallIntegerField(default=0)
    WorkHour = models.PositiveSmallIntegerField(default=10)
    EstimateWorkDay = models.PositiveSmallIntegerField(default=0)
    remainingWorkDay = models.PositiveSmallIntegerField(default=0)
    date = models.DateField(editable=True, default='YYYY-MM-DD')
    loadMinutes = models.PositiveSmallIntegerField(default=0)
    DataLock = models.CharField(max_length=2,default='N',choices=datastatus,null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)

    def __str__(self):
        return f'{self.DayID}'

    class Meta:
        db_table = "SetupDay"
        
        
class SetupLine(models.Model):
    DayID = models.CharField(max_length=150, null=True)
    #LineNum = models.ForeignKey(ProLine, models.CASCADE, null=True)
    #style= models.ForeignKey(Style, models.CASCADE, null=True)
    #HourTerget = models.PositiveSmallIntegerField(default=0)
    #DayTT = models.PositiveSmallIntegerField(default=0)
    LineWIP = models.PositiveSmallIntegerField(default=0, blank=True)
    Manpower = models.PositiveSmallIntegerField(default=0, blank=True)
    H_8_9 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_9_10 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_10_11 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_11_12 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_12_13 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_14_15 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_15_16 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_16_17 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_17_18 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_18_19 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_19_20 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_20_21 = models.PositiveSmallIntegerField(default=0, blank=True)
    H_21_22 = models.PositiveSmallIntegerField(default=0, blank=True)
    DataLock = models.CharField(max_length=2,default='N',choices=datastatus,null=True, blank=True)
    date = models.DateField(editable=True, default='YYYY-MM-DD')

    def __str__(self):
        return f'{self.DayID}'

    class Meta:
        db_table = "SetupLine"
