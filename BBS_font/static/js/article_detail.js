//  添加关注，点击关注后按钮切换为心形
$(".follow").on("click", function(){
    $(this).removeClass("btn-primary");
    $(this).addClass("btn-danger");
    $(this).html(' <span class="glyphicon glyphicon-heart"></span> ');
})

//  查看用户信息
$(".user-info").on("click", function(){
    window.location.href="/user/userinfo";
})

//  文章点赞效果，点赞后，按钮颜色改变
$(".up").on("click", function(){
    $(this).removeClass("btn-danger");
    $(this).addClass("btn-primary");
    $(this).children(".badge").css("background-color", "red");
})

//  评论点赞，点赞后按钮颜色改变
$(".comment-up").on("click", function(){
//    $(this).removeClass("btn-success");
//    $(this).addClass("btn-primary");
    $(this).children(".badge").css("background-color", "red");
})


//  评论点踩，颜色改变
$(".comment-down").on("click", function(){
//    $(this).removeClass("btn-danger");
//    $(this).addClass("btn-primary");
    $(this).children(".badge").css("background-color", "red");
})

//  回复点赞，颜色改变
$(".reply-up").on("click", function(){
    $(this).removeClass("btn-success");
    $(this).addClass("btn-primary");
    $(this).siblings(".badge").css("background-color", "red");
})

//  回复点踩，改变按钮和点踩数量的颜色
$(".reply-down").on("click", function(){
    $(this).removeClass("btn-danger");
    $(this).addClass("btn-primary");
    $(this).siblings(".badge").css("background-color", "red");
})