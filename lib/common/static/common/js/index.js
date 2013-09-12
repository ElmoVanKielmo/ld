var check_timeout;

function enable_refresh_view(content_div){
    var refresh_data;
    if(content_div.find('div.battery').length){
        refresh_data = {
            timeout: 120000,
            url: '/battery/'
        }
    }
    else if (content_div.find('div.wifi').length){
        refresh_data = {
            timeout: 5000,
            url: '/wifi/'
        }
    }
    else return;
    (function(){
        content_div.load(refresh_data.url);
        check_timeout = setTimeout(arguments.callee, refresh_data.timeout);
    })();
}

$(document).ready(function(){
    var headings = $('div.accordion_headings');
    headings.first().addClass('header_highlight');
    headings.each(function(){
        var heading = $(this);
        var content_div = heading.next('div.accordion_child');
        if(!heading.hasClass('header_highlight')){
            content_div.hide();
        };
        heading.click(function(){
            if(!heading.hasClass('header_highlight')){
                if(check_timeout){
                    clearTimeout(check_timeout);
                    check_timeout = null;
                };
                var former = $('div.accordion_headings.header_highlight');
                former.removeClass('header_highlight');
                heading.addClass('header_highlight');
                former.next('div.accordion_child').slideUp();
                enable_refresh_view(content_div);
                content_div.slideDown();
            }
        });
    })
});
