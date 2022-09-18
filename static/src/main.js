$(document).on('submit', '#url-form', function(e) {
    e.preventDefault();
    
    $(".loading").css({"display":"flex"})
    
    $.ajax({
        type: 'POST',
        url: '/',
        data: {
            url: $("#url").val()
        },
        
        success: function(data) {
            $(".loading").css({"display":"none"})
            $("#download-form").html(data)
           
        }
    })
});