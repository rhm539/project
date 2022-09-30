from django.contrib import admin
from itStock.models import InvoiceDetail, Supplier,Fund, Invoice, FundDetail


# Register your models here.
class SupplierAdmin(admin.ModelAdmin):
    list_display=('supplierName','contactName')
    list_filter=('supplierName','contactName')

class FundAdmin(admin.ModelAdmin):
    list_display=('fundNumber','fundName','fundAmount','date','status','staff')
    list_filter=('fundName','fundAmount','status')
class FundDetailAdmin(admin.ModelAdmin):
   list_display=('fundSerial','particulars','buyer','style','quantity','rate','amount','remarks','date','status','fundName','staff')
   list_filter=('fundSerial','particulars','buyer')

class InvoiceAdmin(admin.ModelAdmin):
    list_display=('invoiceNumber','supplierName','totalAmount','status')
    list_filter=('invoiceNumber','supplierName','totalAmount')

class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display=('invoiceNumber','productName','price','warranty')
    list_filter=('invoiceNumber','productName','price')

   



admin.site.register(Supplier,SupplierAdmin)
admin.site.register(Fund,FundAdmin)
admin.site.register(FundDetail,FundDetailAdmin)
admin.site.register(Invoice,InvoiceAdmin)
admin.site.register(InvoiceDetail,InvoiceDetailAdmin)




