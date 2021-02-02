
// 查看本地存储有没有token和username将登录和注册按钮去掉
$().ready(function(){
        var username=window.localStorage.getItem("username");
        var token=window.localStorage.getItem("BBSAuthorization");
        if(username!=null&&token!=null){
            var htmlCode='<li><p class="navbar-text">欢迎，<strong>'+username+'</strong></p></li>'
            $(".personal-part>.beforeLogin").remove();
            $(".personal-part").prepend(htmlCode);
        }else{
            alert("登录后体验更丰富功能");
        }
})


// 获取文章ID，存储本地，发送获取文章详情的异步请求

$(".article-detail").on("click", function(){
    var id=$(this).attr("id");
    window.localStorage.setItem("article-detail", id);
})