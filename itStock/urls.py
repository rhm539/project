from django.urls import path

from itStock import inventory_views, stock_views
from . import invoice_views
from . import views



urlpatterns = [
    path('', views.index, name='itStock-index'),
    path('fund/', views.fund, name='itStock-fund'),
    path('fund/add/', views.fund_add, name='itStock-fund-add'),
    path('fund/show/<str:pk>/', views.fund_show, name='itStock-fund-show'),
    path('fund/show/all/item/', views.fund_show_all_item, name='itStock-fund-show-all-item'),
    path('fund/item/add/inv/<int:pk>/', views.fund_item_add_inv, name='itStock-fund-item-add-inv'),
    path('fund/item/edit/<int:pk>/', views.fund_item_edit, name='itStock-fund-item-edit'),
    path('fund/item/add/item/<str:pk>/', views.fund_item_add, name='itStock-fund-add-item'),
    path('fund/item/delete/<int:pk>/', views.fund_item_del, name='itStock-fund-item-delete'),
    path('fund/view/myfund/', views.fund_myfund, name='itStock-fund-myfund'),
    path('fund/view/<str:pk>/', views.fund_view, name='itStock-fund-view'),
    #path('fund/mail/<str:pk>/', views.fund_submit, name='itStock-fund-mail'),
    path('fund/submit/<str:pk>/', views.fund_submit, name='itStock-fund-submit'),
    path('fund/app/<str:pk>/', views.fund, name='itStock-fund-app'),
    path('fund/pdf/<str:pk>/', views.fund_pdf, name='itStock-fund-pdf'),    # PDF
    #path('fund/delete/<int:pk>/', views.fund_delete, name='itStock-fund-delete'),
    path('supplier/add/', views.supplier_add, name='itStock-supplier-add'),
    path('supplier/edit/<int:pk>/', views.supplier_edit, name='itStock-supplier-edit'),
    path('supplier/delete/<int:pk>/', views.supplier_delete,name='itStock-supplier-delete'),
    #
    path('invoice/list/', invoice_views.invoice_list, name='itStock-invoice-list'),
    path('invoice/list/item', invoice_views.invoice_list_item, name='itStock-invoice-list-item'),
    path('../../media/', invoice_views.invoice_pdf, name='itStock-invoice-pdf'),
    path('invoice/edit/<int:pk>/', invoice_views.invoice_edit, name='itStock-invoice-edit'),
    #path('invoice/edit/', invoice_views.invoice_edit, name='itStock-invoice-edit'),
    path('invoice/add/',invoice_views.invoice_item_add, name='itStock-invoice-add'),
    path('invoice/view/<str:pk>/',invoice_views.invoice_view, name='itStock-invoice-view'),
    path('invoice/add/item/<str:pk>/',invoice_views.invoice_add_item, name='itStock-invoice-add-item'),
    path('invoice/item/edit/<int:pk>/', invoice_views.invoice_item_edit, name='itStock-invoice-item-edit'),
    path('invoice/item/delete/<int:pk>/', invoice_views.invoice_item_delete, name='itStock-invoice-item-delete'),
    #path('fund/invoice/delete/', views.invoice_del, name='itStock-invoice-delete'),
    #
    path('stock/add/<int:pk>/', stock_views.stock_add, name='itStock-stock-add'),
    path('stock/issue/', stock_views.stock_issue, name='itStock-stock-issue'),
    path('stock/issue/delete/<int:pk>/', stock_views.stock_issue_delete,name='itStock-stock-issue-delete'),
    #
    path('inventory/', inventory_views.inventory,name='itStock-inventory'),
    path('inventory/update/<int:pk>/', inventory_views.inventory_update,name='itStock-inventory-update'),
    #
    path('inventory/pc/<int:pk>/', inventory_views.inventory_pc,name='itStock-inventory-pc'),
    path('inventory/pc/add/<int:pk>/', inventory_views.inventory_pc_add,name='itStock-inventory-pc-add'),
    path('inventory/pc/edit/<int:pk>/', inventory_views.inventory_pc_edit,name='itStock-inventory-pc-edit'),
    #
    path('inventory/laptop/<int:pk>/', inventory_views.inventory_laptop,name='itStock-inventory-laptop'),
    path('inventory/laptop/add/<int:pk>/', inventory_views.inventory_laptop_add,name='itStock-inventory-laptop-add'),
    path('inventory/laptop/edit/<int:pk>/', inventory_views.inventory_laptop_edit,name='itStock-inventory-laptop-edit'),
    #
    path('inventory/mobile/<int:pk>/', inventory_views.inventory_mobile,name='itStock-inventory-mobile'),
    path('inventory/mobile/add/<int:pk>/', inventory_views.inventory_mobile_add,name='itStock-inventory-mobile-add'),
    path('inventory/mobile/edit/<int:pk>/', inventory_views.inventory_mobile_edit,name='itStock-inventory-mobile-edit'),
    #
    path('inventory/ipphone/<int:pk>/', inventory_views.inventory_ipphone,name='itStock-inventory-ipphone'),
    path('inventory/ipphone/add/<int:pk>/', inventory_views.inventory_ipphone_add, name='itStock-inventory-ipphone-add'),
    path('inventory/ipphone/edit/<int:pk>/', inventory_views.inventory_ipphone_edit,name='itStock-inventory-ipphone-edit'),
    #
    path('inventory/printerBW/<int:pk>/', inventory_views.inventory_printerBW,name='itStock-inventory-printerBW'),
    path('inventory/printerBW/add/<int:pk>/', inventory_views.inventory_printerBW_add,name='itStock-inventory-printerBW-add'),
    path('inventory/printerBW/edit/<int:pk>/', inventory_views.inventory_printerBW_edit,name='itStock-inventory-printerBW-edit'),
    #
    path('accessories/group/', stock_views.accessories_group,name='itStock-accessories-group'),
    path('accessories/group/edit/<int:pk>/',stock_views.accessories_group_edit, name='itStock-accessories-group-edit'),
    path('accessories/group/item/<int:pk>/', stock_views.accessories_group_item, name='itStock-accessories-group-item'),
    #path('category/delete/<int:pk>/', views.category_delete,name='dashboard-category-delete'),
    #
    
    
]