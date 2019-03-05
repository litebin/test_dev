from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
# Create your views here.

"""
def say_hello(request):
    name = request.GET.get("name","")
    return  HttpResponse("Hello, " + name)
#返回前端name输入的内容
def say_hello(request):
    name = request.GET.get("name","")
    if name == "":
        return HttpResponse("请输入?name=name")
    talk = []
    for n in range(3):
        talk.append("hello:" + name + ", ")
    return  HttpResponse(talk)
#直接返回html   
def say_hello(request):
    name = request.GET.get("name","")
    if name == "":
        return HttpResponse("请输入?name=name")
    html = '<h1 style="color:blue">hello:' + name + "</h1><br> "
    return  HttpResponse(html)
"""
def say_hello(request):
    input_name = request.GET.get("name","")
    if input_name == "":
        return HttpResponse("请输入?name=name")
    return render(request,"index.html",{"name":input_name})

def index(request):
    """
    登录首页
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "index.html")
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        print(username)
        print(password)
        if username == "" or password == "":
            return render(request, "index.html", {"error": "用户名或者密码为空"})

        user = auth.authenticate(username=username,password=password)
        print("user-->",user)
        if user is None:
            return render(request, "index.html", {"error": "用户名或者密码错误"})
        else:
            #return render(request, "manage.html")
            return  HttpResponseRedirect("/manage/")
#登录成功,跳转管理页面
def manage(request):
    return render(request,"manage.html")




"""
def login_action(request):
    
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    print(username)
    print(password)
    if username == "" or password == "":
        return render(request,"index.html",{"error":"用户名或者密码为空"})
    if username =="admin" and password == "admin123":
        return HttpResponse("登录成功")
    else:
        return render(request,"index.html",{"error":"用户名或者密码错误"})
"""