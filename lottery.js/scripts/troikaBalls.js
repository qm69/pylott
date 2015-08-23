var fs = require('fs');
var colors = require('colors');

var ballStat = {
  0 : 3.27, 1 : 3.53, 2 : 3.23, 3 : 3.29, 4 : 3.28,
  5 : 3.27, 6 : 3.30, 7 : 3.42, 8 : 3.53, 9 : 3.44
};

fs.readFile('../res/troika.csv', 'utf-8', function (err, data) {

  var lastResult = data.split(/\n/)[0].split(',').slice(1); // return strings
  var allResults = data.split(/\n/);
  var stats = {};
  console.log(stats)

  for (var i = 0; i < lastResult.length; i += 1) {
    stats[lastResult[i]] = [];
    for (var j = 0; j < 66; j += 1) {
      var daNet = (allResults[j].split(',').slice(1).some(function (el) {
        return el == lastResult[i];}) == true) ? 1 : 0;
      // if (j == 1 && daNet == 0) break;
      stats[lastResult[i]][j] = daNet;
    };
  };

  /*
   * вынести все в фунцию и переделать подсчет если выпадает дубль
  */
  for (stat in stats) {

    var twelv = stats[stat].slice(0, 9).reduce(function (prev, curr) {return prev + curr;});
    var shmerty = stats[stat].slice(0, 32).reduce(function (prev, curr) {return prev + curr;});
    var forty = stats[stat].slice(33, 65).reduce(function (prev, curr) {return prev + curr;});
    console.log(
      (stat < 10) ? '0' + stat : stat,
      stats[stat].slice(0, 11).join(' '),
      [twelv, Math.round((twelv - (1 / ballStat[stat] * 10)) * 100) / 100],
      [shmerty, Math.round((shmerty - (1 / ballStat[stat] * 33)) * 100) / 100],
      [forty, Math.round((forty - (1 / ballStat[stat] * 33)) * 100) / 100]
    )
  }
});
