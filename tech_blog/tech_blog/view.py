from django.shortcuts import render
from django.http import HttpResponse,request
from .model import registration
import smtplib
import xlsxwriter
def lgn_rgstr(request):
    l = []
    login = {}
    list_of_registration = registration.objects.all()
    email_list = []
    for i in list_of_registration:
        email_list.append(i.email)
    for i in list_of_registration:
        l.append(i.username)
    for i in list_of_registration:
        login[i.username] = [i.password, i.type_user]
    if request.method=='POST':
        name=request.POST.get('name','default')
        mobile=request.POST.get('mobile','default')
        email=request.POST.get('email','default')
        username=request.POST.get('username','default')
        password=request.POST.get('password','default')
        passwordc=request.POST.get('passwordc','default')
        genderm=request.POST.get('genderm','default')
        genderf=request.POST.get('genderf','default')
        genderp=request.POST.get('genderp','default')
        type=request.POST.get('type','default')
        username_lgn=request.POST.get('text','default')
        password_lgn=request.POST.get('password_lgn','default')
        typel=request.POST.get('typel','default')
        if name!='default':
            if username in l:
                return render(request,'lgn_rgstr.html',{'message':"The Username already Exist Enter Any other one"})
            elif email in email_list:
                return render(request,'lgn_rgstr.html',{'message':'Email Already Registered'})
            elif password!=passwordc:
                return render(request,'lgn_rgstr.html',{'message':'The Password Doesnot matched May be some some typing error'})
            else:
                try:
                        server = smtplib.SMTP('smtp.gmail.com', '587')
                        server.ehlo()
                        server.starttls()
                        Subject = "Thanks For Registering"
                        server.login("weatherappabhinavcreations@gmail.com", "weatherapp@abhinavcreations")
                        Message = f"Thanks {name} for registering into TechBlogs.We will notify you regarding any updates \n\n\n\n Regards \n Team TechBlogs"
                        msg = 'Subject:{}\n\n{}'.format(Subject, Message)
                        server.sendmail("weatherappabhinavcreations@gmail.com", email, msg)
                        server.close()
                        if genderm == 'male':
                            registration(name=name, mobile=mobile, email=email, username=username, password=password,
                                         gender='Male', type_user=type).save()
                        if genderf == 'female':
                            registration(name=name, mobile=mobile, email=email, username=username, password=password,
                                         gender='Female', type_user=type).save()
                        if genderp == 'other':
                            registration(name=name, mobile=mobile, email=email, username=username, password=password,
                                         gender='Other', type_user=type).save()

                except:
                        return render(request,'lgn_rgstr.html',{'message':"Please Enter a valid mail"})
        if username_lgn!='default':
            if username_lgn in l:
                if password_lgn==login[username_lgn][0]:
                    if typel==login[username_lgn][1]:
                        return HttpResponse("Home Page")
                    else:
                        return render(request,'lgn_rgstr.html',{'message':"Everything is Correct but the user type is incorrect."})
                else:
                    return render(request,'lgn_rgstr.html',{'message':'Wrong Password Try Again'})
            else:
                return render(request,'lgn_rgstr.html',{'message':'This User Doesnot Exist Please Create Account First'})
    return render(request,'lgn_rgstr.html',{'message':''})

def excell(request):
    Register_login=xlsxwriter.Workbook("Registration.xlsx")
    excell=Register_login.add_worksheet()
    excell.set_column(0, 5, 30)
    excell.write(0,0,"Name")
    excell.write(0,1,'Email')
    excell.write(0,2,"Mobile")
    excell.write(0,3,"Username")
    excell.write(0,4,'Gender')
    excell.write(0,5,'Type')
    list=registration.objects.all()
    for i in range(len(list)):
        excell.write(i+1, 0, list[i].name)
        excell.write(i+1, 1, list[i].email)
        excell.write(i+1, 2, list[i].mobile)
        excell.write(i+1, 3, list[i].username)
        excell.write(i+1, 4, list[i].gender)
        excell.write(i+1, 5, list[i].type_user)
    Register_login.close()
    return HttpResponse("Updated the Excell Sheet")
