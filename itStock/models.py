from user.models import Department
from dashboard.models import Category, User
import datetime
from django.db import models

# Create your models here.

def increment_booking_number():
  last_booking = Fund.objects.all().order_by('fundNumber').last()
  if not last_booking:
    return 'FUD' + str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + str(datetime.date.today().day).zfill(2) + '000'
  booking_id = last_booking.fundNumber
  booking_int = int(booking_id[11:14])
  new_booking_int = booking_int + 1
  new_booking_id = 'FUD' + str(str(datetime.date.today().year)) + str(datetime.date.today().month).zfill(2) + str(datetime.date.today().day).zfill(2)+ str(new_booking_int).zfill(3)
  return new_booking_id


####
Unit = (
    ('FSL HQT', 'FSL HQT'), 
    ('FSL', 'FSL'),
    ('FPL', 'FASHION PULSE'),
    ('BRL', 'BRL'),
)
Status = (
    ('ACTIVE', 'ACTIVE'),
    ('INACTIVE', 'INACTIVE'),
)
OrStatus = (
    ('NEW','NEW'),
    ('SEND','SEND'),
    ('ACCEPT', 'ACCEPT'),
    ('DELIVER', 'DELIVER'),
    ('WAITING', 'WAITING'),
    ('APPROVE', 'APPROVE'),
    ('HOLD', 'HOLD'),
    ('REJECT','REJECT')
)
InStatus = (
    ('PAID', 'PAID'),
    ('UNPAID','UNPAID')
)

WStatus = (
    ('NULL','NULL'),
    ('30 D', '30 D'),
    ('60 D', '60 D'),
    ('90 D', '90 D'),
    ('1 Year', '1 Year'),
    ('2 Year', '2 Year'),
    ('3 Year','3 Year'),
    ('5 Year','5 Year'),
    ('Life Time', 'Life Time'),
)

##
class Supplier(models.Model):
    supplierName = models.CharField(max_length=150, null=True)
    contactName = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    contactNumber=models.CharField(max_length=150, null=True,unique=True)
    date=models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=Status,default='ACTIVE', null=True)
    def __str__(self):
        return f'{self.supplierName}'

class Invoice(models.Model):
    unit = models.CharField(max_length=10, choices=Unit,default='FSL HQT', null=True)
    invoiceNumber = models.CharField(max_length=150, null=True,unique=True)
    supplierName = models.ForeignKey(Supplier,models.CASCADE, null=True)
    totalAmount=models.CharField(max_length=150,null=True)
    status = models.CharField(max_length=10, choices=InStatus,default='UNPAID', null=True)
    pdf = models.FileField(default='invoice.pdf',upload_to='invoice_pdf')
    date=models.DateField(editable=True,default='YY-MM-DD')
    def __str__(self):
        return f'{self.invoiceNumber}'
    class Meta:
        db_table = "invoice"

class InvoiceDetail(models.Model):
    productName = models.CharField(max_length=150, null=True)
    quantity = models.PositiveIntegerField(default='1')
    unitprice=models.PositiveIntegerField(default='1')
    price=models.PositiveIntegerField(default='1')
    warranty= models.CharField(max_length=10,choices=WStatus,null=True,default='NULL' )
    macaddress=models.CharField(max_length=150,null=True,default='00-00-00-00')
    invoiceNumber = models.CharField(max_length=150, null=True)
    fundSerial = models.CharField(max_length=15, null=True)
    staff = models.ForeignKey(User,models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    addstock = models.BooleanField(default=False)
    category = models.ForeignKey(Category, models.CASCADE, null=True)
    def __str__(self):
        return f'{self.productName}'
    class Meta:
        db_table = "invoicedetail"



class Fund(models.Model):
    fundNumber= models.CharField(max_length=150,default = increment_booking_number, editable=False,primary_key=True )
    fundName = models.CharField(max_length=150, null=True)
    fundAmount = models.IntegerField()
    unit=models.CharField(max_length=10, choices=Unit,default='FSL HQT', null=True)
    date=models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=OrStatus,default='NEW', null=True)
    staff = models.ForeignKey(User,models.CASCADE, null=True)
    department=models.ForeignKey(Department,models.CASCADE, null=True)
    headdept=models.CharField(max_length=150,default='NULL')
    admindpt=models.CharField(max_length=150,default='NULL')
    gmacc=models.CharField(max_length=150,default='NULL')
    director=models.CharField(max_length=150,default='NULL')
    md=models.CharField(max_length=150,default='NULL')
    def __str__(self):
        return f'{self.fundNumber}'
    class Meta:
        db_table = "fund"


class FundDetail(models.Model):
    particulars=models.CharField(max_length=150,null=True)
    buyer=models.CharField(max_length=150,null=True)
    style=models.CharField(max_length=150,null=True)
    quantity=models.PositiveIntegerField(default='1',null=True)
    rate=models.IntegerField()
    amount=models.CharField(max_length=150,null=True)
    remarks=models.CharField(max_length=150,null=True)
    date=models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=OrStatus,default='NEW', null=True)
    fundSerial=models.CharField(max_length=15,null=True, editable=False)
    fundName = models.CharField(max_length=150,null=True)
    staff = models.ForeignKey(User,models.CASCADE, null=True)
    unit = models.CharField(max_length=10, null=True)
    invoiceNumber = models.ForeignKey(Invoice,models.CASCADE, null=True)
    
 
    def __str__(self):
        return f'{self.particulars}'
    class Meta:
        db_table = "funddetail"
        
        
