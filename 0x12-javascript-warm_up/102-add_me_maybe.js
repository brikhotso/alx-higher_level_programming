#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  const incrementedNumber = number + 1;
  theFunction(incrementedNumber);
};
