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

//获取本地存储的文章id，发送异步请求，获取文章详情
$().ready(function(){
    var id=window.localStorage.getItem("article-detail");
    var token=window.localStorage.getItem("BBSAuthorization")
    if(id==null){
        alert("文章数据无效，请核实")
    }else{
        jQuery.ajax({
            type:"GET",
            url:"http://127.0.0.1:8000/article/"+id,
            async:"true",
            dataType:"json",
            beforeSend:function(request){
                request.setRequestHeader("BBSAUTHORIZATION",token);
            },
            success:function(response){
                if(response.code==200){
                    $(".article-detail").attr("id", response.data.article_id);
                    var article_html='<div class="row">';
                    article_html+='<div class="col-sm-10 col-sm-offset-1">';
                    article_html+='<div class="panel panel-success">';
                    article_html+='<div class="panel-heading">';
                    article_html+='<h3 class="panel-title">'+response.data.article_title+'</h3>';
                    article_html+='<h5><a href="{% url '+"'userinfo'"+' %}">'+response.data.article_author+'</a></h5></div>';
                    article_html+='<div class="panel-body">';
                    article_html+='<p style="line-height: 180%; ">'+response.data.article_content+'</p></div>';
                    article_html+='<div class="panel-footer clearfix"><div class="col-sm-3 col-xs-6 col-sm-offset-1">';
                    article_html+='<small>发布时间：'+response.data.article_created_time+'</small></div>';
                    article_html+='<div class="col-sm-2 col-sm-offset-5">';
                    article_html+='<button class="btn btn-danger btn-xs up"> <span class="glyphicon glyphicon-heart"></span> 点赞<span class="badge">'+response.data.article_up+'</span></button>';
                    article_html+='<button class="btn btn-primary btn-xs follow"> <span class="glyphicon glyphicon-plus"></span> 关注</button></div></div></div></div></div>';
                    $(".article-detail").html(article_html);
                    $(".comment-list>.container-fluid:nth-child(1)>.row:nth-child(2)>div:nth-child(1)>img").attr("src", response.data.avatar);

                    var hot_comment_list=response.data.article_hot_comment_list;
                    var other_comment_list=response.data.article_other_comment_list;
                    if(hot_comment_list.length==0){
                        var _html='<div class="container-fluid"><div class="row">';
                        _html+='<div class="col-sm-4 col-xs-8 col-sm-offset-4 col-xs-offset-2">';
                        _html+='<h2 style="color: grey">还没有评论，快来抢沙发吧</h2></div></div></div>';
                        $(".comment-list").append(_html);
                    }else{
                        var hot_comment_html='<div class="container-fluid hot-comment"><div class="row">';
                        hot_comment_html+='<div class="col-sm-2 col-sm-offset-1">';
                        hot_comment_html+='<h4><strong>热门评论</strong></h4></div></div>';
                        $(".comment-list").append(hot_comment_html);
                        for(var i=0; i<hot_comment_list.length; i++){
                            var comment_html='<div class="container-fluid comment" id="'+hot_comment_list[i].id+'"><div class="row">';
                            comment_html+='<a href="{% url '+"'userinfo' %}"+'">';
                            comment_html+='<div class="col-sm-1 col-sm-offset-1 text-right" style="padding: 0; ">';
                            comment_html+='<img src='+hot_comment_list[i].publisher_avatar+' alt="用户头像" style="width: 30px; height: 30px; border-radius: 100%; "></div>';
                            comment_html+='<div class="col-sm-4">';
                            comment_html+='<p><strong>'+hot_comment_list[i].publisher_name+'</strong></p></div></a>';
                            comment_html+='<div class="col-sm-8 col-sm-offset-2 comment">';
                            comment_html+='<p class="comment-content" style="line-height: 150%; ">'+hot_comment_list[i].comment_content+'</p></div>';
                            comment_html+='<div class="col-sm-2 col-sm-offset-2 text-left">';
                            comment_html+='<small class ="comment-time">'+hot_comment_list[i].created_time+'</small></div>';
                            comment_html+='<div class="col-sm-2 col-sm-offset-1">';
                            comment_html+='<button class="btn btn-success btn-xs comment-up"> <span class="glyphicon glyphicon-thumbs-up"></span> 首肯心折！<span class="badge up_count">'+hot_comment_list[i].up_counts+'</span> </button></div>';
                            comment_html+='<div class="col-sm-2">';
                            comment_html+='<button class="btn btn-danger btn-xs comment-down"> <span class="glyphicon glyphicon-thumbs-down"></span> 大谬不然！<span class="badge down_count">'+hot_comment_list[i].down_counts+'</span></button></div>';
                            comment_html+='<div class="col-sm-1">';
                            comment_html+='<button class="btn btn-xs btn-primary" data-target="#comment_reply" data-toggle="modal">回复</button></div></div></div>';
                            $(".comment-list").append(comment_html);
                            var replies_list=hot_comment_list[i].replies;
                            for(var j=0;j<replies_list.length; j++){
                                var reply_html='<div class="container comment-reply-'+hot_comment_list[i].id+'">';
                                reply_html+='<div class="row" style="margin-top: 10px; ">';
                                reply_html+='<a href="{% url '+"'userinfo' %}"+'">';
                                reply_html+='<div class="col-sm-1 col-sm-offset-1 text-right" style="padding: 0; ">';
                                reply_html+='<img src="'+replies_list[j].publisher_avatar+'" alt="用户头像" style="width: 30px; height: 30px; border-radius: 100%; ">';
                                reply_html+='</div>';
                                reply_html+='<div class="col-sm-4">';
                                reply_html+='<p><strong>'+replies_list[j].publisher+'</strong></p></div></a>';
                                reply_html+='<div class="col-sm-8 col-sm-offset-2">';
                                reply_html+='<p class="comment-reply" style="line-height: 150%; ">'+replies_list[j].reply_content+'</p></div>';
                                reply_html+='<div class="col-sm-2 col-sm-offset-2 reply-time">';
                                reply_html+='<small>'+replies_list[j].created_time+'</small></div>';
                                reply_html+='<div class="col-sm-2 col-sm-offset-1">';
                                reply_html+='<button class="btn btn-success btn-xs reply-up"> <span class="glyphicon glyphicon-thumbs-up"></span> 首肯心折！<span class="badge up_count">2657</span> </button></div>';
                                reply_html+='<div class="col-sm-2">';
                                reply_html+='<button class="btn btn-danger btn-xs reply-down"> <span class="glyphicon glyphicon-thumbs-down"></span> 大谬不然！<span class="badge up_count">2657</span> </button></div></div>';
                                $(".comment-list").append(reply_html);
                            }
                            if(hot_comment_list[i].more_replies){
                                var _html='<div class="row" style="margin: 10px 0">';
                                    _html+='<div class="col-sm-1 col-sm-offset-2">';
                                    _html+='<button class="btn btn-warning btn-xs">';
                                    _html+='查看更多回复</button></div></div></div>';
                            }else{
                                var _html='</div>';
                            }
                            $(".comment-list").append(_html);
                        }
                        $(".comment-list").append('</div>');
                        var divide_html='<div class="container-fluid">';
                        divide_html+='<div class="row" style="margin: 10px 0">';
                        divide_html+='<div class="col-sm-9 col-sm-offset-1">';
                        divide_html+='<div style="height: 3px; background-color: gray;"></div></div></div></div>';
                        divide_html+='<div class="container-fluid other-comment">';
                        divide_html+='<div class="row">';
                        divide_html+='<div class="col-sm-2 col-sm-offset-1">';
                        divide_html+='<h4><strong>其他评论</strong></h4></div></div>';
                        $(".comment-list").append(divide_html);
                    }
                    var html='<div class="container-fluid">';
                    $(".comment-list").append(html);
                    for(var k=0;k<other_comment_list.length;k++){
                        var other_html='<div class="row">';
                            other_html+='<a href="{% url '+"'userinfo'"+' %}">';
                            other_html+='<div class="col-sm-1 col-sm-offset-1 text-right" style="padding: 0; ">';
                            other_html+='<img src="'+other_comment_list[k].publisher_avatar+'" alt="用户头像" style="width: 30px; height: 30px; border-radius: 100%; ">';
                            other_html+='</div>';
                            other_html+='<div class="col-sm-4">';
                            other_html+='<p><strong>'+other_comment_list[k].publisher_name+'</strong></p></div></a>';
                            other_html+='<div class="col-sm-8 col-sm-offset-2 comment">';
                            other_html+='<p class="comment-content" style="line-height: 150%; ">'+other_comment_list[k].comment_content+'</p></div>';
                            other_html+='<div class="col-sm-2 col-sm-offset-2 text-left">';
                            other_html+='<small class ="comment-time">'+other_comment_list[k].created_time+'</small></div>';
                            other_html+='<div class="col-sm-2 col-sm-offset-1">';
                            other_html+='<button class="btn btn-success btn-xs comment-up"> <span class="glyphicon glyphicon-thumbs-up"></span> 首肯心折！<span class="badge up_count">'+other_comment_list[k].up_count+'</span> </button></div>';
                            other_html+='<div class="col-sm-2">';
                            other_html+='<button class="btn btn-danger btn-xs comment-down"> <span class="glyphicon glyphicon-thumbs-down"></span> 大谬不然！<span class="badge down_count">'+other_comment_list[k].down_count+'</span></button></div>';
                            other_html+='<div class="col-sm-1">';
                            other_html+='<button class="btn btn-xs btn-primary" data-target="#comment_reply" data-toggle="modal">回复</button></div></div></div>';
                            other_html+='<div class="container">';
                            $(".comment-list").append(other_html);
                            replies_list=other_comment_list[k].replies;
                            for(var l=0;l<replies_list.length; l++){
                                var reply_html='<div class="row" style="margin-top: 10px; ">';
                                reply_html+='<a href="{% url '+"'userinfo'"+' %}">';
                                reply_html+='<div class="col-sm-1 col-sm-offset-1 text-right" style="padding: 0; ">';
                                reply_html+='<img src="'+replies_list[l].publisher_avatar+'" alt="用户头像" style="width: 30px; height: 30px; border-radius: 100%; ">';
                                reply_html+='</div>';
                                reply_html+='<div class="col-sm-4">';
                                reply_html+='<p><strong>'+replies_list[l].publisher+'</strong></p>';
                                reply_html+='</div>';
                                reply_html+='</a>';
                                reply_html+='<div class="col-sm-8 col-sm-offset-2">';
                                reply_html+='<p class="comment-reply" style="line-height: 150%; ">'+replies_list[l].reply_content+'</p></div>';
                                reply_html+='<div class="col-sm-2 col-sm-offset-2 reply-time">';
                                reply_html+='<small>'+replies_list[l].created_time+'</small>';
                                reply_html+='</div>'
                                reply_html+='<div class="col-sm-2 col-sm-offset-1">'
                                reply_html+='<button class="btn btn-success btn-xs reply-up"> <span class="glyphicon glyphicon-thumbs-up"></span> 首肯心折！<span class="badge up_count">'+replies_list[l].up_count+'</span> </button>';
                                reply_html+='</div>'
                                reply_html+='<div class="col-sm-2">'
                                reply_html+='<button class="btn btn-danger btn-xs reply-down"> <span class="glyphicon glyphicon-thumbs-down"></span> 大谬不然！<span class="badge up_count">'+replies_list[l].down_count+'</span> </button>'
                                reply_html+='</div>'
                                reply_html+='</div>'
                                $(".comment-list").append(reply_html);
                            }
                            if(other_comment_list[k].more_replies){
                                var html='<div class="container-fluid"><div class="row" style="margin: 10px 0;">'
                                html+='<div class="col-sm-1 col-sm-offset-2">';
                                html+='<button class="btn btn-warning btn-xs">';
                                html+='查看更多回复';
                                html+='</button>';
                                html+='</div>';
                                html+='</div>';
                                html+='</div>';
                                $(".comment-list").append(html);
                            }else{
                                var html='</div>';
                                $(".comment-list").append(html);
                            }

                    }
                    if(response.data.more_comment){
                        var html='<div class="container-fluid">';
                        html+='<div class="row" style="margin-top: 15px; ">';
                        html+='<div class="col-sm-1 col-sm-offset-2">';
                        html+='<button class="btn btn-info btn-sm">';
                        html+='<span class="glyphicon glyphicon-th-list"></span> 查看更多评论';
                        html+='</button>';
                        html+='</div>';
                        html+='</div>';
                        html+='</div>';
                        html+='</div>';
                        $(".comment-list").append(html);
                    }else{
                        var html='</div>';
                        $(".comment-list").append(html);
                    }
                }else{
                    alert(response.error);
                }
            }
        })
    }
})

