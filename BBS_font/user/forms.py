import re
from django import forms
from .models import *


class RegisterForm(forms.Form):

    username = forms.CharField(label="用户名")

    password = forms.CharField(label="密码", widget=forms.PasswordInput)

    passwordConfirm = forms.CharField(label="确认密码", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        length = len(username)
        if length < 8 or length > 12:
            raise forms.ValidationError("用户名长度不合法")
        if re.match('^[0-9]+$', username) or re.match('^[a-zA-Z]+$', username) or re.match('^[0-9a-zA-Z]+$', username):
            user_list = User.objects.filter(name=username)
            if len(user_list) > 0:
                print("用户名已存在")
                raise forms.ValidationError("用户已存在，请更换用户名重试")
            else:
                return username
        else:
            print("用户名格式错误")
            raise forms.ValidationError("用户名格式错误，数字和字母必须至少有一种")

    def clean_password(self):
        password = self.cleaned_data.get("password")
        length = len(password)
        if length < 6 or length > 12:
            print('密码长度错误')
            raise forms.ValidationError("密码长度不合法")
        if re.match('^[0-9a-zA-Z_]+$', password):
            return password

        else:
            print("密码不合法")
            raise forms.ValidationError("密码必须包含数字、字母和下划线")

    def clean(self):
        password = self.cleaned_data.get('password')
        passwordConfirm = self.cleaned_data.get('passwordConfirm')
        print(password)
        print(passwordConfirm)

        if passwordConfirm == password:
            return self.cleaned_data

        else:
            print("两次密码不一致")
            raise forms.ValidationError("两次输入密码不一致，请核实后重新输入")
