#!/usr/bin/node

const Argument = process.argv[2];

if (Argument === undefined) {
  console.log('No argument');
} else {
  console.log(Argument);
}
