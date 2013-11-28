$(document).ready(function() {

    $(".dropdown-menu li a").click(function(){
        
        //$(".btn:first-child").text($(this).text());
        //$(".btn:first-child").val($(this).text());
        
        var obj = $(this);
        console.log ($(obj).text());
        $(obj).closest(".btn-group").find(".btn").text($(obj).text());
        //$(obj).closest("btn-group").find(".btn").val($(obj).text())
        
    });
    
});