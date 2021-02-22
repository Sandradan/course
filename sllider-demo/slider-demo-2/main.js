$('.images img:nth-child(1)').addClass('current')
    $('.images img:nth-child(2)').addClass('enter')
setTimeout(() => {
    $('.images img:nth-child(1)').addClass('leave').removeClass('current')
    .one('transitionend',(e)=>{
        $(e.currentTarget).removeClass('leave').addClass('enter')
    })
    $('.images img:nth-child(2)').addClass('current').removeClass('enter')
    .one('transitionend',(e)=>{
        $(e.currentTarget).removeClass('current').addClass('leave')
    })
}, 3000);
setTimeout(() => {
    $('.images img:nth-child(2)').addClass('leave').removeClass('current')
    .one('transitionend',(e)=>{
        $(e.currentTarget).removeClass('leave').addClass('enter')
    })
    $('.images img:nth-child(3)').addClass('current').removeClass('enter')
    .one('transitionend',(e)=>{
        $(e.currentTarget).removeClass('current').addClass('leave')
    })
}, 6000);
setTimeout(() => {
    $('.images img:nth-child(3)').addClass('leave').removeClass('current')
    .one('transitionend',(e)=>{
        $(e.currentTarget).removeClass('leave').addClass('enter')
    })
    $('.images img:nth-child(1)').addClass('current').removeClass('enter')
    .one('transitionend',(e)=>{
        $(e.currentTarget).removeClass('current').addClass('leave')
    })
}, 9000);
setTimeout(() => {
    $('.images img:nth-child(1)').addClass('leave').removeClass('current')
    .one('transitionend',(e)=>{
        $(e.currentTarget).removeClass('leave').addClass('enter')
    })
    $('.images img:nth-child(2)').addClass('current').removeClass('enter')
    .one('transitionend',(e)=>{
        $(e.currentTarget).removeClass('current').addClass('leave')
    })
}, 12000);

