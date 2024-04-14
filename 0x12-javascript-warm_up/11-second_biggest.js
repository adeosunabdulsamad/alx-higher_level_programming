#!/usr/bin/node
const { argv } = require('process');
const array = [];
for (let i = 2; i < argv.length; i++) {
  array.push(parseInt(argv[i]));
}
array.sort((a, b) => a - b);
if (argv[2] === undefined || argv[3] === undefined) {
  console.log(0);
} else {
  console.log(array[array.length - 2]);
}
