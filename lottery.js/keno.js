#!/usr/bin/env node

var async  = require('async');
var colors = require('colors');
var _ = require('underscore');
var fs = require('fs');
var taber = 'draw    data    tron' + 
            '| [ first ] [ last  ] ' +
            '| [ 01,02 ] [ 79,80 ]' + 
            '|   205.0    605.0    809.5  ' +
            '| + 40.5 чет ';

function podshchet (draw, calle) {
    async.parallel([
        // first, last - odd/even
        function (callback) {
            // first & last number 
            callback(null, [
                // first
                oddEven(draw[0] % 2 == 0),
                redGreen(draw[0] > 40.5),
                // last
                oddEven(draw[19] % 2 == 0),
                redGreen(draw[19] > 40.5)
            ].join(' '));
        },
        function (callback) {
            var res = [];
            var sortArr = draw.sort(function (a, b) { return a > b ? 1 : a < b ? -1 : 0 });      
            // [1, 2] & [79, 80]
            callback(null, [
                redGreen(draw.some(function (el) { return el == 1 || el == 2; })),
                oddEven(sortArr[0] % 2 == 0),
                redGreen(draw.some(function (el) { return el == 79 || el == 80; })),
                oddEven(sortArr[19] % 2 == 0),
            ].join(' '));
        },
        function (callback) {
            var s1 = draw
                .filter(function (el) { return el < 40.5; })
                .reduce(function (prev, curr) { return prev + curr });
            var s2 = draw
                .filter(function (el) { return el > 40.5; })
                .reduce(function (prev, curr) { return prev + curr });      
            var s3 = draw
                .reduce(function (prev, curr) { return prev + curr });
            // 200.5, 600.5, 800.5
            callback(null, [
                totalNew(s1, 205), oddEven(s1 % 2 == 0),
                totalNew(s2, 605), oddEven(s2 % 2 == 0),
                totalNew(s3, 809.5), oddEven(s3 % 2 == 0),
            ].join(' '));
        },
        function (callback) {
        //количество до 40.5 и четных
            callback(null, [
                totalTen(draw.filter(function (el) { return el < 40.5; }).length),
                totalTen(draw.filter(function (el) { return el % 2; }).length)
            ].join('  '));
        }
    ], function (err, results) {
        calle(results);
    });
}

function series (draw, ldr, calle) {
    async.parallel([
        // тотал десяток 2.5
        function (callback) {
            var resp = [0 ,0 ,0, 0, 0, 0, 0, 0], arry = [], i, j, k;
            for (i = 0; i < draw.length; i += 1) {
                j = Math.floor((draw[i] - 1) / 10);
                resp[j] += 1;
            }
            for (k = 0; k < resp.length; k += 1) {
                arry.push((resp[k] > 2.5) 
                    ? resp[k].toString().green 
                    : resp[k].toString().red);
            }
            callback(null, arry.join(' '));
        },
        //  by balls
        function (callback) {
            var someArr = '';
            for (var i = 0; i < 20; i++) {
                if (draw.some(function (val) { return val === ldr[i]; })) {
                    someArr += '  1'.green;
                } else {
                    someArr += '  0'.red;
                }
            };
            callback(null, someArr);
        }
    ], function (err, results) { calle(results) });
}

function redGreen(arg) { return (arg == true) ? 'true'.green : 'fals'.red; }

function oddEven(arg) { return (arg == true) ? 'odds'.green : 'even'.red; }

function totalNew(val, tot) {
    return ((val - tot) > 0)
        ? val.toString().green
        : ((val - tot) < 0)
            ? val.toString().red
            : val.toString().cyan;
}

function totalTen(val) {
    return (val > 10)
        ? val.toString().green
        : (val < 10)
            ? ('0' + val).toString().red
            : val.toString().cyan;
}

fs.readFile('results/keno.csv', 'utf-8', function (err, content) {
    var i, arr, resalts;
    //разбить файл на массив из строк
    arr = content.split(/\n/);
    console.log(taber.inverse);
    for (i = 0; i < 12; i += 1) {
        resalts = arr[i]
            .split(',')
            .slice(4)
            .map(function (i) { return parseInt(i, 10) });

        podshchet(resalts, function (otvet) {
            console.log(
                arr[i].split(',').slice(0, 4).join(" "),
                '| ',
                otvet.join(' | ')
            );
        });
    }

    /*
     * Шары по десяткам и вообще
    */

    var lastDraw = arr[0]
        .split(',')
        .slice(4)
        .map(function (i) { return parseInt(i, 10); })
        .sort(function (a, b) { return a > b ? 1 : a < b ? -1 : 0 });

    console.log((  //  print header
        'draw    data    tron| 0 1 2 3 4 5 6 7 | ' +
        lastDraw.map(function (val) { return (val > 10) ? val.toString() : '0' + val.toString()}).join(' ')).inverse);
    
    for (i = 0; i < 12; i += 1) { // по одной строке сравнивает последним тираж с данным
        resalts = arr[i]
            .split(',')
            .slice(4)
            .sort(function (a, b) { return a > b ? 1 : a < b ? -1 : 0; })
            .map(function (i) { return parseInt(i, 10) });

        series(resalts, lastDraw, function (otvet) {
            var tenth = arr[i].split(',').slice(0, 4).join(" ");
            console.log(tenth, '|', otvet.join(' |'));
        });
    }
});

var sortArr = draw.sort(function (a, b) { return a > b ? 1 : a < b ? -1 : 0 });
var sortArr = draw.sort((a, b) => a > b ? 1 : a < b ? -1 : 0);

var taber = `draw    data    tron 
            | [ first ] [ last  ]
            | [ 01,02 ] [ 79,80 ]
            |   205.0    605.0    809.5
            | + 40.5 чет`;