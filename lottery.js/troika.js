#!/usr/bin/env node

var async  = require('async');
var colors = require('colors');
var fs = require('fs');
var args = process.argv[2]; // pick3 || troika
var someArr = [];
var drawBalls = [];
var summMult = [];

function upperRow (draw, cb) {
    var ballOne = draw[0],
        ballTwo = draw[1],
        ballTri = draw[2];
    var sortArr = draw.sort(function (a, b) { return a > b ? 1 : a < b ? -1 : 0 }),
        summ = draw.reduce(function (pre, cur) { return pre + cur }),
        oddsArr = draw.filter(function (el) { return el % 2 === 0; }),
        evenArr = draw.filter(function (el) { return el % 2 !== 0; });

    async.parallel([
        //  1 Секция
        function (callback){
            /*
             * 1й, 2й и 3й > odd/even
             * 1й, 2й и 3й > больше 4.5
            */
            someArr.push([
                oddEven(ballOne % 2 == 0), moreLess(ballOne > 4.5),
                oddEven(ballTwo % 2 == 0), moreLess(ballTwo > 4.5),
                oddEven(ballTri % 2 == 0), moreLess(ballTri > 4.5)
            ].join(' '));
            drawBalls.push([ballOne, ballTwo, ballTri].join(' '));
            /*
             * Хотя бы один из выпавших номеров кратен 2 (0-не кратное): да 1.22; нет 4.44;
             * Сумма всех выпавших номеров кратна 2 (0-не кратное): да 1.92; нет 1.92;
             * Хотя бы один из выпавших номеров кратен 3 (0-не кратное): да 1.46; нет 2.80;
             * Сумма всех выпавших номеров кратна 3 (0-не кратное): да 2.88; нет 1.44;
             * Хотя бы один из выпавших номеров кратен 4 (0-не кратное): да 1.97; нет 1.88;
             * Сумма всех выпавших номеров кратна 4 (0-не кратное): да 3.87; нет 1.28;
            */
            summMult.push([
                totalOne(0.5, draw.filter(function (el) { if (el > 0) return el % 2 == 0; }).length),
                (summ % 2 == 0) ? 'mult'.green : 'unmu'.red,
                totalOne(0.5, draw.filter(function (el) { if (el > 0) return el % 3 == 0; }).length),
                (summ % 3 == 0) ? 'mult'.green : 'unmu'.red,
                totalOne(0.5, draw.filter(function (el) { if (el > 0) return el % 4 == 0; }).length),
                (summ % 4 == 0) ? 'mult'.green : 'unmu'.red,
            ].join(' '))
            /*
             * [0,1] & [8, 9] > true/false
             * наименьш & наибольш > odd/even
            */
            callback(null, [
                oddEven(sortArr[0] % 2 == 0),
                moreLess(draw.some(function (el) { return el == 0 || el == 1; })),
                oddEven(sortArr[2] % 2 == 0),
                moreLess(draw.some(function (el) { return el == 8 || el == 9; })),
            ].join(' '));
        },
        //  2 Секция
        function (callback){
            /*
             * Сумма odd/even
             * Количество четных 
             * Сумма всех выпавших четных номеров: бол. (4.5) 1.75; мен. (4.5) 2.13;
             * Сумма всех выпавших нечетных номеров : бол. (7.5) 2.02; мен. (7.5) 1.83;
             * Из выпавших номеров сумма четных больше, чем сумма нечетных : да 2.26; нет 1.67;
            */
            var oddsSumm = (oddsArr.length !== 0) ? oddsArr.reduce(function (pre, cur) { return pre + cur }) : 0,
                evenSumm = (evenArr.length !== 0) ? evenArr.reduce(function (pre, cur) { return pre + cur }): 0,
                odEvDiff = oddsSumm - evenSumm;
            //console.log(oddsSumm, evenSumm, odEvDiff)
            callback(null, [
                oddEven(summ % 2 == 0),
                totalOne(1.5, draw.filter(function (el) { return el % 2 === 0; }).length),
                totalCouner(4.5, oddsSumm),
                totalCouner(4.5, evenSumm),
                totalCouner((odEvDiff > 0) ? 0 : 100, (odEvDiff > 0) ? odEvDiff : -odEvDiff),
            ].join(' '));
        },
        //  3 Секция
        function (callback) {
            /*
             * Сумма наименьшего и наибольшего из выпавших номеров: бол. (9.5) 2.26; мен. (9.5) 1.67;
             * Разность наибольшего и наименьшего из выпавших номеров: бол. (5.5) 2.29; мен. (5.5) 1.66;
             * Сумма наименьшего и наибольшего из выпавших номеров: четная 1.96; нечетная 1.88;
             * Разность наибольшего и наименьшего из выпавших номеров: четная 1.96; нечетная 1.88;
             * Первый выпавший номер больше, чем второй: да 2.13; нет 1.75; @done (15-08-08 18:15)
             * Первый выпавший номер больше, чем последний: да 2.13; нет 1.75; @done (15-08-08 18:15)
            */
            callback(null, [
                totalCouner(9.5, sortArr[2] + sortArr[0]),
                oddEven((sortArr[2] + sortArr[0]) % 2 == 0),
                totalCouner(5.5, sortArr[2] - sortArr[0]),
                oddEven((sortArr[2] - sortArr[0]) % 2 == 0),
                (ballOne > ballTwo) ? 'more'.green : (ballOne < ballTwo) ? 'less'.red : 'eqal'.blue,
                (ballOne > ballTri) ? 'more'.green : (ballOne < ballTri) ? 'less'.red : 'eqal'.blue,
            ].join(' '));
        },
        //  4 Секция
        function (callback){
            /*
             1. Количество выпавших номеров от 0 до 3 включительно: 2 или 3 номера 2.70; 1 номер 2.20; 0 номеров 4.40;
             2. Сумма всех выпавших номеров от 0 до 3 включительно: бол. (1.5) 1.88; мен. (1.5) 1.96;
                ex. к-во меньше 4.5
             3. Количество выпавших номеров от 0 до 4 включительно: 2 или 3 номера 1.90; 1 номер 2.55; 0 номеров 7.30;
             4. Сумма всех выпавших номеров от 0 до 4 включительно: бол. (2.5) 1.75; мен. (2.5) 2.13;
             5. Количество выпавших номеров от 0 до 5 включительно: 3 номера 4.40; 2 номера 2.20; 0 или 1 номер 2.70;
             6. Количество выпавших номеров от 4 до 9 включительно: 3 номера 4.40; 2 номера 2.20; 0 или 1 номер 2.70;
             7. Количество выпавших номеров от 4 до 6 включительно: 2 или 3 номера 4.40; 1 номер 2.20; 0 номеров 2.70;
             8. Сумма всех выпавших номеров от 4 до 6 включительно: бол. (4.5) 1.88; мен. (4.5) 1.96;  
             9. Количество выпавших номеров от 5 до 9 включительно: 2 или 3 номера 1.90; 1 номер 2.55; 0 номеров 7.30;
            10. Сумма всех выпавших номеров от 5 до 9 включительно : бол. (10.5) 1.98; мен. (10.5) 1.86;
            11. Количество выпавших номеров от 7 до 9 включительно: 2 или 3 номера 4.40; 1 номер 2.20; 0 номеров 2.70;
            12. Сумма всех выпавших номеров от 7 до 9 включительно: бол. (7.5) 1.88; мен. (7.5) 1.96;  
            13. Тотал больше 13.5
             * Сумма всех выпавших номеров: 0-9 4.00; 10-13 3.20; 14-17 3.20; 18-27 4.00; 0-6 10.0; 7-8 10.0; 9-10 7.00;
             *                              11-12 6.00; 13-14 5.50; 15-16 6.00; 17-18 7.00; 19-20 10.0; 21-27 10.0;
            */
            var zeroThree = draw.filter(function (el) { return el <= 3; });
            var zeroFour = draw.filter(function (el) { return el <= 4; });
            var fourSix = draw.filter(function (el) { return el >= 4 && el >= 6; });
            var fiveNine = draw.filter(function (el) { return el >= 5; });
            var sevenNine = draw.filter(function (el) { return el >= 7; });
            callback(null, [
                totalOne(1.5, zeroThree.length),
                totalCouner(1.5, (zeroThree.length > 0) ? zeroThree.reduce(function (pre, cur) { return pre + cur }) : 0),
                totalOne(1.5, zeroFour.length),
                totalCouner(2.5, (zeroFour.length > 0) ? zeroFour.reduce(function (pre, cur) { return pre + cur }) : 0),
                totalOne(1.5, draw.filter(function (el) { return el <= 5; }).length),
                totalOne(1.5, draw.filter(function (el) { return el >= 4 && el >= 9; }).length),
                totalOne(1.5, fourSix.length),
                totalCouner(4.5, (fourSix.length > 0) ? fourSix.reduce(function (pre, cur) { return pre + cur }) : 0),
                totalOne(1.5, fiveNine.length),
                totalCouner(10.5, (fiveNine.length > 0) ? fiveNine.reduce(function (pre, cur) { return pre + cur }) : 0),
                totalOne(1.5, sevenNine.length),
                totalCouner(7.5, (sevenNine.length > 0) ? sevenNine.reduce(function (pre, cur) { return pre + cur }) : 0),
                totalCouner(13.5, summ),
            ].join(' '));
        },      
    ],function (err, results) { cb(results); });
}

