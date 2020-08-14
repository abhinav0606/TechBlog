from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from django.http import HttpResponseRedirect
from .model import registration,blog,writer
from django.core.mail import send_mail
import base64
import smtplib
import xlsxwriter
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as lg
from django.contrib.auth import logout,authenticate
from django.contrib.auth.models import User
from django.contrib.sessions.backends.base import SessionBase
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.template.defaultfilters import linebreaks,linebreaksbr
def lgn_rgstr(request):
    nt=""
    if request.GET:
        nt=(request.GET.get('next'))
    l = []
    login = {}
    list_of_registration = registration.objects.all()
    email_list = []
    list_of_writer=writer.objects.all()
    email_writer=[]
    username_writer=[]
    for i in list_of_writer:
        username_writer.append(i.username1)
    for i in list_of_writer:
        email_writer.append(i.email1)
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
                return render(request,'lgn_rgstr.html',{'message':"The Username already Exist Enter Any other one",'next':nt})
            elif email in email_list:
                return render(request,'lgn_rgstr.html',{'message':'Email Already Registered','next':nt})
            elif password!=passwordc:
                return render(request,'lgn_rgstr.html',{'message':'The Password Doesnot matched May be some some typing error','next':nt})
            else:
                try:
                    if type=="Reader":
                        server = smtplib.SMTP('smtp.gmail.com', '587')
                        server.ehlo()
                        server.starttls()
                        Subject = "Thanks For Registering"
                        server.login("<email>", "<password>")
                        Message = f"Thanks {name} for registering into TechBlogs.We will notify you regarding any updates \n\n\n\n Regards \n Team TechBlogs"
                        msg = 'Subject:{}\n\n{}'.format(Subject, Message)
                        server.sendmail("weatherappabhinavcreations@gmail.com", email, msg)
                        server.close()
                        if genderm == 'male':
                            registration(name=name, mobile=mobile, email=email, username=username, password=password,
                                         gender='Male', type_user=type).save()
                            u=User.objects.create_user(username,email,password)
                            u.name = name
                            u.save()
                        if genderf == 'female':
                            registration(name=name, mobile=mobile, email=email, username=username, password=password,
                                         gender='Female', type_user=type).save()
                            u=User.objects.create_user(username,email,password)
                            u.name = name
                            u.save()
                        if genderp == 'other':
                            registration(name=name, mobile=mobile, email=email, username=username, password=password,
                                         gender='Other', type_user=type).save()
                            u=User.objects.create_user(username,email,password)
                            u.name=name
                            u.save()
                    else:
                        if username in username_writer:
                            return render(request,"lgn_rgstr.html",{"message":"This Username is Already in queue",'next':nt})
                        elif email in email_writer:
                            return render(request,"lgn_rgstr.html",{'message':"This email is already in queue",'next':nt})
                        else:
                            server=smtplib.SMTP("smtp.gmail.com",'587')
                            server.ehlo()
                            server.starttls()
                            Subject = "Thanks For Registering"
                            server.login("<email>", "<password>")
                            Message = f"Thanks {name} for registering into TechBlogs.Your Application is under review,for procedding the application fastly you just send me the list of programming languages that you know or some of your work in technical field\n\nYou will be updated regarding the Acceptance and Rejection of your application\n\n\n\n Regards \n Team TechBlogs"
                            msg = 'Subject:{}\n\n{}'.format(Subject, Message)
                            server.sendmail("weatherappabhinavcreations@gmail.com", email, msg)
                            server.close()
                            # another server
                            s=smtplib.SMTP("smtp.gmail.com","587")
                            s.ehlo()
                            s.starttls()
                            subject="New Application for Writter"
                            s.login("<email>","<password>")
                            m=f"Name:{name}\nemail:{email}\nphone_number:{mobile}"
                            ms="Subject:{}\n\n{}".format(subject,m)
                            s.sendmail("weatherappabhinavcreations@gmail.com","abhinavgangrade0606@gmail.com",ms)
                            s.close()
                            if genderm == 'male':
                                writer(name1=name, mobile1=mobile, email1=email, username1=username, password1=password,
                                             gender1='Male', type_user1=type).save()
                            if genderf == 'female':
                                writer(name1=name, mobile1=mobile, email1=email, username1=username, password1=password,
                                             gender1='Female', type_user1=type).save()
                            if genderp == 'other':
                                writer(name1=name, mobile1=mobile, email1=email, username1=username, password1=password,
                                             gender1='Other', type_user1=type).save()
                            return render(request,"lgn_rgstr.html",{'message':"Process Under Review Check Your Mail",'next':nt})

                except:
                        return render(request,'lgn_rgstr.html',{'message':"Please Enter a valid mail",'next':nt})
        if username_lgn!='default':
            if username_lgn in l:
                if password_lgn==login[username_lgn][0]:
                    if typel==login[username_lgn][1]:
                        user=authenticate(request,username=username_lgn,password=password_lgn)
                        request.session.set_expiry(600)
                        lg(request,user)
                        if nt=="":
                            return HttpResponseRedirect('TechBlog/')
                        else:
                            return HttpResponseRedirect(nt)
                    else:
                        return render(request,'lgn_rgstr.html',{'message':"Everything is Correct but the user type is incorrect.",'next':nt})
                else:
                    return render(request,'lgn_rgstr.html',{'message':'Wrong Password Try Again','next':nt})
            else:
                return render(request,'lgn_rgstr.html',{'message':'This User Doesnot Exist Please Create Account First','next':nt})
    return render(request,'lgn_rgstr.html',{'message':'','next':nt})
