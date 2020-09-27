from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee
def employee_info_view(request):
    employees=Employee.objects.all()
    data={'employees':employees}
    res=render(request,'testapp/employee.html',data)
    return(res)
def greeting(request):
    s="<h>HELLO AND WELCOME TO FIRST APPLICATION</h><p>this is landing page</p>"
    return HttpResponse(s)
def showContact(request):
    s="<h1>this is contact page<h1>"
    s+="<p>Website:my sirg.com</p>"
    s+="<p>Mobile:9090904567</p>"
    s+="<p>mail:somthing.mail.com</p>"
    return HttpResponse(s)
def about(request):
    text="this is an about page"
    return render(request,'testapp/about.html',{'text':text})
