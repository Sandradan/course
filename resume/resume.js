let LiTags = document.querySelectorAll('.navContainer ul li')
for (var i = 0; i < LiTags.length; i++) {
    LiTags[i].onmouseenter = function (e) {

        e.currentTarget.classList.add('active')
    }
    LiTags[i].onmouseleave = function (e) {
        e.currentTarget.classList.remove('active')

    }
}


// Setup the animation loop.
function animate(time) {
    requestAnimationFrame(animate)
    TWEEN.update(time)
}
requestAnimationFrame(animate)



let aTags = document.querySelectorAll('.navContainer>ul>li>a')
for (let i = 0; i < aTags.length; i++) {
    aTags[i].onclick = function (e) {
        e.preventDefault()
        let targets = e.currentTarget
        let href = targets.getAttribute('href')
        let element = document.querySelector(href)
        let top = element.offsetTop;

        var currentTop = window.scrollY;
        var targetTop = top - 100;

        var t = Math.abs((targetTop - currentTop) / 100 * 300);
        if (t > 500) {
            t = 500
        }
        const coords = { y: currentTop } // Start at (0, 0)
        const tween = new TWEEN.Tween(coords) // Create a new tween that modifies 'coords'.
            .to({ y: targetTop }, t) // Move to (300, 200) in 1 second.
            .easing(TWEEN.Easing.Quadratic.InOut) // Use an easing function to make the animation smooth.
            .onUpdate(() => {
                // Called after tween.js updates 'coords'.
                // Move 'box' to the position described by 'coords' with a CSS translation.
                window.scrollTo(0, coords.y)
            })
            .start() // Start the tween immediately.

    }
}