// 关注用户
$(".follow").on("click", function(){
    var data={"author_name": $(this).parents(".panel").children(".panel-heading").children("h5").children('a').text()};
    var token=window.localStorage.getItem("BBSAuthorization");
    jQuery.ajax({
        type:"POST",
        url:"http://127.0.0.1:8000/user/attention",
        data:JSON.stringify(data),
        async:"true",
        dataType:"json",
        beforeSend:function(request){
            request.setRequestHeader("BBSAUTHORIZATION",token);
        },
        success:function(response){
            if(response.code==100){
                alert(response.data);
            }else{
                alert(response.error);
            }
        }
    })
})

// 文章点赞
$(".up").on("click", function(){
    var data={"article_id": $(this).parents(".article-content").attr("id")};
    var token=window.localStorage.getItem("BBSAuthorization");
    jQuery.ajax({
        data: JSON.stringify(data),
        type: "POST",
        url: "http://127.0.0.1:8000/article/star",
        async: "true",
        dataType: "json",
        beforeSend:function(request){
            request.setRequestHeader("BBSAUTHORIZATION",token);
        },
        success:function(response){
            if(response.code!=200){
                alert(response.error);
            }
        }
    })
})

// 评论点赞
$(".comment-up").on("click", function(){
    var data= {"comment-id":$(this).parents(".comment").attr("id"),
               "type": "up"};
    var token=window.localStorage.getItem("BBSAuthorization");
    jQuery.ajax({
        data:JSON.stringify(data),
        type:"POST",
        async:"true",
        url:"http://127.0.0.1:8000/article/comment";
        dataType:"json",
        beforeSend:function(request){
            request.setRequestHeader("BBSAUTHORIZATION",token);
        },
        success:function(response){
            if(response.code!=200){
                alert(response.error);
            }
        }
    })
})

// 评论点踩
$(".comment-down").on("click", function(){
    var data= {"comment-id":$(this).parents(".comment").attr("id"),
               "type": "down"};
    var token=window.localStorage.getItem("BBSAuthorization");
    jQuery.ajax({
        data:JSON.stringify(data),
        type:"POST",
        async:"true",
        url:"http://127.0.0.1:8000/article/comment";
        dataType:"json",
        beforeSend:function(request){
            request.setRequestHeader("BBSAUTHORIZATION",token);
        },
        success:function(response){
            if(response.code!=200){
                alert(response.error);
            }
        }
    })
})