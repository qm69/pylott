//  io.js --harmony_arrow_functions --harmony_modules --harmony_destructuring
"use strict";

var fs = require('fs');
var colors = require('colors');
var totl = require('./libs/totl.es6');
var mloe = require('./libs/mloe.es6');
var diapaz = require('./libs/diapaz.es6');

var gameName = process.argv[2]; // pick3 || troika
var drawBalls =  [],  //  !!!
    metaData  =  [],
    ballLine =   [],  //  выпавшие шары
    oneTwoTri =  [],
    smallLarge = [],  //  наименьш и наибольш
    neighbors =  [],  //  + 1й > 2 & 1й > 3го; 1й, 2й & 3й
    multiple =   [],  //  кратный 2, 3, 4
    oddEven =    [],  //  чет и нечет
    allWinAmnt = [];  //  к-во и сумма

var fileName = 'results/3_x_10/' + gameName + '.csv';
var prom = new Promise((resolve, reject) => {
    fs.readFile(fileName, 'utf-8', (err, content) => {
        var arry, lastDraw;
        arry = content.split(/\n/);
        lastDraw = arry[0].split(',').slice(4).map(i => parseInt(i, 10));
        
        for (let i = 0; i < 12; i += 1) {

            let line = arry[i].split(',');
            let draw = line.slice(4).map(i => parseInt(i, 10));

            // change with '--harmony_destructuring'
            let ballOne = draw[0],
                ballTwo = draw[1],
                ballTri = draw[2];

            let sortArr = draw.sort((a, b) => a > b ? 1 : a < b ? -1 : 0);
            let summ = draw.reduce((pre, cur) => pre + cur);

            metaData.push(line.slice(0, 4).join(' '))
            drawBalls.push([ballOne, ballTwo, ballTri].join(' '));

            /*  ballLine  */
            let tenth = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
            let ballText = '';

            draw.forEach(ballDrop => tenth[ballDrop]++);

            tenth.forEach(val => {
                if (val === 0) {
                    ballText += val.toString().green  + ' '
                } else {
                    ballText += val.toString().red + ' '
                }
            });
            ballLine.push(ballText);

            /* smallLarge
             + Наименьший выпавший номер: бол. (1.5) 2.34;  мен. (1.5) 1.63; 
             + Наименьший выпавший номер: четный 1.60;  нечетный 2.40; 
             + Наибольший выпавший номер : бол. (7.5) 1.63;  мен. (7.5) 2.34; 
             + Наибольший выпавший номер: четный 2.40;  нечетный 1.60; 
             + Сумма наименьшего и наибольшего из выпавших номеров: четная 1.98;  нечетная 1.86; 
             + Сумма наименьшего и наибольшего из выпавших номеров: бол. (9.5) 2.40;  мен. (9.5) 1.60; 
             + Разность наибольшего и наименьшего из выпавших номеров: четная 1.98;  нечетная 1.86; 
             + Разность наибольшего и наименьшего из выпавших номеров: бол. (6.5) 2.24;  мен. (6.5) 1.68;
            */
            let smallest = sortArr[0], largest  = sortArr[2]; 
            let dataListS2 = [
                mloe.more(draw.some(el => el == 0 || el == 1)),
                mloe.odd(smallest % 2 == 0),
                mloe.more(draw.some(el => el == 8 || el == 9)),
                mloe.odd(largest % 2 == 0),
                totl.counter(9.5, smallest + largest),
                mloe.odd((smallest + largest) % 2 == 0),
                totl.counter(6.5, largest - smallest),
                mloe.odd((largest - smallest) % 2 == 0),
            ];
            smallLarge.push(dataListS2.join(' '));

            /* neighbors
             + Выпадут соседние номера: да 2.19;  нет 1.71; 
             + Выпадут совпадающие номера: да 3.43;  нет 1.33; 
             + Первый выпавший номер больше, чем последний: да 2.13;  нет 1.75; 
             + Первый выпавший номер больше, чем второй: да 2.13;  нет 1.75;
            */
            let nesWas = draw.map((val_1, ind, arr) => {
                return arr.some(val_2 => val_2 == val_1 - 1 || val_2 == val_1 + 1);
            });
            let neighbor = nesWas.some(val => val === true);
            let povtor = ballOne === ballTwo || ballTwo === ballTri || ballOne === ballTri;

            let dataListS3 = [
                (neighbor == true) ? 'true'.gray : 'fals'.red,
                (povtor == true) ? 'true'.gray : 'fals'.red,
                (ballOne > ballTwo) ? 'more'.green : (ballOne < ballTwo) ? 'less'.red : 'eqal'.gray,
                (ballOne > ballTri) ? 'more'.green : (ballOne < ballTri) ? 'less'.red : 'eqal'.gray,
            ];
            neighbors.push(dataListS3.join(' '));

            /* multiple
             + Хотя бы один из выпавших номеров кратен 2 (0-не кратное): да 1.22;  нет 4.44; 
             + Хотя бы один из выпавших номеров кратен 3 (0-не кратное): да 1.46;  нет 2.80; 
             + Хотя бы один из выпавших номеров кратен 4 (0-не кратное): да 1.97;  нет 1.88; 
             + Сумма всех вып. ном. кратна 2 (0-не кратное): да 1.92;  нет 1.92; 
             + Сумма всех вып. ном. кратна 3 (0-не кратное): да 2.88;  нет 1.44; 
             + Сумма всех вып. ном. кратна 4 (0-не кратное): да 3.87;  нет 1.28; 
            */
            let dataListS4 = [
                totl.one(0.5, draw.filter(el => { if (el > 0) return el % 2 == 0}).length),
                (summ % 2 == 0) ? 'm'.green : 'u'.red,
                totl.one(0.5, draw.filter(el => { if (el > 0) return el % 3 == 0}).length),
                (summ % 3 == 0) ? 'm'.green : 'u'.red,
                totl.one(0.5, draw.filter(el => { if (el > 0) return el % 4 == 0}).length),
                (summ % 4 == 0) ? 'm'.green : 'u'.red,
            ];
            multiple.push(dataListS4.join(' '));

            /* oddEven
             + Четных номеров выпадет больше, чем нечетных: да 1.92;  нет 1.92; 
             + Из выпавших номеров сумма четных больше, чем сумма нечетных : да 2.26;  нет 1.67; 
             - Из выпавших номеров сумма нечетных больше, чем сумма четных : да 1.76;  нет 2.11; 
             + Ко-во выпавших четных номеров : 2 или 3 номера 1.92;  1 номер 2.55;  0 номеров 7.00; 
             + Ко-во выпавших нечетных номеров : 2 или 3 номера 1.92;  1 номер 2.55;  0 номеров 7.00; 
             + Сумма всех выпавших четных номеров: бол. (4.5) 1.75;  мен. (4.5) 2.13; 
             + Сумма всех выпавших нечетных номеров : бол. (7.5) 2.02;  мен. (7.5) 1.83; 
            */
            let oddsArr = draw.filter(el => el % 2 === 0);
            let evenArr = draw.filter(el => el % 2 !== 0);
            let oddsSumm = (oddsArr.length !== 0) ? oddsArr.reduce((pre, cur) => pre + cur) : 0;
            let evenSumm = (evenArr.length !== 0) ? evenArr.reduce((pre, cur) => pre + cur) : 0;
            
            let dataListS5 = [
                mloe.more(oddsArr.length > evenArr.length),
                mloe.more(oddsSumm > evenSumm),
                totl.one(1.5, oddsArr.length),
                totl.one(1.5, evenArr.length),
                totl.counter(4.5, oddsSumm),
                totl.counter(7.5, oddsSumm),
            ];
            oddEven.push(dataListS5.join(' '));

            /* allWinAmnt
             + К-во вып. ном. от 0 до 3 включ: 2 или 3 номера 2.70;  1 номер 2.20;  0 номеров 4.40; 
             + Сумма всех вып. ном. от 0 до 3 включ: бол. (1.5) 1.88;  мен. (1.5) 1.96;              
             + К-во вып. ном. от 0 до 4 включ: 2 или 3 номера 1.90;  1 номер 2.55;  0 номеров 7.30; 
             + Сумма всех вып. ном. от 0 до 4 включ: бол. (2.5) 1.75;  мен. (2.5) 2.13; 
             + К-во вып. ном. от 0 до 5 включ: 3 номера 4.40;  2 номера 2.20;  0 или 1 номер 2.70; 
             + К-во вып. ном. от 4 до 6 включ: 2 или 3 номера 4.40;  1 номер 2.20;  0 номеров 2.70; 
             + Сумма всех вып. ном. от 4 до 6 включ: бол. (4.5) 1.88;  мен. (4.5) 1.96; 
             + К-во вып. ном. от 4 до 9 включ: 3 номера 4.40;  2 номера 2.20;  0 или 1 номер 2.70; 
             + К-во вып. ном. от 5 до 9 включ: 2 или 3 номера 1.90;  1 номер 2.55;  0 номеров 7.30; 
             + Сумма всех вып. ном. от 5 до 9 включ : бол. (10.5) 1.98;  мен. (10.5) 1.86;              
             + К-во вып. ном. от 7 до 9 включ: 2 или 3 номера 4.40;  1 номер 2.20;  0 номеров 2.70;
             + Сумма всех вып. ном. от 7 до 9 включ: бол. (7.5) 1.88;  мен. (7.5) 1.96;
             + Сумма всех вып. ном.: бол. (13.5) 1.92;  мен. (13.5) 1.92;
            */
            let dataListS6 = [
                diapaz.amount(draw, 0, 3),
                diapaz.summ(draw, 0, 3, 1.5),
                diapaz.amount(draw, 0, 4),
                diapaz.summ(draw, 0, 4, 2.5),
                diapaz.amount(draw, 0, 5),
                diapaz.amount(draw, 4, 6),
                diapaz.summ(draw, 4, 6, 4.5),
                diapaz.amount(draw, 4, 9),
                diapaz.amount(draw, 5, 9),
                diapaz.summ(draw, 5, 9, 10.5),
                diapaz.amount(draw, 7, 9),
                diapaz.summ(draw, 7, 9, 7.5),
                diapaz.summ(draw, 0, 9, 13.5),
            ];
            allWinAmnt.push(dataListS6.join(' '));

            /* oneTwoTri
             + 1-й номер: бол. (4.5) 1.92;  мен. (4.5) 1.92; 
             + 2-й номер: бол. (4.5) 1.92;  мен. (4.5) 1.92; 
             + 3-й номер: бол. (4.5) 1.92;  мен. (4.5) 1.92; 
             + 1-й номер: четный 1.92;  нечетный 1.92; 
             + 2-й номер: четный 1.92;  нечетный 1.92; 
             + 3-й номер: четный 1.92;  нечетный 1.92;  
            */
            let dataListS8 = [
                totl.counter(4.5, ballOne),
                mloe.odd(ballOne % 2 == 0),
                totl.counter(4.5, ballTwo),
                mloe.odd(ballTwo % 2 == 0),
                totl.counter(4.5, ballTri),
                mloe.odd(ballTri % 2 == 0),
            ]; 
            oneTwoTri.push(dataListS8.join(' '));

            if (i == 11) { resolve('done') };

        }
    });
}).then(value =>  {
    let headOne = ' draw    data    tron| Balls | 0 1 2 3 4 5 6 7 8 9  ' +
                  '|   1й      2й      3й    |        Соседи      ';
    var headTwo = '[  0, 1 ] [  8, 9 ]    Summ   Diff   |      odd / even     ' +
                  '|Кратн 2, 3, 4| 0-3  0-4  n-m 4-6  5-9  7-9  all';

    console.log(headOne.inverse);
    for (let i = 0; i < 12; i += 1) {
        console.log([
            metaData[i], drawBalls[i], ballLine[i],
            oneTwoTri[i], neighbors[i]].join(' | '));
    }

    console.log(headTwo.inverse);
    for (let i = 0; i < 12; i += 1) {
        console.log(' ' + [smallLarge[i], oddEven[i],
            multiple[i], allWinAmnt[i]].join(' | '));
    }
});
