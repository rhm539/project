from django.contrib import admin
from fslplan.fslplan_models import Buyer, ProLine, SetupDay, SetupLine, Style, Unit

# Register your models here.
admin.site.register(Unit)
admin.site.register(ProLine)
admin.site.register(Buyer)
admin.site.register(Style)
admin.site.register(SetupDay)
admin.site.register(SetupLine)
