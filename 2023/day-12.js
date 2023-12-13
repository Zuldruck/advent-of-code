const path = require('path');
const fs = require('fs');

const input = fs
  .readFileSync(path.join(__dirname, 'input.txt'), 'utf8')
  .toString()
  .trim()
  .split('\n');

const lines = input.map((line) => {
  const splittedLine = line.split(' ');
  return [
    splittedLine[0],
    splittedLine[1].split(',').map((nb) => parseInt(nb)),
  ];
});

const isSequenceValid = (sequence, groups) => {
  const splittedSequence = sequence.split('.').filter((s) => s !== '');
  if (splittedSequence.length !== groups.length) {
    return false;
  }
  for (let i = 0; i < groups.length; i++) {
    const currentGroup = groups[i];
    const currentSequence = splittedSequence[i];
    if (currentGroup !== currentSequence.length) {
      return false;
    }
  }
  return true;
};

const getNbPossibilitiesForHiddenSequence = (hiddenSequence, groups) => {
  let hiddenChars = 0;
  let possibilities = 0;
  for (const char of hiddenSequence) {
    if (char === '?') {
      hiddenChars++;
    }
  }
  for (let i = 0; i < 2 ** hiddenChars; i++) {
    const binary = i.toString(2).padStart(hiddenChars, '0');
    const binaryArray = binary.split('');
    let newSequence = '';
    let binaryIndex = 0;
    for (const char of hiddenSequence) {
      if (char === '?') {
        newSequence += binaryArray[binaryIndex] === '1' ? '#' : '.';
        binaryIndex++;
      } else {
        newSequence += char;
      }
    }
    if (isSequenceValid(newSequence, groups)) {
      possibilities++;
    }
  }
  return possibilities;
};

const possibilitiesSum = lines.reduce((sum, [hiddenSequence, groups], idx) => {
  return sum + getNbPossibilitiesForHiddenSequence(hiddenSequence, groups);
}, 0);

console.log(possibilitiesSum);
