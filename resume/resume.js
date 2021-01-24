let LiTags = document.querySelectorAll('.navContainer ul li')
for (var i = 0; i < LiTags.length; i++) {
    LiTags[i].onmouseenter = function (e) {

        e.currentTarget.classList.add('active')
    }
    LiTags[i].onmouseleave = function (e) {
        e.currentTarget.classList.remove('active')
       
    }
}