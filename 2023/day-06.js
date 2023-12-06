const path = require('path');
const fs = require('fs');

const input = fs
  .readFileSync(path.join(__dirname, 'input.txt'), 'utf8')
  .toString()
  .trim()
  .split('\n');

const times = [...input[0].matchAll(/\d+/g)].map((match) => parseInt(match[0]));
const recordDistances = [...input[1].matchAll(/\d+/g)].map((match) =>
  parseInt(match[0])
);

function getMultipliedPossibilities(races) {
  let multipliedPosssibilities = null;
  for (const race of races) {
    let possibilities = 0;

    for (let speed = 1; speed < race.time; speed++) {
      const remainingTime = race.time - speed; // speed is also the elapsed time
      const possibleDistance = remainingTime * speed;
      if (possibleDistance > race.recordDistance) possibilities++;
    }

    if (multipliedPosssibilities === null) {
      multipliedPosssibilities = possibilities;
    } else {
      multipliedPosssibilities *= possibilities;
    }
  }
  return multipliedPosssibilities ?? 0;
}

// PART 1
const races = times.map((time, index) => ({
  time,
  recordDistance: recordDistances[index],
}));
console.log(getMultipliedPossibilities(races));

// PART 2
const race = races.reduce(
  (acc, race) => ({
    time: Number(acc.time.toString() + race.time.toString()),
    recordDistance: Number(
      acc.recordDistance.toString() + race.recordDistance.toString()
    ),
  }),
  { time: '', recordDistance: '' }
);
console.log(getMultipliedPossibilities([race]));
