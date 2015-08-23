#!/usr/bin/env node

var fs = require('fs')
  , program = require('commander')
  , async  = require('async')
  , colors = require('colors');

program.version('0.0.1')
  .option('-k, --keno [type]', 'Keno')
  .option('-t, --trojka [type]', 'Trojka')
  .option('-p, --top3 [type]', 'Top 3')
  .parse(process.argv);

if (program.keno) console.log(program.keno);

