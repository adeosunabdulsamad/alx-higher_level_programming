#!/usr/bin/node
const { argv } = require('process');
const num = argv[2];
if (isNaN(parseInt(num))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(num));
}
