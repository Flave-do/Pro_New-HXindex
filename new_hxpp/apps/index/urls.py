from django.urls import path
from .views import *
urlpatterns = [
    path('',Regist.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('index/',Index.as_view(),name='index'),
    path('logout/',LogoutUser.as_view(),name='logout'),
    path('sureg/',Sureg.as_view(),name='sureg'),
    # 5个导航标签
    path('info/<pk>/',Info.as_view()),
    path('news/<pk>/',News.as_view()),
    path('serve/<pk>/', Serve.as_view()),
    path('exchange/<pk>/', Exchange.as_view(),name='exchange/<pk>/'),
    path('exchangform/', ExchangeForm.as_view(),name='exchangeform'),
    path('ability/<pk>/', Ability.as_view()),
    path('legal/<pk>/', Legal.as_view()),
    # 测试模板继承
    path('temp4/',temp4 ),
    # 测试mysql数据库
    path('userinfo/', UserInfo.as_view()),
    path('userdata/', User_Data.as_view()),
    # 测试form表单
    path('temp2/',Exchange.as_view(),name='temp5' ),
    path('temp3/',Register.as_view(),name='register' )

]