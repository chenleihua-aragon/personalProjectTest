var detail_page={}


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

//获取本地存储的文章id，发送异步请求
$().ready(function(){
    var id=window.localStorage.getItem("article-detail");
    if(id==null){
        alert("文章数据无效，请核实")
    }else{
        jQuery.ajax({
            type:"GET",
            url:"http://127.0.0.1:8000/article/"+id,
            async:"true",
            dataType:"json",
            success:function(response){
                if(response.code==200){
                    $(".article-detail").attr("id", response.data.article_id);
                    var article_html='<div class="row">'
                    article_html+='<div class="col-sm-10 col-sm-offset-1">'
                    article_html+='<div class="panel panel-success">'
                    article_html+='<div class="panel-heading">'
                    article_html+='<h3 class="panel-title">'+response.data.article_title+'</h3>'
                    article_html+='<h5><a href="{% url '+"'userinfo'"+' %}">'+response.data.article_author+'</a></h5></div>'
                    article_html+='<div class="panel-body">'
                    article_html+='<p style="line-height: 180%; ">'+response.data.article_content+'</p></div>'
                    article_html+='<div class="panel-footer clearfix"><div class="col-sm-3 col-xs-6 col-sm-offset-1">'
                    article_html+='<small>发布时间：'+response.data.article_created_time+'</small></div>'
                    article_html+='<div class="col-sm-2 col-sm-offset-5">'
                    article_html+='<button class="btn btn-danger btn-xs up"> <span class="glyphicon glyphicon-heart"></span> 点赞<span class="badge">'+response.data.article_up+'</span></button>'
                    article_html+='<button class="btn btn-primary btn-xs follow"> <span class="glyphicon glyphicon-plus"></span> 关注</button></div></div></div></div></div>'
                    $(".article-detail").html(article_html);
                    $(".comment-list>.container-fluid:nth-child(1)>.row:nth-child(2)>div:nth-child(1)>img").attr("src", response.data.avatar);


                    var hot_comment=''    // 从后端返回具体的评论和回复数据，填充作为评论内容


                    $(".hot-comment").after(hot_comment);  // 热门评论按照3/2/1的顺序追加

                    var other_comment=''

                    $(".other-comment").append(other_comment);
                }else{
                    alert(response.error);
                }
            }
        })
    }
})