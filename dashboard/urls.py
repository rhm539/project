from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    #path('', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/list/', views.staff_list, name='dashboard-staff-list'),
    path('staff/update/<int:pk>/', views.staff_update,name='dashboard-staff-update'),
    path('staff/detail/<int:pk>/', views.staff_detail, name='dashboard-staff-detail'),
    path('department/', views.department, name='dashboard-department'),
    path('department/update/<int:pk>/',
         views.department_update, name='dashboard-department-update'),
    path('staff/request/', views.staff_request, name='dashboard-staff-request'),
    path('product/', views.product, name='dashboard-product'),
    path('product/edit/<int:pk>/', views.product_edit, name='dashboard-product-edit'),
    path('product/delete/<int:pk>/', views.product_delete,name='dashboard-product-delete'),
    #path('product/detail/<int:pk>/', views.product_detail,name='dashboard-product-detail'),
    #
    path('category/', views.category, name='dashboard-category'),
    path('category/edit/<int:pk>/', views.category_edit, name='dashboard-category-edit'),
    path('category/delete/<int:pk>/', views.category_delete,name='dashboard-category-delete'),
    #
    path('order/', views.order, name='dashboard-order'),
    path('order/edit/<int:pk>/', views.order_edit, name='dashboard-order-edit'),
    path('order/update/<int:pk>/', views.order_update,name='dashboard-order-update'),
    path('order/delete/<int:pk>/', views.order_delete,name='dashboard-order-delete'),
    path('order/view/<int:pk>/', views.order_view,name='dashboard-order-view'),
    #path('order/mail/<int:pk>/', views.order_mail,name='dashboard-order-mail'),
    #
    #path('orderUser/edit/<int:pk>/', views.orderUser_edit, name='dashboard-orderUser-edit'),
    #path('orderUser/delete/<int:pk>/', views.orderUser_delete,name='dashboard-orderUser-delete'),
    #
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name ='password_reset_complete'),
    ]
  
