$(function() {
    $('.content').hide();
    $('.subcontent').hide();

    $('h2').click(function() {
        $(this).next('.content').toggle();
    });

    $('h3').click(function() {
        $(this).next('.subcontent').toggle();
    });
    
    $('.toggle').click(function() {
        $('.content').toggle();
        $('.subcontent').toggle();
    });
   
});