$().ready(function(){
        var username=window.localStorage.getItem("username");
        var token=window.localStorage.getItem("BBSAuthorization");
        console.log(username);
        console.log(token);
        if(username!=null&&token!=null){
            var htmlCode='<li><p class="navbar-text">欢迎，<strong>'+username+'</strong></p></li>'
            $(".personal-part>.beforeLogin").remove();
            $(".personal-part").prepend(htmlCode);
        }else{
            alert("登录后体验更丰富功能");
        }
})