class StockIssue(models.Model):
    issueName = models.CharField(max_length=150, null=True)
    category = models.ForeignKey(Category, models.CASCADE, null=True)
    staff = models.ForeignKey(User,models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default='1')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.issueName}'

    class Meta:
        db_table = "StockIssue"

##3#####################################################################################################


def increment_Inventory_number():
  last_booking = InventoryDetail.objects.all().order_by('inventoryNumber').last()
  if not last_booking:
    return 'INV' + str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + str(datetime.date.today().day).zfill(2) + '000'
  booking_id = last_booking.inventoryNumber
  booking_int = int(booking_id[11:14])
  new_booking_int = booking_int + 1
  new_booking_id = 'INV' + str(str(datetime.date.today().year)) + str(datetime.date.today(
  ).month).zfill(2) + str(datetime.date.today().day).zfill(2) + str(new_booking_int).zfill(3)
  return new_booking_id


class Inventory(models.Model):
    productname = models.CharField(max_length=150, null=True, unique=True)
    linkAdd= models.CharField(max_length=150, null=True)
    linkDetail = models.CharField(max_length=150, null=True)
    def __str__(self):
        return f'{self.productname}'
    class Meta:
        db_table = "Inventory"


bagStatus = (
    ('YES', 'YES'),
    ('NO', 'NO')
)
InvStatus = (
    ('ACTIVE', 'ACTIVE'),
    ('IN STOCK', 'IN STOCK'),
    ('DAMAGE', 'DAMAGE'),
)
laptop = (
    ('HP', 'HP'),
    ('DELL', 'DELL'),
    ('LENOVO', 'LENOVO'),
    ('MAC', 'MAC'),
    ('ACER', 'ACER'),
)

class MobileSetup(models.Model):
    MobileName = models.CharField(max_length=150, null=True)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=Status, default='ACTIVE', null=True)
    def __str__(self):
        return f'{self.MobileName}'

class InventoryDetail(models.Model):
    inventoryNumber = models.CharField(max_length=150, default=increment_Inventory_number, editable=False,unique=True)
    LaptopBrand = models.CharField(max_length=30, choices=laptop, null=True)
    MobileBrand = models.ForeignKey(MobileSetup, models.CASCADE, null=True)
    productname = models.ForeignKey(Inventory, models.CASCADE, null=True)
    Processor = models.ForeignKey(Category,models.CASCADE, null=True)
    Motherboard = models.ForeignKey(Category, models.CASCADE, null=True, related_name = 'Motherboard')
    RAM1 = models.ForeignKey(Category, models.CASCADE,null=True, related_name='RAM1')
    RAM2 = models.ForeignKey(Category, models.CASCADE,null=True, related_name='RAM2', blank=True)
    GraphicsCard = models.ForeignKey(
        Category, models.CASCADE, null=True, related_name='GraphicsCard', blank=True)
    STORAGE1 = models.ForeignKey(Category, models.CASCADE,null=True, related_name='SSD')
    STORAGE2 = models.ForeignKey(
        Category, models.CASCADE, null=True, related_name='M2', blank=True)
    Monitor = models.ForeignKey(Category, models.CASCADE, null=True, related_name='Monitor')
    Mouse = models.ForeignKey(Category, models.CASCADE, null=True, related_name='Mouse')
    Keyboard = models.ForeignKey(Category, models.CASCADE, null=True, related_name='Keyboard')
    UPS = models.ForeignKey(Category, models.CASCADE, null=True,related_name='UPS', blank=True)
    remarks = models.CharField(max_length=150, null=True, blank=True)
    Laptopbag = models.CharField(max_length=10, choices=bagStatus, default='NO', null=True)
    Knox = models.CharField(
        max_length=10, choices=bagStatus, default='YES', null=True)
    MobileMacc = models.CharField(max_length=50, null=True, default='00-00-00-00')
    #quantity = models.PositiveIntegerField(default='1')
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    status = models.CharField(max_length=30, choices=InvStatus, default='ACTIVE', null=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.inventoryNumber}'
    class Meta:
        db_table = "InventoryDetail"

########################################################################################


def increment_InventoryAll_number():
  last_booking = InventoryAll.objects.all().order_by('inventoryNumber').last()
  if not last_booking:
    return 'FSL' + str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + str(datetime.date.today().day).zfill(2) + '000'
  booking_id = last_booking.inventoryNumber
  booking_int = int(booking_id[11:14])
  new_booking_int = booking_int + 1
  new_booking_id = 'FSL' + str(str(datetime.date.today().year)) + str(datetime.date.today(
  ).month).zfill(2) + str(datetime.date.today().day).zfill(2) + str(new_booking_int).zfill(3)
  return new_booking_id

class InventoryAll(models.Model):
    inventoryNumber = models.CharField(max_length=150, default=increment_InventoryAll_number, editable=False, unique=True)
    productname = models.ForeignKey(Inventory, models.CASCADE, null=True)
    Brand = models.CharField(max_length=30, null=True)
    model= models.CharField(max_length=30, null=True)
    ExtensionNumber = models.CharField(max_length=5, null=True,blank=True)
    department = models.ForeignKey(Department, models.CASCADE, null=True)
    unit = models.CharField(max_length=10, choices=Unit,default='FSL HQT', null=True)
    macaddress = models.CharField(max_length=150, null=True, default='00-00-00-00')
    status = models.CharField(max_length=30, choices=InvStatus, default='ACTIVE', null=True)
    remarks = models.CharField(max_length=150, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.inventoryNumber}'

    class Meta:
        db_table = "InventoryAll"
        
