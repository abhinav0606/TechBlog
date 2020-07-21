from django.shortcuts import render
from django.http import HttpResponse,request
from .model import registration
import smtplib
l=[]
login={}
list_of_registration=registration.objects.all()
for i in list_of_registration:
    l.append(i.username)
for i in list_of_registration:
    login[i.username]=i.password
def lgn_rgstr(request):
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
        if name!='default':
            if username in l:
                return render(request,'lgn_rgstr.html',{'message':"The Username already Exist Enter Any other one"})
            elif password!=passwordc:
                return render(request,'lgn_rgstr.html',{'message':'The Password Doesnot matched May be some some typing error'})
            else:
                if genderm=='male':
                    registration(name=name,mobile=mobile,email=email,username=username,password=password,gender='Male',type_user=type).save()
                if genderf=='female':
                    registration(name=name, mobile=mobile, email=email, username=username, password=password, gender='Female',type_user=type).save()
                if genderp=='other':
                    registration(name=name, mobile=mobile, email=email, username=username, password=password, gender='Other',type_user=type).save()
                server=smtplib.SMTP('smtp.gmail.com','587')
                server.ehlo()
                server.starttls()
                Subject="Thanks For Registering"
                server.login("<email>", "<password>")
                Message=f"Thanks {name} for registering into TechBlogs.We will notify you regarding any updates \n\n\n\n Regards \n Team TechBlogs"
                msg='Subject:{}\n\n{}'.format(Subject,Message)
                server.sendmail("weatherappabhinavcreations@gmail.com",email,msg)
                server.close()
        if username_lgn!='default':
            if username_lgn in l:
                if password_lgn==login[username_lgn]:
                    return HttpResponse("Homepage")
                else:
                    return render(request,'lgn_rgstr.html',{'message':'Wrong Password Try Again'})
            else:
                return render(request,'lgn_rgstr.html',{'message':'This User Doesnot Exist Please Create Account First'})
    return render(request,'lgn_rgstr.html',{'message':''})
