from dashboard.models import Product
from itStock.models import Fund, Invoice
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from user.forms import addDepartmentForm, addProfileForm, addUserForm
from user.models import Department, Profile
from .models import Product, Order, User, Category
from .forms import CategoryFormEdit, OrderITForm, ProductForm, OrderForm, CategoryForm, ProductFormEdit, OrderFormEdit
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib import messages
####################################
# Create your views here.

@login_required
def index(request):
    orders = Order.objects.all()
    product = Product.objects.all()
    staff_count = User.objects.all().count()
    product_count= product.count()
    order_count = orders.count()
    fund = Fund.objects.all()
    fund_count = fund.count()
    invoice=Invoice.objects.all()
    invoice_count = invoice.count()
    category_count= Category.objects.all().count()
    if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.staff = request.user
                instance.save()
                return redirect('dashboard-index')
    else:
        form = OrderForm()
    context ={
        'orders': orders,
        'form': form,
        'product': product,
        'staff_count':staff_count,
        'product_count':product_count,
        'order_count':order_count,
        'category_count': category_count,
        'fund_count': fund_count,
        'fund': fund,
        'invoice_count' : invoice_count,
    }
    return render(request,'dashboard/index.html', context)
@login_required
def staff_request(request):
    orders = Order.objects.filter(staff=request.user)
    if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.staff = request.user
                instance.save()
                return redirect('dashboard-staff-request')
    else:
        form = OrderForm()
    context ={
        'orders': orders,
        'form': form,
        'product': product,

    }
    return render(request,'dashboard/staff_request.html', context)


@login_required
def staff_detail(request, pk):
    staff = User.objects.get(id=pk)
    context = {
        'staff': staff,
    }
    return render(request, 'dashboard/staff_detail.html', context)



@login_required
def staff(request):
    staff = User.objects.all()
    staff_count = User.objects.all().count()
    product_count= Product.objects.all().count()
    order_count = Order.objects.all().count()
    category_count= Category.objects.all().count()
    context = {
        'staff': staff,
        'staff_count': staff_count,
        'product_count':product_count,
        'order_count': order_count,
        'category_count': category_count,
    }
    return render(request,'dashboard/staff.html', context)


@login_required
def staff_list(request):
    staff = Profile.objects.all().order_by('loginuser')
    form = addUserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} has been added')
            #group = Group.objects.get(name='Customers')
            #user.groups.add(group)
            Profile.objects.create(loginuser=user)
            staff=Profile.objects.get(loginuser=user)
            return redirect('dashboard-staff-update', staff.id)
    else:
        form = addUserForm()
    context = {
        'form': form,
        'staff': staff,
    }
    return render(request, 'dashboard/staff_list.html', context)


@login_required
def staff_update(request, pk):
    staff = Profile.objects.all().order_by('loginuser')
    profile = Profile.objects.get(id=pk)
    user = User.objects.get(id=pk)
    
    if request.method == 'POST':
        form = addProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard-staff-list')
    else:
        form = addProfileForm(instance=profile)
    context = {
        'user': user,
        'form': form,
        'staff': staff,
     }
    return render(request, 'dashboard/staff_update.html', context)


@login_required
def department(request):
    department = Department.objects.all().order_by('dptName')
    if request.method == 'POST':
        form = addDepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-department')
    else:
        form = addDepartmentForm()
    context = {
        'form': form,
        'department': department,
    }
    return render(request, 'dashboard/department.html', context)


@login_required
def department_update(request,pk):
    department = Department.objects.all()
    departmentID = Department.objects.get(id=pk)

    if request.method == 'POST':
        form = addDepartmentForm(request.POST, request.FILES, instance=departmentID)
        if form.is_valid():
            form.save()
            return redirect('dashboard-department')
    else:
        form = addDepartmentForm(instance=departmentID)
    context = {
        'form': form,
        'department': department,
    }
    return render(request, 'dashboard/department_update.html', context)






























@login_required
def product(request):
    product = Product.objects.all()
    staff_count = User.objects.all().count()
    product_count= Product.objects.all().count()
    order_count = Order.objects.all().count()
    category_count= Category.objects.all().count()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'form': form,
        'product': product,
        'staff_count': staff_count,
        'product_count':product_count,
        'order_count': order_count,
        'category_count': category_count,
    }
    return render(request, 'dashboard/product.html', context)