@login_required(login_url="/")
def excell(request):
    if request.user.is_authenticated:
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
    else:
        return HttpResponse("Do the login first")
def home(request):
    if request.user.is_authenticated:
        BLogs = blog.objects.all()[::-1][:5]
        print(BLogs)
        return render(request, 'Home2.html', {'blogg': BLogs})
    else:
        return HttpResponseRedirect("/")
def about(request):
    return render(request,"Developers.html")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/")
def log(request):
    logout(request)
    for sesskey in request.session.keys():
        del request.session[sesskey]
    return HttpResponseRedirect("/")
def admin(request):
    write=writer.objects.all()[::-1]
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if username=="<username>" and password=="<password>":
            return render(request,"admin.html",{"Fundamental":False,"write":write})
        else:
            return HttpResponse("Password is Incorrect")
    return render(request,"admin.html",{"Fundamental":True})
def accepts(request,username):
    details=writer.objects.filter(username1=username)
    registration(name=details[0].username1, mobile=details[0].mobile1, email=details[0].email1, username=details[0].username1, password=details[0].password1,
                 gender=details[0].gender1, type_user=details[0].type_user1).save()
    u=User.objects.create_user(details[0].username1,details[0].email1,details[0].password1)
    u.name=details[0].name1
    u.save()
    server=smtplib.SMTP("smtp.gmail.com","587")
    server.ehlo()
    server.starttls()
    server.login("<email>","<password>")
    Subject="Application for writer at TechBlogs"
    Message=f"Your Application has been Accepted,Now you can login with the registered username and password\nIncase you forgot here it is\n\nUsername:{details[0].username1}\nPassword:{details[0].password1}\n\n\nThanks\n\nRegards TechBlog"
    msg="Subject:{}\n\n{}".format(Subject,Message)
    server.sendmail("weatherappabhinavcreations@gmail.com",details[0].email1,msg)
    server.close()
    details.delete()
    return HttpResponseRedirect("/adm")
def rejects(request,username):
    details=writer.objects.filter(username1=username)
    server=smtplib.SMTP("smtp.gmail.com","587")
    server.ehlo()
    server.starttls()
    server.login("<email>","<>")
    Subject="Application for writer at TechBlogs"
    Message=f"Sorry To say but your application to contribute as a writter at TechBlog is not accepted,but you can have the access of the blog as a reader.....\n\nThanks\nRegrads TechBlog"
    msg="Subject:{}\n\n{}".format(Subject,Message)
    server.sendmail("weatherappabhinavcreations@gmail.com",details[0].email1,msg)
    server.close()
    details.delete()
    return HttpResponseRedirect("/adm")
@login_required(login_url="/")
def blogg(request):
    blogs=blog.objects.all()[::-1]
    return render(request,"blogs.html",{"blog":blogs})
@login_required(login_url="/")
def writ_the_blog(request):
    u=registration.objects.filter(username=request.user)[0].type_user
    if u=="Writer":
        if request.method=="POST":
            a=request.POST
            blog(title=a.get("title",""),language=a.get("language",""),description=a.get("desc",""),main=a.get("main",""),
                 code=a.get("code",""),output=a.get("output",""),writer_name=a.get("w","")).save()
        return render(request,"Write_blog.html")
    else:
        return HttpResponse("<div style:'text-align:center'>You Are a Reader You are not supposed to contribute as writer<br><a href='/logout/'>Home Page</a></div>")
@login_required(login_url="/")
def full_blog(request,title):
    x=blog.objects.filter(title=title)
    return render(request,"Full_blog.html",{'x':x[0]})
