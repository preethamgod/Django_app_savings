
from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_protect
from . import models
from .models import my_savings
from django.db.backends import sqlite3
from savingstrack.forms import SavingsForm, AddForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.conf.urls import include, url
from django.contrib import auth
from django.contrib.auth.models import User




class Savings(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    @login_required
    def my_savings(request):
        if not request.user.is_authenticated:
            print("Not Logged in")
            redirect('/login/', include('django.contrib.auth.urls'))

        else:
            print("logged in")
            username1 = request.user.username
            print(" logged in user is :", username1)
            user_id = User.objects.get(username=username1).pk

            form = SavingsForm()
            form1 = AddForm()

            abill = form.default_month
            year1 = form.year
            tran_date1 = str(year1)+"-"+"07"

            # return render(request,'index.html',{'form':form})
            if request.method == 'POST':
                form = SavingsForm(request.POST)
                if form.is_valid():
                    abill = form.cleaned_data['savingsmn']
                    year1 = form.cleaned_data['year1']
                    tran_date1 = abill + "-"+ str(year1)


            query_results = my_savings.objects.filter(sa_id=user_id,transaction_date__contains=tran_date1)

            # return HttpResponse(abill)
            print(query_results)
            return render(request, 'bill.html',
                          {'query_results': query_results, 'abill': abill, 'year1': year1, 'form': form, 'form1': form1,
                           'user': username1})

    @login_required
    def AddBill(request):
        if not request.user.is_authenticated:
            return redirect('/login/', include('django.contrib.auth.urls'))

        username1 = request.user.username
        Add_details = my_savings.objects.create()

        user_id = User.objects.get(username=username1).pk
        print(user_id)


        Add_details.sa_id = user_id

        if request.method == 'POST':
            form1 = AddForm(request.POST)
            abill = request.POST.get('abillmn', False)
            year1 = request.POST.get('ayear', False)
            if form1.is_valid():
                Add_details.name = form1.cleaned_data['tran_name']
                Add_details.transaction_date = form1.cleaned_data['tran_date']
                Add_details.transaction_amt = form1.cleaned_data['tran_amt']
                if form1.cleaned_data['tran_type'] == '1':
                    Add_details.tran_type = 'Income'
                else:
                    Add_details.tran_type = 'Expense'
                Add_details.save()
        # return HttpResponseRedirect("/bill")
        query_results = my_savings.objects.filter(sa_id =user_id)
        # return HttpResponse(form.billmn)
        return render(request, 'bill1.html',
                      {'query_results': query_results, 'abill': abill, 'year1': year1, 'form1': form1})
        # return redirect('bill', {'abill': abill})
        # Add_details = my_bill.objects.create(bill=abill,utility=Addbillmn,completed=AddPaid,completed_date=AddPaiddate)
        # a=Add_details.save()

    @login_required
    def DelBill(request, item_id):
        if not request.user.is_authenticated:
            return redirect('/login/', include('django.contrib.auth.urls'))

        username1 = request.user.username
        user_id = User.objects.get(username=username1).pk
        deldate = my_savings.objects.filter(id=item_id).values('transaction_date')
        a = deldate[0]
        year1 = a['transaction_date'].year
        abill = a['transaction_date'].strftime("%B")


        delmb = my_savings.objects.get(id=item_id)
        query_results = my_savings.objects.filter(sa_id=user_id)
        delmb.delete()
        form1 = AddForm()
        return render(request, 'bill1.html',
                      {'query_results': query_results, 'abill': abill, 'year1': year1, 'form1': form1})

    def logout_request(request):
        auth.logout(request)
        return redirect('/login/', include('django.contrib.auth.urls'))
