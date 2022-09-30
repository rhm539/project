from weasyprint import HTML
from django.db.models.query_utils import Q
from user.models import Profile, UserType
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from itStock.models import Fund, FundDetail,Supplier
from django.shortcuts import render, redirect
from .forms import FundDetailForm, FundDetailInvForm, FundForm,SupplierForm
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError
from num2words import num2words 
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
###
from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import render_to_string
###############################
from django.template.loader import get_template
from django.core.mail import EmailMessage
####################################
from .invoice_views import date_default, date_enddate, date_startdate
##

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string




##




# Create your views here.
@login_required
def index(request):
    return render(request,'itStock/index.html')



def fund_test(request):
    return render(request,'itStock/test.html')


def fund(request):
	if request.user.profile.utype.utype == 'DptHead':
		posts = Fund.objects.all().filter(department=request.user.profile.department).order_by("-pk")  # fetching all post objects from database
	elif request.user.profile.utype.utype == 'Audit':
		posts = Fund.objects.all().filter(admindpt='mynuddin').order_by(
		    "-pk")  # fetching all post objects from database
	elif request.user.profile.utype.utype == 'GMACC':
		posts = Fund.objects.all().filter(gmacc='moin').order_by(
		    "-pk")  # fetching all post objects from database
	elif request.user.profile.utype.utype == 'MD':
		posts = Fund.objects.all().filter(md='masud').order_by(
		    "-pk")  # fetching all post objects from database
	else:
		posts = Fund.objects.all().filter(staff=request.user.id).order_by("-pk")  # fetching all post objects from database
	
	if request.GET:
		q = request.GET['q']
		todate = request.GET['todate']
		fromdate = request.GET['fromdate']
		enddate = date_enddate(todate)
		startdate = date_startdate(fromdate)
		dataRange = Q(date__range=[startdate, enddate])
		if q:
			multiple_q = Q(Q(unit=q) | Q(
			    fundNumber__icontains=q) | Q(fundName__icontains=q) | Q(status__icontains=q) | Q(fundAmount__icontains=q))
			posts = posts.filter(dataRange & multiple_q).order_by('-pk')
		elif not q:
			posts = posts.filter(dataRange).order_by('-pk')
		else:
			posts = posts.all().order_by('-pk')
	else:
		dateQ = date_default()
		posts = posts.filter(dateQ).order_by('-date')

	context = {

            'fund': posts,
            #'page_obj': page_obj,
        }
	return render(request, 'itStock/fund.html', context)




@login_required
def fund_add(request):
	#context = {}
	MarksFormset = modelformset_factory(FundDetail, form=FundDetailForm)	
	form = FundForm(request.POST or None)
	formset = MarksFormset(request.POST or None, queryset= FundDetail.objects.none(), prefix='funddetail')
	if request.method == "POST":
		if form.is_valid() and formset.is_valid():
			try:
				with transaction.atomic():
					student = form.save(commit=False)
					student.staff = request.user
					#fundNumber=student.fundNumber
					fundAmount=0
					for funddetails in formset:
						data = funddetails.save(commit=False)
						if data.particulars and data.rate and data.quantity  is not None:
							data.staff = request.user
							student.department = request.user.profile.department
							#data.fundNumber = student.fundNumber
							#data.fundNumber=FundForm(request.POST, instance=fundNumber)
							#print(fundNumber)
							amount = float(data.rate) * float(data.quantity)
							data.amount =round(amount,2)
							fundAmount = fundAmount + data.amount
							data.fundSerial=student.fundNumber
							data.fundName=student.fundName
							#data.student = student
							data.unit = student.unit
							data.save()
				student.fundAmount=fundAmount			
				student.save()
				#return redirect('itStock-fund')
			except IntegrityError:
				print("Error Encountered")
			return redirect('itStock-fund')
	context = {
            'formset': formset,
        	'form': form,
		}
	#context['formset'] = formset
	#context['form'] = form
	return render(request, 'itStock/fund_add.html', context)

@login_required    
def fund_show(request,pk):
	context=fund_pro_show(pk)
	return render(request,'itStock/fund_show.html',context)

@login_required    
def fund_view(request,pk):
	context=fund_pro_show(pk)
	return render(request,'itStock/fund_mail.html',context)
