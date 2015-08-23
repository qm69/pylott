var fs = require('fs');
var Table = require('cli-table');
var colors = require('colors');

fs.readFile('../results/keno.csv', 'utf-8', function(err, data) {

  var lastResult = data
      .split(/\n/)[0]
      .split(',')
      .slice(1)
      .map(function (val) { return parseInt(val, 10) })
      .sort(function (a, b) { return a > b ? 1 : a < b ? -1 : 0; })
  ;

  var allResults = data.split(/\n/);
  var statArray = [];

  for (var i = 0; i < 12; i += 1) {
    var res = [];
    for (var j = 0; j < 20; j += 1) {   
      var trueFalse = allResults[i]
          .split(',')
          .some(function (el) {return el == lastResult[j];
      });
      res.push((trueFalse == true) ? '1 ' : '0 ');
    };
    statArray.push(res);
  };

//console.log(table.toString());
  console.log('  ' + lastResult.join(' '));
  for (var k = 0; k < 12; k++) {
    var asd = statArray[k]
        .map(function(val){return (val == 1) 
          ? val.toString().green 
          : val.toString().red; })
        .join(' ');   
    console.log(asd);
  };
});