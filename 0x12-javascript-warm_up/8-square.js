#!/usr/bin/node

const size = process.argv[2];
const str = 'X';

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += str;
    }
    console.log(row);
  }
}
