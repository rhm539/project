from django.urls import path
from . import fslplan_views


urlpatterns = [
    path('', fslplan_views.index, name='fslplan-index'),
    path('buyer/list/', fslplan_views.buyer_list, name='fslplan-buyer-list'),
    path('buyer/edit/<int:pk>/', fslplan_views.buyer_edit,
         name='fslplan-buyer-edit'),
    path('style/list/', fslplan_views.style_list, name='fslplan-style-list'),
    path('style/edit/<int:pk>/', fslplan_views.style_edit,
         name='fslplan-style-edit'),
    path('Buyer_style/list/<int:pk>/', fslplan_views.Buyer_style_list,
         name='fslplan-Buyer_style-list'),
    path('daysetup/', fslplan_views.daySetup, name='fslplan-daysetup'),
    path('daysetup/show/', fslplan_views.daySetup_show,
         name='fslplan-daysetup-show'),
    path('prod/output/edit/<int:pk>/', fslplan_views.prod_output_edit,
         name='fslplan-prod-output-edit'),
    path('prod/output/show', fslplan_views.prod_output_show,
         name='fslplan-prod-output-show'),
    path('prod/load/style/', fslplan_views.load_style,name='ajax_load_style'),  # AJAX

]
