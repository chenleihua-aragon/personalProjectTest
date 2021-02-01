var login_page={}
login_page.submit={
    getFormData:function(formID){
        var form=document.getElementById(formID);
	    var tagElements=form.getElementsByTagName('input');//这里我把所有我要获取值得属性都使用了同一个类来标识；
	    var json={};
	    for (var j=0; j<tagElements.length; j++){
			var name=tagElements[j].name;//这里就是要获取得name属性，将此name属性作为json对象得key；
			var value=tagElements[j].value;
	  		json[name] = value; 	//注意这里必须要使用这种方式给json赋值。如果使用json.name=value得话你会发现你所有的key都是一个字符串name，而不是name代表的值
	  }
	return json;
    },

    check:function(){
        var $username=$("#userName").val(); //用户输入的原始名字
        var $password=$("#password").val(); //用户输入的原始密码

        var username_strip_space=$username.replace(/\s+/g,""); //去除空格之后的名字

        var $nameWarning=$("#user-error"); //用户名为空报错
        var $passwordWarning=$("#password-error"); //密码为空报错

        var username_space_error=$("#user-space-error"); //用户名含空格报错

        if($password!=''){
            if($username==''){
                $nameWarning.show();
                login_page.submit.authid($nameWarning);
                return false;
            }else{
                if(username_strip_space.length==$username.length){
                    return true
                }else if(username_strip_space.length<$username.length){
                    username_space_error.show();
                    login_page.submit.authid(username_space_error);
                    return false;
                }
            }
        }else{
            if($username==''){
                $nameWarning.show();
                $passwordWarning.show();
                login_page.submit.authid($nameWarning);
                login_page.submit.authid($passwordWarning);
                return false;
            }else{
                if(username_strip_space.length==$username.length){
                    $passwordWarning.show();
                    login_page.submit.authid($passwordWarning);
                    return false;
                }else if(username_strip_space.length<$username.length){
                    $passwordWarning.show();
                    username_space_error.show();
                    login_page.submit.authid($passwordWarning);
                    login_page.submit.authid(username_space_error);
                    return false;
                }
            }
        }
    },

    authid:function(obj){
        setTimeout(function(){
            obj.hide();
        }, 4000);
    },

    login:function(data){
        var data=serializeForm("login-form");
        jQuery.ajax({
            type:"POST",
            url:"http://127.0.0.1:8000/user/token",
            dataType:"json",
            data:JSON.stringify(data),
            async:"true",
            success:function(response){
                if(response.code==200){
                    token=response.data.token;
                    name=response.username;
                    sign=response.sign;
                    avatar=response.data.avatar;
                    if(avatar){
                        window.localStorage.setItem("avatar",avatar);
                    }
                    window.localStorage.setItem("username",name);
                    window.localStorage.setItem("BBSAuthorization",token);
                    window.localStorage.setItem("sign",sign);
                    window.localStorage.href="article/";
                }
            }
        })
    }
}
$(".login").on("click", function(){
    var result=login_page.submit.check();
    if(result){
        var data=login_page.submit.getFormData("login-form");
        login_page.submit.login(data);
    }
})