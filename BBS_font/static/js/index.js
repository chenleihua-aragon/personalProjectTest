var index_page={}

//功能实现部分
index_page.js={
    // 切换至文章详情页
    articleDetail:function(){
        window.location.href="/article/detail";
    },


}






//功能使用部分
$(".switch-article-type>a").on("click", function(){
    $(this).addClass('active');
    $(this).siblings("a").removeClass('active');
    $(this).children(".badge").text('');
    $(".article-list").remove();
})

$(".article-detail").on("click", function(){
    index_page.js.articleDetail()
})


