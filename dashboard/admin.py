from django.contrib import admin


from itStock.models import Inventory, InventoryAll, InventoryDetail, MobileSetup,StockIssue
from .models import AccessoriesGroup, Order, Product, Category
# Register your models here.

admin.site.site_header='FSL Inventory'
admin.site.site_title='FSL Home Page'

class ProductAdmin(admin.ModelAdmin):
    list_display=('name', 'category', 'quantity','Status')
    list_filter=('name','category','Status')

class OrderAdmin(admin.ModelAdmin):
    list_display=('product', 'staff', 'order_quantity','OrStatus')
    list_filter=('product', 'staff','OrStatus')
class CategoryAdmin(admin.ModelAdmin):
    list_display=('Category','Status')


class StockIssueAdmin(admin.ModelAdmin):
    list_display = ('issueName', 'staff')


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('productname')
    

class InventoryDetailAdmin(admin.ModelAdmin):
    list_display = ('inventoryNumber', 'productname',
                    'MobileBrand', 'LaptopBrand', 'staff')
    list_filter = ('productname', 'inventoryNumber', 'MobileBrand')


class AccessoriesGroupAdmin(admin.ModelAdmin):
    list_display = ('AccessoriesName')


class MobileSetupAdmin(admin.ModelAdmin):
    list_display = ('MobileName')


class InventoryAllAdmin(admin.ModelAdmin):
    list_display = ('productname', 'inventoryNumber', 'status')
    list_filter = ('productname', 'inventoryNumber', 'status')


admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Category)
admin.site.register(StockIssue)
admin.site.register(Inventory)
admin.site.register(InventoryDetail, InventoryDetailAdmin)
admin.site.register(AccessoriesGroup)
admin.site.register(MobileSetup)
admin.site.register(InventoryAll, InventoryAllAdmin)
