from django.shortcuts import render,reverse,redirect
from django.views.generic import View
# 登录出错给出提示
from django.http import HttpResponse
# django自带用户模型下的表
from django.contrib.auth.models import User
# 登录和登出功能
from django.contrib.auth import logout,login,authenticate
# Create your views here.

# 注册
class Regist(View):
    def get(self,request):
        # 判断用户当前是否登录，如果登录就跳转到首页
        if request.user.is_authenticated:
            # 跳转
            return redirect(reverse('index'))
        return render(request,'register.html')

    def post(self,request):
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        check_password = request.POST.get('check_password','')

        if password != check_password:
            return HttpResponse('密码输入不一致')

        # 判断当前注册帐号是否已经被注册，如果已经被注册，则提示用户重新注册
        exists = User.objects.filter(username=username).exists()
        if exists:
            return HttpResponse('该帐号已被注册')
        User.objects.create_user(username=username,password=password)
        return redirect(reverse('login'))


# 登录
class Login(View):
    def get(self, request):
        return render(request,'login.html')

    def post(self, request):
        # 获取用户输入的，没有获取到就留空
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        # 判断当前用户是否存在，如果不存在则让用户重新注册
        exists = User.objects.filter(username=username).exists()
        if not exists:
            return HttpResponse('该帐号不存在，请重新注册')
        # 验证，如果通过会返回一个用户对象，如果不通过会返回一个none
        user = authenticate(username=username,password=password)
        if user:
            # 如果有值
            login(request,user)
            return redirect(reverse('index'))
        else:
            return HttpResponse('密码错误')


# 网站首页
class Index(View):
    def get(self, request):
        return render(request,'index.html')

    def post(self, request):
        pass


# 用户注销
class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('register'))

    def post(self, request):
        pass


class Sureg(View):
    def get(self, request):

        return render(request,'sureg.html')

    def post(self, request):
        pass


class Info(View):
    def get(self,request,pk):
        # return render(request, 'login.html')
        print(pk)
        return render(request,"info/info_{}.html".format(pk))

    def psot(self,reuqest):
        pass


class News(View):
    def get(self,request,pk):
        # return render(request, 'login.html')
        print(pk)
        return render(request,"news/news_{}.html".format(pk))

    def psot(self,reuqest):
        pass


class Serve(View):
    def get(self,request,pk):
        # return render(request, 'login.html')
        print(pk)
        return render(request,"serve/serve_{}.html".format(pk))

    def psot(self,reuqest):
        pass


class Exchange(View):
    def get(self,request,pk):
        # return render(request, 'login.html')
        print(pk)
        return render(request,"exchange/exchange_{}.html".format(pk))

    def psot(self,reuqest):
        pass


class Ability(View):
    def get(self,request,pk):
        # return render(request, 'login.html')
        print(pk)
        return render(request,"ability/ability_{}.html".format(pk))

    def psot(self,reuqest):
        pass


class Legal(View):
    def get(self,request,pk):
        # return render(request, 'login.html')
        print(pk)
        return render(request,"legal/legal_{}.html".format(pk))

    def psot(self,reuqest):
        pass


# 测试模板继承
def temp4(request):
    cotext={
        'title':"模板继承",
        'title1': "模板继承",
        'title2': "模板继承",
    }
    return render(request,"temp1.html")