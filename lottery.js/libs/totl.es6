"use strict";

exports.counter = function (total, value) {
    if (value < total) {
        return (value >= 0 && value < 10)
            ? ('0' + value).toString().red
            : value.toString().red;
    } else {
        return (value >= 0 && value < 10)
            ? ('0' + value).toString().green
            : value.toString().green;
    }
}

exports.one = function (total, val) {
    return (val > total)
        ? val.toString().green
        : (val < total)
            ? val.toString().red
            : val.toString().cyan;
}