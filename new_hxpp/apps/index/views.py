from django.shortcuts import render,reverse,redirect
from django.views.generic import View
from django.utils import timezone
# 登录出错给出提示
from django.http import HttpResponse
# django自带用户模型下的表
from django.contrib.auth.models import User
# 登录和登出功能
from django.contrib.auth import logout,login,authenticate
# 自定义模型类
from .models import UserProfile,UserComment,FormTexi

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

        return render(request,"info/info_{}.html".format(pk))

    def post(self,reuqest):
        pass


class News(View):
    def get(self,request,pk):
        # return render(request, 'login.html')

        return render(request,"news/news_{}.html".format(pk))

    def post(self,reuqest):
        pass


class Serve(View):
    def get(self,request,pk):
        # return render(request, 'login.html')

        return render(request,"serve/serve_{}.html".format(pk))

    def post(self,reuqest):
        pass


class Exchange(View):
    def get(self,request,pk):
        # return render(request, 'login.html')
        pk = int(pk)
        if pk ==2:
            items = UserComment.objects.all()

            return render(request,"exchange/exchange_2.html",{"items":items})

        else:
            return render(request,"exchange/exchange_{}.html".format(pk))

    def post(self,reuqest):
        pass


class ExchangeForm(View):
    def get(self,request):
        pass

    def post(self,request):
        datatime = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        fkauthor = request.POST.get('fkauthor', '')
        fkmotif = request.POST.get('fkmotif','')
        fkwhere = request.POST.get('fkwhere','')
        fkdetails = request.POST.get('fkdetails','')
        fkemail = request.POST.get('fkemail','')

        if (fkauthor and datatime and fkmotif and fkemail and fkwhere and fkdetails):
            # 有则取无则建
            user = UserProfile.objects.get_or_create(username=fkauthor)

            user_profile = FormTexi()
            user_profile.datatime = datatime
            user_profile.fkauthor = user
            user_profile.fkwhere = fkwhere
            user_profile.fkemail = fkemail
            user_profile.fkmotif = fkmotif
            user_profile.fkdetails = fkdetails
            user_profile.save()

        items = FormTexi.objects.all()

        return render(request, "exchange/exchange_2.html", {"items": items})


class Ability(View):
    def get(self,request,pk):
        # return render(request, 'login.html')
        return render(request,"ability/ability_{}.html".format(pk))

    def post(self,reuqest):
        pass


class Legal(View):
    def get(self,request,pk):
        # return render(request, 'login.html')

        return render(request,"legal/legal_{}.html".format(pk))

    def post(self,reuqest):
        pass


# 测试模板继承
def temp4(request):
    cotext={
        'title':"模板继承",
        'title1': "模板继承",
        'title2': "模板继承",
    }
    return render(request,"temp1.html")

# 测试mysql
class UserInfo(View):
    def get(self,request):
        # 创建数据
        # UserProfile.objects.create(username='正心')

        # user = UserProfile(username='笑容')
        # print(timezone.now().strftime("%Y-%m-%d %H:%M:%S"))

        # user = UserProfile()
        # user.username = '山河6'
        # user.save()

        # 查询方法
        user = UserComment.objects.get(id=2)
        items = UserComment.objects.all()
        return render(request, 'UserInfo.html',{'name':user.fkauthor_id,'time':user.datatime,'users':items})

        # Users = UserProfile.objects.all()
        # print(Users)

        # 有则取无则建
        # user = UserProfile.objects.get_or_create(username='马克')

        # 更新方法
        # user = UserProfile.objects.filter(id=1).update(username='更新')

        # 删除方法
        # user = UserProfile.objects.get(id=1)
        # user.delete()

        return render(request,'UserInfo.html')

# 测试mysql表关系
class User_Data(View):
    def get(self,request):
        # user = UserProfile()
        # user.id = 1
        # user.username = '正心'
        # user.save()

        user = UserProfile.objects.get(id=1)
        user_profile = UserComment()
        user_profile.fkauthor = user
        user_profile.motif = '检定收费标准怎么查不到'
        user_profile.datatime = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        user_profile.details = '检定收费标准现在怎么查不到'
        user_profile.restore = '您好，相关检测咨询请致电：7627628。'
        user_profile.save()

        return HttpResponse('successful')

# 测试form表单
class OneForm(View):
    def get(self,request):
        return render(request,'temp2.html')

    def post(self,request):
        fkauthor = request.POST.get('fkauthor', '')
        datatime = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        motif = request.POST.get('motif', '')
        details = request.POST.get('details', '')
        restore = request.POST.get('restore', '')
        print(fkauthor,datatime,motif,details,restore)

        return HttpResponse('fkauthor')