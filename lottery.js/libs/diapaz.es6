"use strict";

// diapazon Amount
exports.amount = function (draw, form, to) {
    let data = draw.filter(el => el >= form && el <= to).length;
    switch (data) {
      case 0:
        return data.toString().blue;
      case 1:
        return data.toString().green;
      case 2:
        return data.toString().gray;
      case 3:
        return data.toString().white;
    }
}

// diapazon Summ
exports.summ = function (draw, form, to, total) {
    let filt = draw.filter(el => el >= form && el <= to);
    let summ = (filt.length > 0) ? filt.reduce((pre, cur) => pre + cur) : 0;
    if (summ > total) {
        return (summ >= 0 && summ < 10)
            ? ('0' + summ).toString().gray
            : summ.toString().gray;
    } else {
        return (summ >= 0 && summ < 10)
            ? ('0' + summ).toString().red
            : summ.toString().red;        
    }
}