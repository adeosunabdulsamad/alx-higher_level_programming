#!/usr/bin/node
const { argv } = require('process');
const num1 = parseInt(argv[2]);
const num2 = parseInt(argv[3]);
function add (a, b) {
  console.log(a + b);
}
add(num1, num2);
