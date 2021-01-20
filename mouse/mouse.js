var canvas = document.getElementById('xxx');
var ctx = canvas.getContext('2d');
var era = document.getElementById('eraser');

var pageWidth = document.documentElement.clientWidth;
var pageHeight = document.documentElement.clientHeight;
canvas.width = pageWidth;
canvas.height = pageHeight;
window.onresize = function () {
  var pageWidth = document.documentElement.clientWidth;
  var pageHeight = document.documentElement.clientHeight;
  canvas.width = pageWidth;
  canvas.height = pageHeight;
};
using = false;
var lastPoint;
canvas.onmousedown = function (e) {

  var x = e.clientX;
  var y = e.clientY;
  if (eraserEnabled) {
    using = true;
    ctx.clearRect(x, y, 50, 50);
  }
  else {
    using = true;
    lastPoint = { "x": x, "y": y };
    console.log(lastPoint);
    drawCircle(x, y, 5);
  }


};

canvas.onmousemove = function (e) {
  var x = e.clientX;
  var y = e.clientY;
  if (eraserEnabled) {
    if (using) {
      ctx.clearRect(x, y, 50, 50);
    }

  }
  else {
    if (using) {

      var newPoint = { 'x': x, "y": y };
      console.log(newPoint);
      drawCircle(x, y, 5);

      drawLine(lastPoint.x, lastPoint.y, newPoint.x, newPoint.y);
      lastPoint = newPoint;
    }
  }

};
canvas.onmouseup = function (e) {
  using = false;
};




function drawCircle(x, y, radius) {
  ctx.beginPath();
  ctx.arc(x - radius / 2, y - radius / 2, radius, 0, Math.PI * 2, true);
  ctx.fill();

}

function drawLine(x1, y1, x2, y2) {
  ctx.beginPath();
  ctx.moveTo(x1, y1);
  ctx.lineTo(x2, y2);
  ctx.stroke();
  //   ctx.closPath();
}


var eraserEnabled = false;
eraser.onclick = function () {
  eraserEnabled = !eraserEnabled;
};


