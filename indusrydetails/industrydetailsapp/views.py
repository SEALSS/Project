from industrydetailsapp.models import user, company_details
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
import time
import os
import uuid


# Create your views here.

def Signin(request):
    return render(request, 'industrydetails/Signin.html', {})


def Signup(request):
    return render(request, 'industrydetails/Signup.html', {})


def Details_Form(request):
    return render(request, 'industrydetails/Details_Form.html', {})


def ssignupdetails(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        number = request.POST.get('number')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        flage=1
        for e in user.objects.all():
            if (e.email == email):
                flage = 0
                context = {
                    's2': e.email
                }

        if (flage == 1):
            if (password == confirmpassword):

                email = request.POST.get('email')

                request.session["test"] = email

                data1 = user(username=username, email=email, number=number, password=password)
                data1.save()
                return redirect('Signin')
            else:
                err = 'Password not matching'
                return render(request, 'industrydetails/Signup.html', {'err': err})
        else:
            errmail = 'Email already exist'
            return render(request, 'industrydetails/signup.html', {'errmail': errmail})


    else:
        return render(request, 'industrydetails/Signup.html', {})




# ------------------------------------------------------------------------------





def ssignindetails(request):
    global display_email
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        request.session["test"] = email
        display_email = request.session["test"]

        if email == "admin" and password == "admin_pass":
            return redirect('admin')

        flag = 0
        for e in user.objects.all():

            if e.email == email and e.password == password:
                flag = 1
                context = {
                    's2': e.email
                }

        if flag == 1:
            # cluster_data_signin = Cluster.objects.all()
            return render(request, 'industrydetails/Details_Form.html')

        else:
            clk = 'Please Enter valid Email or Password'
            return render(request, 'industrydetails/Signin.html', {'clk': clk})

def submitdetails(request):
    # global display_email
    # ------- Ramdom-Id---------
    stringLength = 8
    randomString = uuid.uuid4().hex  # get a random string in a UUID fromat
    randomString = randomString.upper()[0:stringLength]  # convert it in a uppercase letter and trim to your size.
    # ------- Ramdom-Id---------
    id = randomString
    # email = display_email

    if request.method == "POST":
        company_name = request.POST.get('company_name')
        business_entity = request.POST.get('business_entity')
        company_address = request.POST.get('company_address')
        pincode = request.POST.get('pincode')
        about = request.POST.get('about')
        keycontact = request.POST.get('keycontact')
        website = request.POST.get('website')
        founded_date = request.POST.get('founded_date')
        number_of_employees = request.POST.get('number_of_employees')
        transport_type = request.POST.get('transport_type')
        clients = request.POST.get('clients')
        office_time_from = request.POST.get('office_time_from')
        office_time_to = request.POST.get('office_time_to')
        factory_time_from = request.POST.get('factory_time_from')
        factory_time_to = request.POST.get('factory_time_to')
        core_operation = request.POST.get('core_operation')
        certifications = request.POST.get('certifications')
        awards = request.POST.get('awards')
        overall_area = request.POST.get('overall_area')
        built_area = request.POST.get('built_area')
        shop_area = request.POST.get('shop_area')

        data2 = company_details(company_name=company_name, id=id, business_entity=business_entity, company_address=company_address, pincode=pincode, about=about, keycontact=keycontact, website=website, founded_date=founded_date, number_of_employees=number_of_employees, transport_type=transport_type, clients=clients, office_time_from=office_time_from, office_time_to=office_time_to, factory_time_from=factory_time_from, factory_time_to=factory_time_to, core_operation=core_operation, certifications=certifications, awards=awards, overall_area=overall_area, built_area=built_area, shop_area=shop_area)
        data2.save()

    return render(request, 'industrydetails/Recorded.html')
