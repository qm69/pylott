var fs = require('fs');

fs.readFile('keno.csv', 'utf-8', function(err, content) {
  if (err) console.log(err);
  var i, tirag, results, test, serija = 0, total = 0, arry = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
  //  разбить файл на массив из строк
  var arr = content.split(/\n/);
  
  for (i = 0; i < arr.length; i += 1) {
    tirag = parseInt(arr[i].split(',')[0]);
    test = arr[i].split(',').slice(1).some(function (el) {
      return el == 79 || el == 80;
    });
    
    if (test == true) { serija += 1; total += 1; }
    else {
      if (serija != 0) {
        console.log(tirag - serija, serija);
        arry[serija - 1] += 1;
        serija = 0;
      } else { serija = 0;}
    }
  }
  console.log(total, arry);
});