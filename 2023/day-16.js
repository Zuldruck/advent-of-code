const path = require('path');
const fs = require('fs');

const DIRECTION = {
  UPWARD: 0,
  LEFTWARD: 1,
  DOWNWARD: 2,
  RIGHTWARD: 3,
};
const DIRECTION_DIFFERENCE = {
  [DIRECTION.UPWARD]: [-1, 0],
  [DIRECTION.LEFTWARD]: [0, -1],
  [DIRECTION.DOWNWARD]: [1, 0],
  [DIRECTION.RIGHTWARD]: [0, 1],
};
const REFLECTIONS = {
  '-': {
    [DIRECTION.UPWARD]: [DIRECTION.LEFTWARD, DIRECTION.RIGHTWARD],
    [DIRECTION.DOWNWARD]: [DIRECTION.LEFTWARD, DIRECTION.RIGHTWARD],
  },
  '|': {
    [DIRECTION.LEFTWARD]: [DIRECTION.UPWARD, DIRECTION.DOWNWARD],
    [DIRECTION.RIGHTWARD]: [DIRECTION.UPWARD, DIRECTION.DOWNWARD],
  },
  '/': {
    [DIRECTION.UPWARD]: [DIRECTION.RIGHTWARD],
    [DIRECTION.LEFTWARD]: [DIRECTION.DOWNWARD],
    [DIRECTION.DOWNWARD]: [DIRECTION.LEFTWARD],
    [DIRECTION.RIGHTWARD]: [DIRECTION.UPWARD],
  },
  '\\': {
    [DIRECTION.UPWARD]: [DIRECTION.LEFTWARD],
    [DIRECTION.LEFTWARD]: [DIRECTION.UPWARD],
    [DIRECTION.DOWNWARD]: [DIRECTION.RIGHTWARD],
    [DIRECTION.RIGHTWARD]: [DIRECTION.DOWNWARD],
  },
};

const grid = fs
  .readFileSync(path.join(__dirname, 'input.txt'), 'utf8')
  .toString()
  .trim()
  .split('\n');

function updateBeam(beam, grid) {
  const reflections = REFLECTIONS[grid[beam.pos[0]][beam.pos[1]]]?.[beam.direction] || [beam.direction];
  
  beam.direction = reflections[0];
  
  const directionDifference = DIRECTION_DIFFERENCE[beam.direction];
  const newBeamPos = [beam.pos[0] + directionDifference[0], beam.pos[1] + directionDifference[1]];

  if (reflections.length > 1) {
    const directionDifference = DIRECTION_DIFFERENCE[reflections[1]];
    const newBeam = {
      direction: reflections[1],
      pos: [beam.pos[0] + directionDifference[0], beam.pos[1] + directionDifference[1]],
    };
    beam.pos = newBeamPos;
    return newBeam;
  }
  
  beam.pos = newBeamPos;
  return null;
}

function hashPos(pos) {
  return `x${pos[0]}y${pos[1]}`;
}

function isBeamLooping(beam, energizedTiles) {
  const energizedTile = energizedTiles[hashPos(beam.pos)];
  return energizedTile?.[beam.direction];
}

function isBeamOutOfBounds(beam, grid) {
  return (
    beam.pos[0] < 0 || beam.pos[0] >= grid.length
    || beam.pos[1] < 0 || beam.pos[1] >= grid[beam.pos[0]].length
  );
}

function countEnergizedTiles(grid, startingPos, startingDirection) {
  const energizedTiles = {};
  const beams = [{ pos: startingPos, direction: startingDirection }];
  const toRemoveBeamIds = [];
  const toAddBeams = [];

  while (beams.length) {
    for (let i = 0; i < beams.length; i++) {
      const beam = beams[i];
      if (isBeamOutOfBounds(beam, grid) || isBeamLooping(beam, energizedTiles)) {
        toRemoveBeamIds.push(i);
        continue;
      }
      const energizedTile = energizedTiles[hashPos(beam.pos)];
      if (!energizedTile) energizedTiles[hashPos(beam.pos)] = { [beam.direction]: true };
      else energizedTile[beam.direction] = true;
      const toAddBeam = updateBeam(beam, grid);
      if (toAddBeam) toAddBeams.push(toAddBeam);
    }
    while (toRemoveBeamIds.length) {
      beams.splice(toRemoveBeamIds.pop(), 1);
    }
    while (toAddBeams.length) {
      beams.push(toAddBeams.pop());
    }
  }

  return Object.keys(energizedTiles).length;
}

// PART 1
console.log(countEnergizedTiles(grid, [0, 0], DIRECTION.RIGHTWARD));

// PART 2
function getStartingDirectionsFromPos(x, y, grid) {
  if (x === 0 && y === 0) return [DIRECTION.RIGHTWARD, DIRECTION.DOWNWARD];
  if (x === grid.length - 1 && y === grid[x].legnth - 1) return [DIRECTION.LEFTWARD, DIRECTION.UPWARD];
  if (x === grid.length - 1 && y === 0) return [DIRECTION.RIGHTWARD, DIRECTION.UPWARD];
  if (x === 0 && y === grid[x].legnth - 1) return [DIRECTION.LEFTWARD, DIRECTION.DOWNWARD];
  if (x === 0) return [DIRECTION.DOWNWARD];
  if (y === 0) return [DIRECTION.RIGHTWARD];
  if (x === grid.length - 1) return [DIRECTION.UPWARD];
  if (y === grid[x].length - 1) return [DIRECTION.LEFTWARD];
  return [];
}

let max = -Infinity;
for (let x = 0; x < grid.length; x++) {
  for (let y = 0; y < grid[x].length; y++) {
    if (!(x === 0 || x === grid.length - 1 || y === 0 || y === grid[x].length - 1)) continue;
    const directions = getStartingDirectionsFromPos(x, y, grid);
    for (const direction of directions) {
      max = Math.max(max, countEnergizedTiles(grid, [x, y], direction));
    }
  }
}
console.log(max);
