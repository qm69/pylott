var fs = require('fs');

fs.readFile('results/keno.csv', 'utf-8', function(err, content) {
  var i, arr, tirag, resalts;
  //  разбить файл на массив из строк
  arr = content.split(/\n/);

  for (i = 0; i < 10; i += 1) {
    tirag = arr[i].split(',')[0];
    resalts = arr[i].split(',').slice(1);
    
    console.log(tirag, resalts);
  }

});