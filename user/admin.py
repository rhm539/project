from django.contrib import admin
from .models import Department,Profile, UserType
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display=('loginuser', 'name', 'officeID','department','designation')
    list_filter=('officeID','officeLocation','department')

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Department)
admin.site.register(UserType)
#admin.site.register(DeptHead)
