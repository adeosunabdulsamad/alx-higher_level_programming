#!/usr/bin/node
const { argv } = require('process');
const num = argv[2];
if (isNaN(parseInt(num))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(num); i++) {
    console.log('X'.repeat(parseInt(num)));
  }
}
