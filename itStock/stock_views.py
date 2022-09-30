from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import Q

from dashboard.forms import CategoryForm
###
from .models import User
from django.shortcuts import render
from dashboard.models import AccessoriesGroup, Category
from django.contrib import messages
from itStock.models import InvoiceDetail, StockIssue
from itStock.stock_forms import AccessoriesGroupForm, InvoiceItemAddStockForm, StockIssueForm
###############################
####################################

@login_required
def stock_add(request, pk):
    invoiceItemDetail = InvoiceDetail.objects.get(id=pk)

    #category = Category.objects.get(id=invoiceItemDetail.category)
    if request.method== 'POST':
        form = InvoiceItemAddStockForm(request.POST, request.FILES, instance=invoiceItemDetail)
        if form.is_valid():
            invItemdata = form.save(commit=False)
            catagoryID = invItemdata.category.id
            invItemdata.save()
            category = Category.objects.get(id=catagoryID)
            category.stock_quantity = category.stock_quantity + invItemdata.quantity
            category.total_quantity = category.use_quantity + category.stock_quantity + category.damage_quantity
            category.save()
        return redirect('itStock-invoice-list-item')

    else:
        form = InvoiceItemAddStockForm(instance=invoiceItemDetail)
    context = {
        'form': form,
        'invoiceItemDetail':invoiceItemDetail,
               }
    return render(request,'itStock/stock_add.html',context)

@login_required
def stock_issue(request):
    stockIssue = StockIssue.objects.all()
    if request.method == 'POST':
        form = StockIssueForm(request.POST, request.FILES)
        if form.is_valid():
            stockIssuedata = form.save(commit=False)
            categorydata = Category.objects.get(id=stockIssuedata.category.id)
            if stockIssuedata.staff.id > 1 and stockIssuedata.quantity > 0 and stockIssuedata.category.id > 1 and categorydata.stock_quantity > 0:
                    categorydata.stock_quantity = categorydata.stock_quantity-stockIssuedata.quantity
                    categorydata.use_quantity = categorydata.use_quantity+stockIssuedata.quantity
                    categorydata.total_quantity = categorydata.use_quantity + categorydata.stock_quantity + categorydata.damage_quantity
                    categorydata.save()
                    stockIssuedata.save()
                    messages.success(request, f'{stockIssuedata.issueName} has been Issue')
                    return redirect('itStock-stock-issue')
            else:
                messages.success(request, 'unsuccessful Data not added')
                return redirect('itStock-stock-issue')
          
        return redirect('itStock-stock-issue')
    else:
        form = StockIssueForm()
    context = {
        'form': form,
        'stockIssue': stockIssue,
    }
    return render(request, 'itStock/stock_issue.html', context)


@login_required
def stock_issue_delete(request, pk):
    stockIssuedata = StockIssue.objects.get(id=pk)
    categorydata = Category.objects.get(id=stockIssuedata.category.id)
    if request.method == 'POST':
        
        if categorydata.use_quantity > 0:
            categorydata.use_quantity = categorydata.use_quantity-stockIssuedata.quantity
        else:
            categorydata.use_quantity = categorydata.use_quantity+stockIssuedata.quantity
        
        categorydata.total_quantity = categorydata.use_quantity + categorydata.stock_quantity + categorydata.damage_quantity
        stockIssuedata.delete()
        categorydata.save()
        messages.success(request, f'{stockIssuedata.issueName} has been Deleted')
        return redirect('itStock-stock-issue')
    else:
        return render(request, 'itStock/stock_issue_delete.html')


#################################################################

@login_required
def accessories_group(request):
    accessoriesGroupData = AccessoriesGroup.objects.all()
    if request.method == 'POST':
        form = AccessoriesGroupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('itStock-accessories-group')
    else:
        form = AccessoriesGroupForm()
    context = {
        'form': form,
        'accessoriesGroupData': accessoriesGroupData,
    }
    return render(request, 'itStock/accessories_group.html', context)


@login_required
def accessories_group_edit(request, pk):
    accessoriesGroupData = AccessoriesGroup.objects.all()
    accessoriesName = AccessoriesGroup.objects.get(id=pk)
    #category = Category.objects.get(id=invoiceItemDetail.category)
    if request.method== 'POST':
        form = AccessoriesGroupForm(request.POST, request.FILES, instance=accessoriesName)
        if form.is_valid():
            form.save()
        return redirect('itStock-accessories-group')

    else:
        form = AccessoriesGroupForm(instance=accessoriesName)
    context = {
        'form': form,
        'accessoriesGroupData': accessoriesGroupData,
               }
    return render(request, 'itStock/accessories_group_edit.html', context)


@login_required
def accessories_group_item(request, pk):
    category = Category.objects.filter(AGroupName=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            cdata = form.save(commit=False)
            cdata.category = cdata.category.upper()
            cdata.save()
            return redirect('itStock-accessories-group-item', pk)
    else:
        form = CategoryForm(initial={'AGroupName': pk})
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'itStock/access_group_item.html', context)

