from django.shortcuts import render
from django.http import HttpResponse
def ajith (request):
    a="<h1>Welcome to Django</h1>"
    return HttpResponse(a)

def ak (request):
    return HttpResponse ("helooooooooo")

def pavi (request):
    return HttpResponse("<h1>AjithPavi</h1>")

def new(request):
    return render (request,"ak.html",{"NAME":"DJANGO"})

# def pro (request):
#     return render (request,"ak.html",{"ID":234567})

# def product(request):
#     mobile=int (request.GET["mobile"])
#     keyword=int (request.GET["keyword"])
#     monitor=int (request.GET["monitor"])
#     price=monitor+keyword+mobile
#     return render(request,"result.html",{"Price":price})

def stu (request):
    return render (request,"ak.html")


def student(request):
    Name=str(request.GET["Name"])
    Maths=int(request.GET["Maths"])
    English=int(request.GET["English"])
    Social=int(request.GET["Social"])
    Science=int(request.GET["Science"])
    Tamil=int(request.GET["Tamil"])+
    +




























































































    
    Total=Maths+English+Social+Science+Tamil
    Average=(Total/5)
    # name=Name
    # maths=Maths
    # science=Science
    # social=Social
    # english=English
    return render(request,"result.html",{"Total":Total,"Average":Average,"Name":Name,"Maths":Maths,"Science":Science,"Social":Social,"English":English,"Tamil":Tamil})