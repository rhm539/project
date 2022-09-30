from datetime import date, datetime, timedelta
from django.contrib.auth.decorators import login_required
from itStock.models import Invoice, InvoiceDetail
from django.shortcuts import render, redirect
from .forms import InvoiceDetailForm, InvoiceFormPdf, InvoiceItemAddForm, InvoiceItemEditForm,InvoiceForm
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError
from django.db.models import Q
from num2words import num2words 
###
from django.shortcuts import render
###############################
####################################


def date_default():
    enddate = date.today()
    startdate = enddate - timedelta(days=45)
    dateQ = Q(date__range=[startdate, enddate])
    return dateQ


def date_enddate(enddate):
    if not enddate:
        enddate = date.today()
    else:
        enddate = datetime.strptime(enddate, "%m/%d/%Y").strftime('%Y-%m-%d')
    return enddate


def date_startdate(startdate):
    if not startdate:
        startdate = '2021-06-01'
    else:
        startdate = datetime.strptime(startdate, "%m/%d/%Y").strftime('%Y-%m-%d')
    return startdate
        
    

@login_required
def invoice_item_delete(request, pk):
    invoiceDetail = InvoiceDetail.objects.get(id=pk)
    invoiceNumber=invoiceDetail.invoiceNumber
    invoice=Invoice.objects.get(invoiceNumber=invoiceNumber)
    invoiceitemCount=InvoiceDetail.objects.all().filter(invoiceNumber=invoiceNumber).count()
    price=0
    if request.method == 'POST':
        invoiceDetail.delete()
        invoiceItemSum=InvoiceDetail.objects.all().filter(invoiceNumber=invoiceNumber)
        if invoiceitemCount > 1:
            for invoiceItemSum in invoiceItemSum:
                price= price + float(invoiceItemSum.price)
            if price != 0:
                invoice.totalAmount=price
                invoice.save()
        else:
             invoice.delete()
             return redirect('itStock-invoice-list')    
        return redirect('itStock-invoice-view', invoiceNumber)
    context = {
        'invoiceItemDetail':invoiceDetail,
        }
    #return render(request,'itStock/invoice_view.html',context)
    return render(request, 'itStock/invoice_item_delete.html',context)

@login_required
def invoice_add_item(request,pk):
    invoiceNumber = pk
    invoice=Invoice.objects.get(invoiceNumber=invoiceNumber)
    price=0
    if request.method== 'POST':
        form = InvoiceItemAddForm(request.POST, request.FILES)
        if form.is_valid():
            invoiceItem=form.save(commit=False)
            invoiceItem.price=float(invoiceItem.unitprice) * float(invoiceItem.quantity)
            if invoiceItem.price >1:
                invoiceItem.invoiceNumber=invoiceNumber
                form.save()
                invoiceItemSum=InvoiceDetail.objects.all().filter(invoiceNumber=invoiceNumber)
                for invoiceItemSum in invoiceItemSum:
                    price= price + float(invoiceItemSum.price)
                invoice.totalAmount=price
                invoice.save() 
            return redirect('itStock-invoice-view', invoiceNumber)
    else:
        form = InvoiceItemAddForm()
    context = {
        'form': form,
        'invoiceItemDetail':invoice,
		}
    return render(request,'itStock/invoice_add_item.html', context)

@login_required
def invoice_item_edit(request,pk):
    invoiceItemDetail = InvoiceDetail.objects.get(id=pk)
    invoice=Invoice.objects.get(invoiceNumber=invoiceItemDetail.invoiceNumber)
    price=0
    invoiceNumber=invoiceItemDetail.invoiceNumber
    if request.method== 'POST':
        form = InvoiceItemEditForm(request.POST, request.FILES,instance=invoiceItemDetail)
        if form.is_valid():
            invoiceItemDetail=form.save(commit=False)
            invoiceItemDetail.price=float(invoiceItemDetail.unitprice) * float(invoiceItemDetail.quantity)
            if invoiceItemDetail.price >1:
                form.save()
                invoiceItemSum=InvoiceDetail.objects.all().filter(invoiceNumber=invoiceNumber)
                for invoiceItemSum in invoiceItemSum:
                    price= price + float(invoiceItemSum.price)
                invoice.totalAmount=price
                invoice.save()    
            return redirect('itStock-invoice-view', invoiceNumber)
    else:
         form = InvoiceItemEditForm(instance=invoiceItemDetail)
    context = {
        'form': form,
        'invoiceItemDetail':invoiceItemDetail,
               }
    return render(request,'itStock/invoice_item_edit.html',context)


