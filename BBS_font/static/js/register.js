var register_page={}




$(".register").on("click", function(){
    var result=register_page.submit.check();
    if(result){
        register_page.submit.register();
    }
})