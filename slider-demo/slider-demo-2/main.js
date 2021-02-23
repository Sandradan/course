// $('.images img:nth-child(1)').addClass('current')   //初始化第一张是当前状态
//     $('.images img:nth-child(2)').addClass('enter') //初始化第二张是进入状态
// setTimeout(() => {
//     $('.images img:nth-child(1)').addClass('leave').removeClass('current') //第一张状态是离开状态
//     .one('transitionend',(e)=>{
//         $(e.currentTarget).removeClass('leave').addClass('enter')
//     })
//     $('.images img:nth-child(2)').addClass('current').removeClass('enter') //第二张状态是当前状态
//     .one('transitionend',(e)=>{
//         $(e.currentTarget).removeClass('current').addClass('leave')
//     })
// }, 3000);
// setTimeout(() => {
//     $('.images img:nth-child(2)').addClass('leave').removeClass('current')
//     .one('transitionend',(e)=>{
//         $(e.currentTarget).removeClass('leave').addClass('enter')
//     })
//     $('.images img:nth-child(3)').addClass('current').removeClass('enter')
//     .one('transitionend',(e)=>{
//         $(e.currentTarget).removeClass('current').addClass('leave')
//     })
// }, 6000);
// setTimeout(() => {
//     $('.images img:nth-child(3)').addClass('leave').removeClass('current')
//     .one('transitionend',(e)=>{
//         $(e.currentTarget).removeClass('leave').addClass('enter')
//     })
//     $('.images img:nth-child(1)').addClass('current').removeClass('enter')
//     .one('transitionend',(e)=>{
//         $(e.currentTarget).removeClass('current').addClass('leave')
//     })
// }, 9000);
// setTimeout(() => {
//     $('.images img:nth-child(1)').addClass('leave').removeClass('current')
//     .one('transitionend',(e)=>{
//         $(e.currentTarget).removeClass('leave').addClass('enter')
//     })
//     $('.images img:nth-child(2)').addClass('current').removeClass('enter')
//     .one('transitionend',(e)=>{
//         $(e.currentTarget).removeClass('current').addClass('leave')
//     })
// }, 12000);




$('.images img:nth-child(1)').addClass('current')   //初始化第一张是当前状态
$('.images img:nth-child(2)').addClass('enter') //初始化第二张是进入状态
let n = 1
setInterval(() => {
    $(`.images img:nth-child(${x(n)})`).addClass('leave').removeClass('current').one('transitionend', (e) => {
        $(e.currentTarget).addClass('enter').removeClass('leave')
    })
    $(`.images img:nth-child(${x(n+1)})`).addClass('current').removeClass('enter')
    n = n + 1
}, 3000)

function x(n){
    if (n > 3) {
        n = n % 3
        if (n === 0) {
            n = 3
        }
    }
    return n
}