@login_required
def product_delete(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')
@login_required
def product_edit(request, pk):
    product = Product.objects.get(id=pk)
    if request.method== 'POST':
        form = ProductFormEdit(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductFormEdit(instance=product)
    
    context = {
        'form': form,
		}
    return render(request, 'dashboard/product_edit.html', context)





##########################
@login_required
def order(request):
    orders = Order.objects.all()
    if request.method == 'POST':
        form = OrderITForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.staff:
                order.save()
                messages.success(request, 'Succeful, Request Added ')
            elif request.user.profile.department.id <5:
                messages.success(request, 'Unsucceful, Add Employee')
                return redirect('dashboard-order')
            else:
                order.staff=request.user
                order.save()
                messages.success(request, 'Succeful, Request Added ')
            return redirect('dashboard-order')

    else:
        if request.user.profile.department.id > 5:
            form = OrderForm()
        else:
            form = OrderITForm()
    
    context ={
        'orders': orders,
        'form': form,
        }
    return render(request,'dashboard/order.html', context)

@login_required
def order_update(request, pk):
    order = Order.objects.get(id=pk)
    if order.OrStatus == 'NEW':
        order.OrStatus = 'SEND'
        order.save()
        mailOwn = order.staff.email
        mailUP = request.user.email
        orderSend_mail(request, pk, mailOwn, mailUP)
        #send_mail('Service Reques', 'body of the message','project@fashionstepbd.net', ['a.rob@fashionstepbd.net', ])
        #return redirect('dashboard-order')
    elif order.OrStatus == 'SEND':
        order.OrStatus = 'DELIVER'
        order.save()
        mailOwn = order.staff.email
        mailUP = request.user.email
        orderSend_mail(request, pk, mailOwn, mailUP)
        #send_mail('subject', 'body of the message', 'project@fashionstepbd.net', ['a.rob@fashionstepbd.net', ])
        #return redirect('dashboard-order')
    return redirect('dashboard-order')


@login_required
def order_view(request, pk):
    context = order_mail(pk)
    return render(request, 'dashboard/order_mail.html', context)



def order_mail(pk):
    order = Order.objects.get(id=pk)
    context = {
        'order': order,
    }
    return context
    #return render(request, 'dashboard/order_mail.html', context)


@login_required
def orderSend_mail(request, pk, mailOwn, mailUP):
    context = order_mail(pk)
    message = get_template('dashboard/order_mail.html').render(context)
    msg = EmailMessage(
            'Subject: IT Product Request',
            message,
            'project@fashionstepbd.net',
            ['mynuddin@fashionstepbd.net',
                'itsupport@fashionstepbd.net', mailUP, mailOwn],
        )
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    #return redirect('dashboard-order')

@login_required
def order_delete(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('dashboard-order')
    return render(request, 'dashboard/order_delete.html')

@login_required
def order_edit(request, pk):
    order = Order.objects.get(id=pk)
    if request.method== 'POST':
        form = OrderFormEdit(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('dashboard-order')
    else:
            form = OrderFormEdit(instance=order)
    context = {
        'form': form,
		}
    return render(request, 'dashboard/order_edit.html', context)


####    ACCESSORIES
@login_required
def category(request):
    category = Category.objects.all().order_by('category')
    if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                cdata = form.save(commit=False)
                cdata.category = cdata.category.upper()
                cdata.save()
                return redirect('dashboard-category')
    else:
        form = CategoryForm()
       
    context={
        'form': form,
        'category': category,
    }
    return render(request,'dashboard/category.html', context)


@login_required
def category_delete(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('dashboard-category')
    return render(request, 'dashboard/category_delete.html')

@login_required
def category_edit(request, pk):
    category = Category.objects.get(id=pk)
    if request.method== 'POST':
        form = CategoryFormEdit(request.POST, instance=category)
        if form.is_valid():
            cdata = form.save(commit=False)
            cdata.category = cdata.category.upper()
            cdata.save()
            return redirect('dashboard-category')
    else:
        form = CategoryFormEdit(instance=category)
    context = {
        'form': form,
		}
    return render(request, 'dashboard/category_edit.html', context)