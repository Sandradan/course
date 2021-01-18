var div = document.getElementById('canvas');
var painting = false;
div.onmousedown= function(a){
    painting = true;
    var x = a.clientX;
    var y = a.clientY;
    var dot = document.createElement('div');
    dot.style = "width:6px; height:6px;"+"background:black;border-radius:3px;"+"position:absolute; top:"+(y-3)+"px;"+"left:"+(x-3)+"px;";
    div.appendChild(dot);
};


//动鼠标

div.onmousemove = function(a){
  if(painting){
    var x = a.clientX;
    var y = a.clientY;
    var dot = document.createElement('div');
    dot.style = "width:6px; height:6px;"+"background:black;border-radius:3px;"+"position:absolute; top:"+(y-3)+"px;"+"left:"+(x-3)+"px;";
    div.appendChild(dot);
  }
  
};



//鼠标松开
div.onmouseup= function (a) {
   painting = false;
};