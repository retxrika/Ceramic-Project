$(document).ready(function() {
    const open = $('.contact-open');
    const block = $('.contact-cart-block');
    const triangle = $('.contact-open-triangle');

    block.click(function() {
        if (open.first().is(':hidden'))
        {
            triangle.slideToggle();
            open.slideToggle();
        }
        else
        {
            triangle.slideUp();
            open.slideUp();
        }
    });

    block.mouseenter(function() {
        triangle.slideToggle();
        open.slideToggle();
    });

    block.mouseleave(function() {
        setTimeout(function () {
            triangle.slideUp();
            open.slideUp();
        }, 1000);
    });
});