#!/usr/bin/node

const Argument = process.argv[2];
const integer = parseInt(Argument);

if (isNaN(integer)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + integer);
}
