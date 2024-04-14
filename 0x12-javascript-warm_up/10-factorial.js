#!/usr/bin/node
const { argv } = require('process');
const num = parseInt(argv[2]);
function factorial (a) {
  if (a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
