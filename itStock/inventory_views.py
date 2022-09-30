from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from itStock.inventory_forms import InventoryALLphoneForm, InventoryDetailForm, InventoryForm, InventoryIPphoneForm, InventoryLaptopForm, InventoryMobileForm
from itStock.models import Inventory, InventoryAll, InventoryDetail
from django.contrib import messages

@login_required
def inventory(request):
    inventorydata = Inventory.objects.all().order_by('productname')

    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Product Added')
            form.save()
            return redirect('itStock-inventory')
    else:
        form = InventoryForm()

    context = {
            'form': form,
           	'inventorydata': inventorydata,

        }
    return render(request, 'itStock/inventory.html', context)


@login_required
def inventory_update(request, pk):
    inventorydata = Inventory.objects.all()
    inventory = Inventory.objects.get(id=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST, request.FILES, instance=inventory)
        if form.is_valid():
            form.save()
            messages.success(
            	request, 'Product Updated')
            return redirect('itStock-inventory')
    else:
        form = InventoryForm(instance=inventory)
    context = {
            'form': form,
           	'inventorydata': inventorydata,
    }
    return render(request, 'itStock/inventory_update.html', context)

##############################################
@login_required
def inventory_pc(request,pk):
	InventoryPCdata = InventoryDetail.objects.filter(productname=pk)
	context = {

           	'InventoryPCdata': InventoryPCdata,
        }
	return render(request, 'itStock/inventory_pc.html', context)


@login_required
def inventory_pc_add(request,pk):
    inventory = Inventory.objects.get(id=pk)
    if request.method == 'POST':
        
        form = InventoryDetailForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            return redirect('itStock-inventory')
    else:
        form = InventoryDetailForm(initial={'productname': pk})
    context = {
        'form': form,
        'inventory': inventory,
    }
    return render(request, 'itStock/inventory_pc_add.html', context)


@login_required
def inventory_pc_edit(request, pk):
    inventoryPC = InventoryDetail.objects.get(id=pk)
    if request.method == 'POST':
        form = InventoryDetailForm(
            request.POST, request.FILES, instance=inventoryPC)
        if form.is_valid():
            form.save()
            return redirect('itStock-inventory-pc', inventoryPC.productname.id)
    else:
        form = InventoryDetailForm(instance=inventoryPC)
    context = {
        'form': form,
        'inventoryPC': inventoryPC
    }
    return render(request, 'itStock/inventory_pc_edit.html', context)
    
    
############################################################   
@login_required
def inventory_laptop(request, pk):
	InventoryPCdata = InventoryDetail.objects.filter(productname=pk)
	context = {

            'InventoryPCdata': InventoryPCdata,
        }
	return render(request, 'itStock/inventory_laptop.html', context)


    
@login_required
def inventory_laptop_add(request, pk):
    inventory = Inventory.objects.get(id=pk)
    if request.method == 'POST':

        form = InventoryLaptopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('itStock-inventory')
    else:
        form = InventoryLaptopForm(initial={'productname': pk})
    context = {
        'form': form,
        'inventory': inventory,
    }
    return render(request, 'itStock/inventory_laptop_add.html', context)
    

@login_required
def inventory_laptop_edit(request, pk):
    inventoryPC = InventoryDetail.objects.get(id=pk)
    if request.method == 'POST':
        form = InventoryLaptopForm(
            request.POST, request.FILES, instance=inventoryPC)
        if form.is_valid():
            form.save()
            return redirect('itStock-inventory-laptop', inventoryPC.productname.id)
    else:
        form = InventoryLaptopForm(instance=inventoryPC)
    context = {
        'form': form,
        'inventoryPC': inventoryPC
    }
    return render(request, 'itStock/inventory_laptop_edit.html', context)

######################################################################################


@login_required
def inventory_mobile(request, pk):
	InventoryPCdata = InventoryDetail.objects.filter(productname=pk)
	context = {

            'InventoryPCdata': InventoryPCdata,
        }
	return render(request, 'itStock/inventory_mobile.html', context)

    
@login_required
def inventory_mobile_add(request, pk):
    inventory = Inventory.objects.get(id=pk)
    if request.method == 'POST':

        form = InventoryMobileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('itStock-inventory')
    else:
        form = InventoryMobileForm(initial={'productname': pk})
    context = {
        'form': form,
        'inventory': inventory,
    }
    return render(request, 'itStock/inventory_mobile_add.html', context)


@login_required
def inventory_mobile_edit(request, pk):
    inventoryPC = InventoryDetail.objects.get(id=pk)
    if request.method == 'POST':
        form = InventoryMobileForm(
            request.POST, request.FILES, instance=inventoryPC)
        if form.is_valid():
            form.save()
            return redirect('itStock-inventory-mobile', inventoryPC.productname.id)
    else:
        form = InventoryMobileForm(instance=inventoryPC)
    context = {
        'form': form,
        'inventoryPC': inventoryPC
    }
    return render(request, 'itStock/inventory_mobile_edit.html', context)

#########################################################################################
@login_required
def inventory_ipphone(request, pk):
	InventoryPCdata = InventoryAll.objects.filter(productname=pk)
	context = {
            'InventoryPCdata': InventoryPCdata,
        }
	return render(request, 'itStock/inventory_ipphone.html', context)
 
@login_required
def inventory_ipphone_add(request, pk):
    inventory = Inventory.objects.get(id=pk)
    if request.method == 'POST':
        form = InventoryIPphoneForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('itStock-inventory')
    else:
        form = InventoryIPphoneForm(initial={'productname': pk})
    context = {
        'form': form,
        'inventory': inventory,
    }
    return render(request, 'itStock/inventory_ipphone_add.html', context)
@login_required
def inventory_ipphone_edit(request, pk):
    inventoryPC = InventoryAll.objects.get(id=pk)
    if request.method == 'POST':
        form = InventoryIPphoneForm(
            request.POST, request.FILES, instance=inventoryPC)
        if form.is_valid():
            form.save()
            return redirect('itStock-inventory-ipphone', inventoryPC.productname.id)
    else:
        form = InventoryIPphoneForm(instance=inventoryPC)
    context = {
        'form': form,
        'inventoryPC': inventoryPC
    }
    return render(request, 'itStock/inventory_ipphone_edit.html', context)
#################################################################################


@login_required
def inventory_printerBW(request, pk):
	InventoryPCdata = InventoryAll.objects.filter(productname=pk)
	context = {
            'InventoryPCdata': InventoryPCdata,
        }
	return render(request, 'itStock/inventory_PrinterBW.html', context)

@login_required
def inventory_printerBW_add(request, pk):
    inventory = Inventory.objects.get(id=pk)
    if request.method == 'POST':
        form = InventoryALLphoneForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('itStock-inventory')
    else:
        form = InventoryALLphoneForm(initial={'productname': pk})
    context = {
        'form': form,
        'inventory': inventory,
    }
    return render(request, 'itStock/inventory_printerBW_add.html', context)


@login_required
def inventory_printerBW_edit(request, pk):
    inventoryPC = InventoryAll.objects.get(id=pk)
    if request.method == 'POST':
        form = InventoryALLphoneForm(
            request.POST, request.FILES, instance=inventoryPC)
        if form.is_valid():
            form.save()
            return redirect('itStock-inventory-printerBW', inventoryPC.productname.id)
    else:
        form = InventoryALLphoneForm(instance=inventoryPC)
    context = {
        'form': form,
        'inventoryPC': inventoryPC
    }
    return render(request, 'itStock/inventory_printerBW_edit.html', context)
