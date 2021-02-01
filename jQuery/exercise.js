// 取所有的兄弟元素
// function getSiblings(node) {
//     var allchildren = node.parentNode.children
//     var array = { length: 0 }
//     for (let i = 0; i < allchildren.length; i++) {
//         if (allchildren[i] !== node) {
//             array[array.length] = allchildren[i]
//             array.length += 1
//         }
//     }
//     return array
// }

// var classes = ['a','b','c']
// classes.forEach((value)=>{
//     item2.classList.add(value)
// })


//增加类
// function addClass(node, classes) {
//     // var classes = {
//     //     "a":true,
//     //     "b": false,
//     //     "c":true
//     // }
//     for (let key in classes) {
//         // if (classes[key]) {
//         //     node.classList.add(key)
//         // } else {
//         //     node.classList.remove(key)
//         // }
//         var methodName = classes[key] ? "add" : "remove"
//         node.classList[methodName](key)

//     }
// }

Node.prototype.getSiblings = function () {
    var allchildren = this.parentNode.children
    var array = { length: 0 }
    for (let i = 0; i < allchildren.length; i++) {
        if (allchildren[i] !== this) {
            array[array.length] = allchildren[i]
            array.length += 1
        }
    }
    return array
}
Node.prototype.addClass = function(classes) {
    // var classes = {
    //     "a":true,
    //     "b": false,
    //     "c":true
    // }
    for (let key in classes) {
        // if (classes[key]) {
        //     node.classList.add(key)
        // } else {
        //     node.classList.remove(key)
        // }
        var methodName = classes[key] ? "add" : "remove"
        this.classList[methodName](key)

    }
}

item2.getSiblings.call(item2)
item2.addClass.call(item2, { "a": false, "b": true, "c": true })