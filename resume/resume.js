let LiTags = document.querySelectorAll('.navContainer ul li')
for (var i = 0; i < LiTags.length; i++) {
    LiTags[i].onmouseenter = function (e) {

        e.currentTarget.classList.add('active')
    }
    LiTags[i].onmouseleave = function (e) {
        e.currentTarget.classList.remove('active')

    }
}




let aTags = document.querySelectorAll('.navContainer>ul>li>a')
for (let i = 0; i < aTags.length; i++) {
    aTags[i].onclick = function (e) {
        e.preventDefault()
        let targets = e.currentTarget
        let href = targets.getAttribute('href')
        let element = document.querySelector(href)
        let top = element.offsetTop;
        window.scrollTo(0, top - 80)
    }
}