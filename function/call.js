//例一
function f1(){
    function f2(){
        console.log(this)
    }
    f2.call()
}
var obj = {
    name:'obj'
}
f1.call(obj)



//例二
var a = 1
function f1(){
    var a = 2 //相当于先var a 再给a赋值 a = 2
    f2.call()
}
function f2(){
    console.log(a)
}
f1.call() //1
