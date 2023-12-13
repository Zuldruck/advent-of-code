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

const splitPossibilities = (possibilities, currentIndex, groups) => {
  const newPossibilities = {};

  for (let j = 0; j < possibilities.length; j++) {
    let possibility2Valid = true;
    const possibility = possibilities[j];
    const newPossibility1 = {
      ...possibility,
      sequence:
        possibility.sequence.substring(0, currentIndex) +
        '#' +
        possibility.sequence.substring(currentIndex + 1),
    };
    const newPossibility2 = {
      ...possibility,
      sequence:
        possibility.sequence.substring(0, currentIndex) +
        '.' +
        possibility.sequence.substring(currentIndex + 1),
    };
    if (
      newPossibility2.groupCharactersAmount > 0 &&
      newPossibility2.groupCharactersAmount !== groups[newPossibility2.groupIdx]
    ) {
      possibility2Valid = false;
    }
    if (newPossibility2.groupCharactersAmount > 0) {
      newPossibility2.groupIdx++;
      newPossibility2.groupCharactersAmount = 0;
    }
    const newPossibilitiesKey1 = `${newPossibility1.groupIdx};${newPossibility1.groupCharactersAmount};${newPossibility1.sequence[currentIndex]}`;
    const newPossibilitiesKey2 = `${newPossibility2.groupIdx};${newPossibility2.groupCharactersAmount};${newPossibility2.sequence[currentIndex]}`;
    if (!newPossibilities[newPossibilitiesKey1]) {
      newPossibilities[newPossibilitiesKey1] = newPossibility1;
    } else {
      newPossibilities[newPossibilitiesKey1].permutations +=
        newPossibility1.permutations;
    }
    if (!possibility2Valid) continue;
    if (!newPossibilities[newPossibilitiesKey2]) {
      newPossibilities[newPossibilitiesKey2] = newPossibility2;
    } else {
      newPossibilities[newPossibilitiesKey2].permutations +=
        newPossibility2.permutations;
    }
  }
  return Object.values(newPossibilities);
};

const getNbPossibilitiesForHiddenSequence = (hiddenSequence, groups) => {
  let possibilities = [
    {
      sequence: hiddenSequence,
      groupIdx: 0,
      groupCharactersAmount: 0,
      permutations: 1,
    },
  ];
  let toRemove = [];
  for (let i = 0; i < hiddenSequence.length; i++) {
    if (hiddenSequence[i] === '?')
      possibilities = splitPossibilities(possibilities, i, groups);

    for (let j = 0; j < possibilities.length; j++) {
      const possibility = possibilities[j];
      if (possibility.sequence[i] === '#') {
        possibility.groupCharactersAmount++;
        if (
          possibility.groupCharactersAmount > groups[possibility.groupIdx] ||
          (possibility.groupCharactersAmount === groups[possibility.groupIdx] &&
            i < hiddenSequence.length - 1 &&
            hiddenSequence[i + 1] === '#')
        ) {
          toRemove.push(j);
          continue;
        }
      }
      if (possibility.sequence[i] === '.') {
        if (
          possibility.groupCharactersAmount > 0 &&
          possibility.groupCharactersAmount !== groups[possibility.groupIdx]
        ) {
          toRemove.push(j);
          continue;
        }
        if (possibility.groupCharactersAmount > 0) possibility.groupIdx++;
        possibility.groupCharactersAmount = 0;
      }
    }

    possibilities = possibilities.filter((_, idx) => !toRemove.includes(idx));
    toRemove = [];
  }
  return possibilities.reduce((sum, possibility) => {
    if (
      (possibility.groupIdx === groups.length &&
        possibility.groupCharactersAmount === 0) ||
      (possibility.groupCharactersAmount === groups[possibility.groupIdx] &&
        possibility.groupIdx === groups.length - 1)
    )
      return sum + possibility.permutations;
    return sum;
  }, 0);
};

const possibilitiesSum = lines.reduce((sum, [hiddenSequence, groups], idx) => {
  // PART 2
  hiddenSequence = (hiddenSequence + '?').repeat(5);
  hiddenSequence = hiddenSequence.substring(0, hiddenSequence.length - 1);
  groups = (groups.join(',') + ',')
    .repeat(5)
    .split(',')
    .map((nb) => parseInt(nb))
    .filter((nb) => !isNaN(nb));

  const possibilities = getNbPossibilitiesForHiddenSequence(
    hiddenSequence,
    groups
  );

  return sum + possibilities;
}, 0);

console.log(possibilitiesSum);
