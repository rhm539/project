

from datetime import date
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from django.shortcuts import render
from fslplan.fslplan_forms import BuyerForm, DaysetupForm, SetupLineForm, StyleForm

from fslplan.fslplan_models import Buyer, SetupDay, SetupLine, Style



###############################

####################################

# AJAX
def load_style(request):
    buyer = request.GET.get('buyer')
    styles = Style.objects.filter(buyer=buyer).all()
    return render(request, 'fslplan/style_load.html', {'styles': styles})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)



@login_required
def index(request):
  return render(request, 'fslplan/index.html')


@login_required
def buyerlist(request):
    clientDATA = Buyer.objects.all().order_by('name')
    if request.method == 'POST':
        form = BuyerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fslplan-buyer-list')
    else:
        form = BuyerForm()
    context = {
        'form': form,
        'clientDATA': clientDATA,
    }
    return render(request, 'fslplan/buyer_list.html', context)


@login_required
def buyer_list(request):
    clientDATA = Buyer.objects.all().order_by('name')
    if request.method == 'POST':
        form = BuyerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fslplan-buyer-list')
    else:
        form = BuyerForm()
    context = {
        'form': form,
        'clientDATA': clientDATA,
    }
    return render(request, 'fslplan/buyer_list.html', context)


@login_required
def buyer_edit(request, pk):
    clientDATA = Buyer.objects.all()
    ClientDataID = Buyer.objects.get(id=pk)

    if request.method == 'POST':
        form = BuyerForm(
            request.POST, request.FILES, instance=ClientDataID)
        if form.is_valid():
            form.save()
            return redirect('fslplan-buyer-list')
    else:
        form = BuyerForm(instance=ClientDataID)
    context = {
        'form': form,
        'clientDATA': clientDATA,
    }
    return render(request, 'fslplan/buyer_list.html', context)


@login_required
def style_list(request):
    StyleDATA = Style.objects.all().order_by('name')
    if request.method == 'POST':
        form = StyleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fslplan-style-list')
    else:
        form = StyleForm()
    context = {
        'form': form,
        'StyleDATA': StyleDATA,
    }
    return render(request, 'fslplan/style_list.html', context)


@login_required
def style_edit(request, pk):
    StyleDATA = Style.objects.all()
    StyleID = Style.objects.get(id=pk)

    if request.method == 'POST':
        form = StyleForm(request.POST, request.FILES, instance=StyleID)
        if form.is_valid():
            form.save()
            return redirect('fslplan-style-list')
    else:
        form = StyleForm(instance=StyleID)
    context = {
        'form': form,
        'StyleDATA': StyleDATA,
    }
    return render(request, 'fslplan/style_list.html', context)


@login_required
def Buyer_style_list(request,pk):
    ClientData= Buyer.objects.get(id=pk)
    StyleDATA = Style.objects.filter(name=ClientData.id).order_by('name')
    if request.method == 'POST':
        form = StyleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fslplan-style-list')
    else:
        form = StyleForm()
    context = {
        'form': form,
        'StyleDATA': StyleDATA,
    }
    return render(request, 'fslplan/style_list.html', context)


@login_required
def daySetup(request):
	#invoiceNumber=pk
    form = DaysetupForm(request.POST or None)
    #rob = request.POST['lname']
    if request.method == "POST":
        #IDStyle = request.POST['StyleID']
        if form.is_valid():
 
            return redirect('fslplan-daysetup-show')
    context = {
   	'form': form,
    }
    return render(request, 'fslplan/day_setup.html', context)
















login_required
def daySetup_show(request):
    SetupDayData = SetupDay.objects.all().order_by('-date')
    context = {
        'SetupDay': SetupDayData,
    }
    return render(request, 'fslplan/day_setup_show.html', context)









@login_required
def prod_output_show(request):
    enddate = date.today()
    if request.GET:
        SetupLineData = SetupLine.objects.all().order_by('-date')
    else:
        SetupLineData = SetupLine.objects.filter(date=enddate)
    context = {
        'SetupLineData': SetupLineData,
    }
    return render(request,'fslplan/prod_output_show.html', context)


@login_required  # load_buyer
def prod_output_edit(request,pk):
    SetupLineData = SetupLine.objects.get(id=pk)
    if request.method== 'POST':
        form = SetupLineForm(request.POST, instance=SetupLineData)
        if form.is_valid():
            dayData=form.save(commit=False)
            dayData.DayTT=dayData.H_8_9+dayData.H_9_10+dayData.H_10_11+dayData.H_11_12+dayData.H_12_13+dayData.H_14_15+dayData.H_15_16+dayData.H_16_17+dayData.H_17_18+dayData.H_18_19+dayData.H_19_20+dayData.H_20_21+dayData.H_21_22
            dayData.save()
            return redirect('fslplan-prod-output-show')
    else:
        form = SetupLineForm(instance=SetupLineData)
    context = {
        'form': form,
        'SetupLineData':SetupLineData,
		}
    return render(request,'fslplan/prod_output_edit.html', context)