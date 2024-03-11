#!/usr/bin/node

const Argument1 = process.argv[2];
const Argument2 = process.argv[3];

if (Argument1 === undefined && Argument2 === undefined) {
  console.log('undefined is undefined');
} else {
  console.log(Argument1 + ' is ' + Argument2);
}
