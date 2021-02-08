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




// Node.prototype.getSiblings = function () {
//     var allchildren = this.parentNode.children
//     var array = { length: 0 }
//     for (let i = 0; i < allchildren.length; i++) {
//         if (allchildren[i] !== this) {
//             array[array.length] = allchildren[i]
//             array.length += 1
//         }
//     }
//     return array
// }
// Node.prototype.addClass = function(classes) {
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
//         this.classList[methodName](key)

//     }
// }

// item2.getSiblings.call(item2)
// item2.addClass.call(item2, { "a": false, "b": true, "c": true })



// window.jQuery = function (nodeOrSelector) {
//     let node
//     if(typeof nodeOrSelector === 'string'){
//         node = document.querySelector(nodeOrSelector)
//     }else{
//         node = nodeOrSelector
//     }
//     return {
//         getSiblings: function () {
//             var allchildren = node.parentNode.children
//             var array = { length: 0 }
//             for (let i = 0; i < allchildren.length; i++) {
//                 if (allchildren[i] !== node) {
//                     array[array.length] = allchildren[i]
//                     array.length += 1
//                 }
//             }
//             return array
//         },
//         addClass: function (classes) {
//             classes.forEach((value)=>{
//                     node.classList.add(value)
//                 })

//         }
//     }
// }
// var node2 = jQuery("ul>li:nth-child(4)")
// node2.getSiblings()
// console.log(node2.getSiblings())
// node2.addClass(['red', 'b', 'c'])





window.jQuery = function (nodeOrSelector) {
    let nodes = {}
    if (typeof nodeOrSelector === 'string') {
        let temp = document.querySelectorAll(nodeOrSelector)
        for (let i = 0; i < temp.length; i++) {
            nodes[i] = temp[i]
        }
        nodes.length = temp.length
    } else if (nodeOrSelector instanceof Node) {
        nodes = {
            0: nodeOrSelector,
            length: 1
        }
    }

    nodes.getSiblings = function () {
        // var allchildren = node.parentNode.children
        // var array = { length: 0 }
        // for (let i = 0; i < allchildren.length; i++) {
        //     if (allchildren[i] !== node) {
        //         array[array.length] = allchildren[i]
        //         array.length += 1
        //     }
        // }
        // return array
    }
    nodes.addClass = function (classes) {
        classes.forEach((value) => {
            for (let i = 0; i < nodes.length; i++) {
                nodes[i].classList.add(value)
            }
        })

    }

    nodes.text = function (text) {
        if (text === undefined) {
            var texts = []
            for (let i = 0; i < nodes.length; i++) {
                texts.push(nodes[i].textContent)
            }
            return texts
        } else {
            for (let i = 0; i < nodes.length; i++) {
                nodes[i].textContent = text
            }
        }
    }

    return nodes
}




var node2 = jQuery("ul>li")
node2.getSiblings()
console.log(node2.getSiblings())
node2.addClass(['red'])

node2.text('hi')