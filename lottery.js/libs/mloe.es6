"use strict";

exports.odd = function(arg) {
    return (arg == true)
        ? 'odds'.green
        : 'even'.red;
}

exports.more = function(arg) {
    return (arg == true)
        ? 'more'.green
        : 'less'.red;
}
