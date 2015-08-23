#!/usr/bin/env node

var fs = require('fs')
  , program = require('commander')
  , async  = require('async')
  , colors = require('colors');
var ballStat = {
  1 : 3.87,
  2 : 3.94,
  3 : 3.92,
  4 : 4.01,
  5 : 4.02,
  6 : 3.90,
  7 : 4.04,
  8 : 4.14,
  9 : 3.94,
  10 : 3.74,
  11 : 4.10,
  12 : 4.13,
  13 : 4.22,
  14 : 4.19,
  15 : 4.24,
  16 : 4.16,
  17 : 4.14,
  18 : 3.94,
  19 : 4.10,
  20 : 4.12,
  21 : 3.97,
  22 : 3.96,
  23 : 4.01,
  24 : 3.90,
  25 : 3.91,
  26 : 3.98,
  27 : 3.95,
  28 : 3.96,
  29 : 3.83,
  30 : 4.00,
  31 : 4.00,
  32 : 4.11,
  33 : 4.08,
  34 : 3.97,
  35 : 3.92,
  36 : 3.99,
  37 : 4.03,
  38 : 4.15,
  39 : 4.04,
  40 : 3.92,
  41 : 4.00,
  42 : 3.94,
  43 : 3.94,
  44 : 3.99,
  45 : 4.23,
  46 : 4.00,
  47 : 3.99,
  48 : 4.07,
  49 : 4.14,
  50 : 4.06,
  51 : 4.01,
  52 : 3.88,
  53 : 3.93,
  54 : 4.12,
  55 : 4.04,
  56 : 4.03,
  57 : 3.94,
  58 : 3.91,
  59 : 3.92,
  60 : 3.93,
  61 : 3.86,
  62 : 3.83,
  63 : 3.77,
  64 : 3.97,
  65 : 3.92,
  66 : 3.86,
  67 : 3.92,
  68 : 3.83,
  69 : 3.87,
  70 : 3.92,
  71 : 4.25,
  72 : 3.94,
  73 : 4.04,
  74 : 4.05,
  75 : 4.14,
  76 : 4.07,
  77 : 4.17,
  78 : 3.94,
  79 : 4.28,
  80 : 4.10,
};

program.version('0.0.1')
  .option('-k, --keno [type]', 'Keno')
  .option('-t, --trojka [type]', 'Trojka')
  .option('-p, --top3 [type]', 'Top 3')
  .parse(process.argv);

//if (program.keno) console.log(program.keno);

fs.readFile('results/keno.csv', 'utf-8', function(err, data) {

  var lastResult = data.split(/\n/)[0].split(',').slice(1); // return strings
  var allResults = data.split(/\n/);
  var stats = [];

  var num = parseInt(program.keno, 10);

    for (var j = 0; j < 160; j += 1) {
      var daNet = allResults[j].split(',').slice(1).some(function (el) {
        return el == num;
      });
      stats.push((daNet == true) ? 1 : 0);
    };
  
  function hujunction (a, b) {
    var qwe = stats.slice(a, b).reduce(function (prev, curr) {return prev + curr;});
    var period = b - a + 1;
    var twe = Math.round((qwe - (1 / ballStat[num] * period)) * 100) / 100;
    console.log(period, qwe, twe);
  }

  hujunction(0, 11);
  hujunction(0, 19);
  hujunction(0, 39);
  hujunction(40, 79);
  hujunction(80, 119);
  hujunction(120, 159);
});