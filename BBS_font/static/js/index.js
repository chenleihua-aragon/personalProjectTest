var index_page={}

//功能实现部分
index_page.js={
}

//功能使用部分
$(".switch-article-type>a").on("click", function(){
    window.localStorage.setItem("block", $(this).attr("id"));
})

// 使选中的版块按钮显示激活蓝色
$().ready(function(){
    var id_name=window.localStorage.getItem("block");
    if(id_name==null||id_name=="news"){
        $("#news").addClass("active");
    }else{
        aObj=document.getElementById(id_name);
        aObj.setAttribute("class", "list-group-item active");
    }
})

$(".sort-method").on("click", function(){
    window.localStorage.setItem("sort-method", $(this).attr("id"));
})
$(".page").on("click", function(){
    window.localStorage.setItem("page", $(this).text());
})


$().ready(function(){
    var sort_method=window.localStorage.getItem("sort-method");
    var selector="#"+sort_method;
    $(selector).addClass("active");
    var page=window.localStorage.getItem("page");
    var time_href="?sort_method=time&page="+page;
    var heat_href="?sort_method=heat&page="+page;
    var page_selector="#"+page;
    $(page_selector).parent().addClass("active");
//    $("#time>a").attr("href", time_href);
//    $("#heat>a").attr("href", heat_href);
//    var page_href="?sort_method="+sort_method+"&page="+$(".page").text();
//    $(".page").attr("href", page_href);
})

$("#pre").on("click",function(){
    var page=window.localStorage.getItem("page");
    page--;
    window.localStorage.setItem("page", page);
})

$("#next").on("click",function(){
    var page=window.localStorage.getItem("page");
    page++;
    window.localStorage.setItem("page", page);
})