function oddEven(arg) { return (arg == true) ? 'odds'.green : 'even'.red; }

function moreLess(arg) { return (arg == true) ? 'more'.green : 'less'.red; }

function totalOne(total, val) {
    return (val > total) ? val.toString().green :
      (val < total) ? val.toString().red : val.toString().cyan;
}

function totalCouner(total, val) {
    if (val < total) {
        return (val >= 0 && val < 10) ? ('0' + val).toString().red : val.toString().red;
    } else {
        return (val >= 0 && val < 10) ? ('0' + val).toString().green : val.toString().green;
    }
}

fs.readFile('results/3_x_10/' + args + '.csv', 'utf-8', function (err, content) {
    var i, arry, resalts, resp, lastDraw;
    arry = content.split(/\n/);
    lastDraw = arry[0].split(',').slice(4).map(function (i) { return parseInt(i, 10) });
    /*
     * Верхний ряд
    */
    var head = '[  0, 1 ] [  8, 9 ] ' +
               '|    odd / even   ' +
               '| first  >  second  >  last ' +
               '| 0-3  0-4  n-m 4-6  5-9  7-9  all';

    console.log(head.inverse);
    for (i = 0; i < 12; i += 1) {
        var res = arry[i].split(',');
        resalts = res.slice(4).map(function (i) { return parseInt(i, 10) });

        upperRow(resalts, function (otvet) {
            resp = otvet.join(' | ');
            console.log(resp);
        })
    }
    /*
     * Нижний ряд
    */
    var head = ' draw    data    tron' +
               '| Balls ' +
               '| 0 1 2 3 4 5 6 7 8 9  ' +
               '|     1й       2й        3й     ' +
               '|   2м     3м     4м  ';

    console.log(head.inverse);
    for (i = 0; i < 12; i += 1) {
        var tenth = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
        var text = '';
        var resp = arry[i].split(',');

        resp.slice(4)
            .map(function (i) { return parseInt(i, 10) })
            .forEach(function (ballDrop) { tenth[ballDrop]++ });

        tenth.forEach(function (val) {
            if (val === 0) { text += val.toString().blue  + ' '}
            else { text += val.toString().red + ' '}
        });
        var hujar = [resp.slice(0, 4).join(' '), drawBalls[i], text, someArr[i], summMult[i]];
        console.log(hujar.join(' | '));
    }

});
