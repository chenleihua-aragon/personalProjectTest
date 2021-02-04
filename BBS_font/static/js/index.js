var index_page={}

//功能实现部分
index_page.js={


}


//功能使用部分
$(".switch-article-type>a").on("click", function(){
    $(this).addClass('active');
    $(this).siblings("a").removeClass('active');
    $(this).children(".badge").text('');
    $(".article-list").remove();
})