#func
def fund_pro_show(pk):
	fund = Fund.objects.get(fundNumber=pk)
	funddetail = FundDetail.objects.all().filter(fundSerial=pk)
	#test=fund.unit
	inword=num2words(fund.fundAmount)+' Taka'
	headofdept=fund.headdept
	audit=fund.admindpt
	gmacc=fund.gmacc
	md=fund.md
	hsignature='NULL'
	auditsig='NULL'
	gmaccsig='NULL'
	mdsig='NULL'

	if fund.status == 'ACCEPT':
		headsig=User.objects.get(username=headofdept)
		headofdeptID=headsig.id
		hsignature=Profile.objects.get(loginuser=headofdeptID)
	
	
	if  fund.status == 'DELIVER':
		headsig=User.objects.get(username=headofdept)
		headofdeptID=headsig.id
		hsignature=Profile.objects.get(loginuser=headofdeptID)

		audituser=User.objects.get(username=audit)
		auditID=audituser.id
		auditsig=Profile.objects.get(loginuser=auditID)

	if fund.status == 'WAITING':
		headsig=User.objects.get(username=headofdept)
		headofdeptID=headsig.id
		hsignature=Profile.objects.get(loginuser=headofdeptID)

		audituser=User.objects.get(username=audit)
		auditID=audituser.id
		auditsig=Profile.objects.get(loginuser=auditID)

		gmaccuser=User.objects.get(username=gmacc)
		gmaccID=gmaccuser.id
		gmaccsig=Profile.objects.get(loginuser=gmaccID)	
	
	if 	fund.status == 'APPROVE':
		headsig=User.objects.get(username=headofdept)
		headofdeptID=headsig.id
		hsignature=Profile.objects.get(loginuser=headofdeptID)

		audituser=User.objects.get(username=audit)
		auditID=audituser.id
		auditsig=Profile.objects.get(loginuser=auditID)

		gmaccuser=User.objects.get(username=gmacc)
		gmaccID=gmaccuser.id
		gmaccsig=Profile.objects.get(loginuser=gmaccID)

		mduser=User.objects.get(username=md)
		mdID=mduser.id
		mdsig=Profile.objects.get(loginuser=mdID)

	context = {
        'funddetail': funddetail,
		'fund':fund,
		'inword': inword,
		'hsignature':hsignature,
		'auditsig': auditsig,
		'gmaccsig': gmaccsig,
		'mdsig': mdsig,
		}
	return context	

@login_required
def fund_item_edit(request, pk):
	funditem = FundDetail.objects.get(id=pk)
	fundSerial=funditem.fundSerial
	fund = Fund.objects.get(fundNumber=fundSerial)
	fundAmount=0
	if request.method== 'POST':
		form = FundDetailForm(request.POST, instance=funditem)
		if form.is_valid():
			funditem = form.save(commit=False)
			funditem.amount=float(funditem.rate) * float(funditem.quantity)
			form.save()
			funddetail = FundDetail.objects.all().filter(fundSerial=fundSerial)
			for funddetail in funddetail:
				amount = float(funddetail.rate) * float(funddetail.quantity)
				funddetail.amount =round(amount,2)
				fundAmount = fundAmount + funddetail.amount
				form.save()
			if fundAmount != 0:
				fund.fundAmount=round(fundAmount,2)
				fund.save()
				return redirect('itStock-fund-show',fundSerial)
	else:
		form = FundDetailForm(instance=funditem)
	context = {
        'form': form,
		'fund': fund,
	}
	return render(request,'itStock/fund_item_edit.html',context)

def fund_item_add(request,pk):
	fund = Fund.objects.get(fundNumber=pk)
	fundSerial=fund.fundNumber
	fundAmount=0
	if request.method == "POST":
		form = FundDetailForm(request.POST)
		if form.is_valid():
			funditem = form.save(commit=False)
			funditem.fundSerial=fundSerial
			funditem.fundName=fund.fundName
			funditem.staff=request.user
			funditem.amount=float(funditem.rate) * float(funditem.quantity)
			funditem.unit = fund.unit
			form.save()
			funddetail = FundDetail.objects.all().filter(fundSerial=fundSerial)
			for funddetail in funddetail:
				amount = float(funddetail.rate) * float(funddetail.quantity)
				funddetail.amount =round(amount,2)
				fundAmount = fundAmount + funddetail.amount
				form.save()
			if fundAmount != 0:
				fund.fundAmount=round(fundAmount,2)
				fund.save()
			return redirect('itStock-fund-show',fundSerial)
			#return redirect('fund_add_item',context)
	else:
		form = FundDetailForm()
	
	context={
		'fund': fund,
		'form':form,
	}
	return render(request,'itStock/fund_add_item.html',context)



