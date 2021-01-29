var login_page={}
login_page.submit={
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
    }
}
$(".login").on("click", function(){
    var result=login_page.submit.check();
    if(result){
        login_page.submit.login();
    }
})