@login_required #Search
def invoice_list_item(request):
    if request.GET:
        q = request.GET['q']
        todate = request.GET['todate']
        fromdate = request.GET['fromdate']
        enddate = date_enddate(todate)
        startdate = date_startdate(fromdate)
        dataRange = Q(date__range=[startdate, enddate])
    
        if q:
            multiple_q = Q(Q(productName__icontains=q)|Q(macaddress__icontains=q)|Q(invoiceNumber__icontains=q))
            invoicedetail = InvoiceDetail.objects.filter(dataRange & multiple_q).order_by('-date')
        elif not q:
            invoicedetail = InvoiceDetail.objects.filter(dataRange).order_by('-date')
        else:
            invoicedetail = InvoiceDetail.objects.all().order_by('-date')
    
    else:
        dateQ = date_default()
        invoicedetail = InvoiceDetail.objects.filter(dateQ).order_by('-date')
    context = {
            'invoicedetail':invoicedetail,
        }
    return render(request,'itStock/invoice_list_item.html', context)



@login_required
def invoice_list(request):
    if request.GET:
        q = request.GET['q']
        todate = request.GET['todate']
        fromdate = request.GET['fromdate']
        enddate = date_enddate(todate)
        startdate = date_startdate(fromdate)
        dataRange = Q(date__range=[startdate, enddate])
        if q:
            multiple_q = Q(Q(unit=q) |
                           Q(invoiceNumber__icontains=q) | Q(status=q) | Q(totalAmount__icontains=q))
            invoice = Invoice.objects.filter(dataRange & multiple_q).order_by('-date')
        elif not q:
            invoice = Invoice.objects.filter(
                dataRange).order_by('-date')
        else:
            invoice = Invoice.objects.all().order_by('-date')
    else:
        dateQ = date_default()
        invoice = Invoice.objects.filter(dateQ).order_by('-date')
    context = {
		'invoice':invoice,
    }
    return render(request,'itStock/invoice_list.html', context)
    





@login_required
def invoice_edit(request,pk):
    invoice = Invoice.objects.get(id=pk)
    if request.method== 'POST':
        form = InvoiceFormPdf(request.POST, request.FILES,instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('itStock-invoice-list')
    else:
        form = InvoiceFormPdf(instance=invoice)
    
    context = {
        'form': form,
		}
    return render(request, 'itStock/invoice_edit.html', context)



@login_required
def invoice_item_add(request):
	#invoiceNumber=pk
    context = {}
    MarksFormset = modelformset_factory(InvoiceDetail, form=InvoiceDetailForm)	
    form = InvoiceForm(request.POST or None)
    formset = MarksFormset(request.POST or None, queryset= InvoiceDetail.objects.none(), prefix='ivoicedetail')
    if request.method == "POST":
        if formset.is_valid():
            try:
                with transaction.atomic():
                    student = form.save(commit=False)
                    student.staff = request.user
                    #student.date = datetime.strptime(student.date, "%m/%d/%Y").strftime('%Y-%m-%d')
					#fundNumber=student.fundNumber
                    invoiceAmount=0
                    for invoicedetails in formset:
                        data = invoicedetails.save(commit=False)
                        if data.productName and data.unitprice and data.quantity  is not None:
                            data.staff = request.user
							#data.fundNumber = student.fundNumber
							#data.fundNumber=FundForm(request.POST, instance=fundNumber)
							#print(fundNumber)
                            price = float(data.unitprice) * float(data.quantity)
                            data.price =round(price,2)
                            invoiceAmount = invoiceAmount + data.price
                            data.invoiceNumber=student.invoiceNumber
                            data.save()
                student.totalAmount=invoiceAmount			
                student.save()
            except IntegrityError:
                print("Error Encountered")
            return redirect('itStock-invoice-list')
    context['formset'] = formset
    context['form'] = form
    return render(request, 'itStock/invoice_add.html',context)


@login_required
def invoice_view(request,pk):
    invoicedetail = InvoiceDetail.objects.all().filter(invoiceNumber=pk)
    invoice=Invoice.objects.get(invoiceNumber=pk)
    #fq = FundDetail.objects.filter(invoiceNumber=invoicedetail.invoiceNumber)
    #funddetailtest = fq.fundSerial
    #funddetailtest=0
    #iq = invoice.id
    #funddetail = FundDetail.objects.first(invoiceNumber=invoice.id)
    #funddetailtest = funddetail.fundSerial
    inword=num2words(invoice.totalAmount)+' Taka'
    context = {
        'invoicedetail': invoicedetail,
		'invoice' : invoice,
		'inword':inword,
        #'funddetailtest': funddetailtest,
        }
    return render(request,'itStock/invoice_view.html',context)








@login_required
def invoice_pdf(request):
	return render(request,'itStock/invoice_pdf.html')






