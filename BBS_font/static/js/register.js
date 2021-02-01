var register_page={}

register_page.submit={
    check:function(){
        var $username=$("#userName").val();
        var $password=$("#password").val();
        var $passwordConfirm=$("#passwordConfirm").val();

        var usernameLength=$username.length
        var passwordLength=$password.length
        var nameStripSpace=$username.replace(/\s+/g,"")

        var $usernameError=$("#name-error");
        var $passwordError=$("#password-error");
        var $passwordConfirmError=$("#password-confirm-error");

        if($username!=""&&8<usernameLength&&12>usernameLength&&nameStripSpace.length==usernameLength&&8<passwordLength&&12>passwordLength&&$password==$passwordConfirm){
            return true;
        }else if(($username==""||8>usernameLength||12<usernameLength||nameStripSpace.length<usernameLength) && (8<passwordLength&&12>passwordLength&&$password==$passwordConfirm)){
            $usernameError.show(); // 用户名不合法
            register_page.submit.authid($usernameError);
            return false;
        }else if(($username==""||8>usernameLength||12<usernameLength||nameStripSpace.length<usernameLength)&&(8>passwordLength||12<passwordLength)&&$password==$passwordConfirm){
            $usernameError.show(); // 用户名不合法
            register_page.submit.authid($usernameError);
            $passwordError.show(); // 密码长度不合法
            register_page.submit.authid($passwordError);
            return false;
        }else if(($username==""||8>usernameLength||12<usernameLength||nameStripSpace.length<usernameLength)&&((8>passwordLength&&$password!="")||12<passwordLength)&&$password!=$passwordConfirm){
            $usernameError.show(); //用户名不合法
            register_page.submit.authid($usernameError);
            $passwordError.show(); // 密码长度不合法
            register_page.submit.authid($passwordError);
            passwordConfirmError.show(); //两次密码不一致
            register_page.submit.authid(passwordConfirmError);
            return false;
        }else if(($username!=""&&8<usernameLength&&12>usernameLength&&nameStripSpace.length==usernameLength)&&((8>passwordLength&&$password!="")||12<passwordLength) &&$password!=$passwordConfirm){
            $passwordError.show(); // 密码长度不合法
            register_page.submit.authid($passwordError);
            passwordConfirmError.show(); // 两次密码不一致
            register_page.submit.authid(passwordConfirmError);
            return false;
        }else if(($username==""||8>usernameLength||12<usernameLength||nameStripSpace.length<usernameLength) && (8<passwordLength&&12>passwordLength&&$password!=$passwordConfirm)){
            $usernameError.show(); // 用户名不合法
            register_page.submit.authid($usernameError);
            passwordConfirmError.show(); //两次密码不一致
            register_page.submit.authid(passwordConfirmError);
            return false;
        }else if($username!=""&&8<usernameLength&&12>usernameLength&&nameStripSpace.length==usernameLength&&8<passwordLength&&12>passwordLength&&$password!=$passwordConfirm){
            passwordConfirmError.show(); // 两次输入密码不一致
            register_page.submit.authid(passwordConfirmError);
            return false;
        }else if($username!=""&&8<usernameLength&&12>usernameLength&&nameStripSpace.length==usernameLength&&((8>passwordLength&&$password!="")||12<passwordLength)&&$password==$passwordConfirm){
            passwordError.show(); //密码不合法
            return false;
        }
    },
    authid:function(obj){
        setTimeout(function(){
            obj.hide();
        }, 4000);
    },
}


$(".register").on("click", function(){
    var result=register_page.submit.check();
    if(result){
        register_page.submit.register();
    }
})