@login_required
def fund_item_del(request,pk):
	funditem = FundDetail.objects.get(id=pk)
	fundSerial=funditem.fundSerial
	fund=Fund.objects.get(fundNumber=fundSerial)
	fundAmount=0
	funddetailCount=FundDetail.objects.all().filter(fundSerial=fundSerial).count()
	context={
			'fundSerial':fundSerial,
			'fund':fund,
	}
	if request.method == 'POST':
		funditem.delete()
		funddetail = FundDetail.objects.all().filter(fundSerial=fundSerial)
		if funddetailCount > 1:
			for funddetail in funddetail:
				fundAmount = fundAmount + float(funddetail.amount)
				if fundAmount != 0:
					fund.fundAmount=round(fundAmount,2)
					fund.save()
		else:
			fund.delete()
			return redirect('itStock-fund')
		return redirect('itStock-fund-show',fundSerial)
	return render(request,'itStock/fund_delete.html',context)


def fund_pdf(request, pk):
    context = fund_pro_show(pk)
    #return render(request, 'itStock/fund_pdf.html', context)
    html_string = render_to_string('itStock/fund_pdf.html', context)
    html = HTML(string=html_string).write_pdf()
    #html.write_pdf()
    response = HttpResponse(html, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="home_page.pdf"'
    return response




@login_required
def fund_mail(request,pk,mailOwn,mailUP):
	context=fund_pro_show(pk)
	message = get_template('itStock/fund_mail.html').render(context)
	msg = EmailMessage(
        'Subject: Fund Requisition',
        message,
        'project@fashionstepbd.net',
        [ mailUP, mailOwn],
    )
	msg.content_subtype = "html"  # Main content is now text/html
	msg.send()
	#return redirect('itStock-fund')

@login_required
def fund_submit(request, pk):
	fund = Fund.objects.get(fundNumber=pk)
	funddetail = FundDetail.objects.all().filter(fundSerial=pk)
	if fund.status == 'NEW':
		mailOwn= request.user.email
		mailUP=request.user.profile.department.dptHeadName.email
		fund.headdept= request.user.profile.department.dptHeadName.username
		fund.status= "SEND"
		fund.save()
		for funddetail in funddetail:
			funddetail.status= "SEND"
			funddetail.save()
		fund_mail(request,pk,mailOwn,mailUP)
	elif fund.status == 'SEND':
		mailOwn= request.user.email
		#auditID=UserType.objects.get(utype='Audit')
		uid=UserType.objects.get(utype='Audit')
		louser=Profile.objects.get(utype=uid.id)
		fund.admindpt= louser.loginuser.username
		lo2=User.objects.get(username=louser.loginuser)
		mailUP=lo2.email
		fund.status= "ACCEPT"
		fund.save()
		for funddetail in funddetail:
			funddetail.status= "ACCEPT"
			funddetail.save()
		fund_mail(request,pk,mailOwn,mailUP)
	elif fund.status == 'ACCEPT':
		mailOwn= request.user.email
		#auditID=UserType.objects.get(utype='Audit')
		lo2=User.objects.get(username='moin')
		mailUP=lo2.email
		fund.gmacc=lo2.username
		fund.status= "DELIVER"
		fund.save()
		for funddetail in funddetail:
			funddetail.status= "DELIVER"
			funddetail.save()
		fund_mail(request,pk,mailOwn,mailUP)
	elif fund.status == 'DELIVER':
		mailOwn= request.user.email
		#auditID=UserType.objects.get(utype='Audit')
		lo2=User.objects.get(username='masud')
		mailUP=lo2.email
		fund.md=lo2.username
		fund.status= "WAITING"
		fund.save()
		for funddetail in funddetail:
			funddetail.status= "WAITING"
			funddetail.save()
		fund_mail(request,pk,mailOwn,mailUP)
	elif fund.status == 'WAITING':
		mailOwn= request.user.email
		#auditID=UserType.objects.get(utype='Audit')
		lo2=fund.staff
		lo2a=User.objects.get(username=lo2)
		mailUP=lo2a.email
		fund.status= "APPROVE"
		fund.save()
		for funddetail in funddetail:
			funddetail.status= "APPROVE"
			funddetail.save()
		fund_mail(request,pk,mailOwn,mailUP)
	return redirect('itStock-fund')

@login_required
def fund_myfund(request):
	if request.user.profile.utype.utype == 'Audit' :
		posts = Fund.objects.all().filter(department=request.user.profile.department).order_by("-pk") # fetching all post objects from database
	else:
		posts = Fund.objects.all().filter(staff=request.user.id).order_by("-pk") # fetching all post objects from database
	
	p = Paginator(posts, 5)  # creating a paginator object
    # getting the desired page number from url
	page_number = request.GET.get('page')
	try:
		page_obj = p.get_page(page_number)  # returns the desired page object
	except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
		page_obj = p.page(1)
	except EmptyPage:
        # if page is empty then return last page
		page_obj = p.page(p.num_pages)
	context = {
      
        'fund': posts,
		'page_obj': page_obj,
    } 
	return render(request,'itStock/fund_myfund.html', context)

@login_required
def fund_show_all_item(request):
    if request.GET:
        q = request.GET['q']
        todate = request.GET['todate']
        fromdate = request.GET['fromdate']
        enddate = date_enddate(todate)
        startdate = date_startdate(fromdate)
        dataRange = Q(date__range=[startdate, enddate])
        if q:
            multiple_q = Q(Q(particulars__icontains=q) | Q(buyer__icontains=q) | Q(style__icontains=q) | Q(fundSerial__icontains=q) | Q(remarks__icontains=q))
            funddetail = FundDetail.objects.filter(dataRange & multiple_q).order_by('-id')
        elif not q:
            funddetail = FundDetail.objects.filter(dataRange).order_by('-id')
        else:
            funddetail = FundDetail.objects.all().order_by('-id')
    else:
        dateQ = date_default()
        funddetail = FundDetail.objects.filter(dateQ).order_by('-date')
    context = {
        'funddetail':funddetail,
        }
    return render(request,'itStock/fund_show_all_item.html', context)

@login_required
def fund_item_add_inv(request,pk):
    funddetail = FundDetail.objects.get(id=pk)
    if request.method== 'POST':
        form = FundDetailInvForm(request.POST, instance=funddetail)
        if form.is_valid():
            form.save()
            return redirect('itStock-fund-show-all-item')
    else:
        form = FundDetailInvForm(instance=funddetail)
    context = {
        'form': form,
		}
    return render(request, 'itStock/fund_item_add_inv.html', context)





@login_required
def supplier_add(request):
	supplier = Supplier.objects.all()
	if request.method == 'POST':
		form = SupplierForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('itStock-supplier-add')
	else:
		form = SupplierForm()
	
	context = {
        'form': form,
		'supplier':supplier,
    }
	return render(request,'itStock/supplier_add.html', context)

@login_required
def supplier_edit(request,pk):
    supplier = Supplier.objects.get(id=pk)
    if request.method== 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('itStock-supplier-add')
    else:
        form = SupplierForm(instance=supplier)
    
    context = {
        'form': form,
		}
    return render(request, 'itStock/supplier_edit.html', context)

@login_required
def supplier_delete(request, pk):
    supplier = Supplier.objects.get(id=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('itStock-supplier-add')
    return render(request, 'itStock/supplier_delete.html')

#####################################################################################################################################################


# this is call func 
def fund_find(pk):
	fund = Fund.objects.get(fundNumber=pk)
	funddetail = FundDetail.objects.all().filter(fundSerial=pk)
	#test=fund.unit
	inword=num2words(fund.fundAmount)+' Taka'
	context = {
        'funddetail': funddetail,
		'fund':fund,
		'inword': inword,
		}
	return context


