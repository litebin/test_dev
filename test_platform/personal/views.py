from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

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
            auth.login(request,user) #记录用户的登录状态
            return  HttpResponseRedirect("/project/")
#登录成功,默认项目管理页
#@login_required()登录装饰器,根据记录的状态判断是否登录，如果未登录，跳转页面就会失败
@login_required()
def project_manage(request):
    return render(request,"project.html")

#处理用户的退出
def logout(request):
    auth.logout(request) #退出登录,清除session
    return  HttpResponseRedirect("/index/")

#模块管理
def module_manage(request):
    return render(request,"module.html")


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