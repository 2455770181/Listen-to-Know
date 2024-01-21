from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from basic_function import models
import uuid
import requests

# requests模块用于发起网络请求
# 简单起见，使用uuid生成token
# Create your views here.

"""
    小程序访问的是API，不能直接写视图函数。
"""


# 登录时调用的接口
class LoginView(APIView):
    # 若请求方式为post，则获取传递的参数用request.data；若请求方式为get，则获取传递的参数用request.query_params。
    # 若传递的参数为字典，则用request.data.get('键名')或request.query_params.get('键名')获取其值。
    def post(self, request, *args, **kwargs):

        data = {
            'appid': request.data.get('appid'),
            'secret': request.data.get('secret'),
            'js_code': request.data.get('js_code'),
            'grant_type': request.data.get('grant_type')
        }
        # 前端通过 wx.login 接口获得临时登录凭证 code 后传到开发者服务器调用此接口获取登录凭证
        # requests.get(url,params=None,**kwargs)
        # Requests库有两个重要对象，分别是Request和Response。Request对象对应的是请求，向目标网址发送一个请求访问服务。而Response对象，是包含了爬虫返回的内容。
        login_info = requests.get("https://api.weixin.qq.com/sns/jscode2session", params=data)
        if not login_info:
            return Response("无法获取code2session的返回信息。")
        openid = login_info.json().get('openid')
        session_key = login_info.json().get('session_key')
        if not openid and not session_key:
            return Response("无法获取openid和session_key")

        # 获取到openid和session_key后去数据库比较openid，如果存在则登录，否则注册
        user_object, if_created = models.TbUser.objects.get_or_create(user_openid=openid)
        # if_created表示是否创建了新的数据，如果是 True 则表示创建了新的数据，否则表示获取到的是已存在的数据。
        user_object.user_session_key = session_key
        user_object.user_token = str(uuid.uuid4())
        user_object.save()
        if not if_created:
            operation = "登录"
        else:
            operation = "注册"
        print("openid:", openid, "session_key:", session_key, "token:", user_object.user_token, "操作:", operation)
        """
            这种写法也可以：
            user = models.TbUser.objects.filter(user_openid=openid).first()
            if not user:
                models.TbUser.objects.create(user_openid=openid, user_session_key=session_key, user_token=str(uuid.uuid4()))
            else:
                # session_key有时效性，但多久不得而知，需要不定时更新
                user.user_session_key=session_key
                user.user_token=str(uuid.uuid4())
                user.save()
            # 也可以使用models.TbUser.objects.update(user_session_key=session_key,user_token=str(uuid.uuid4()))
        """

        return Response({"status": True, "token": user_object.user_token, "operation":operation})
