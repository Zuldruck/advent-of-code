const path = require('path');
const fs = require('fs');

const input = fs
  .readFileSync(path.join(__dirname, 'input.txt'), 'utf8')
  .toString()
  .trim()
  .split('\n');

const grid = input.map((row) => row.split(''));
const firstPosition = grid.reduce((acc, row, rowIndex) => {
  const SIndex = row.indexOf('S');
  if (SIndex !== -1) {
    return [rowIndex, SIndex];
  }
  return acc;
}, []);

const allowedTileByDirection = {
  N: new Set(['F', '|', '7']),
  E: new Set(['J', '-', '7']),
  S: new Set(['L', '|', 'J']),
  W: new Set(['F', '-', 'L']),
};

const allowedDirectionByTile = {
  F: new Set(['E', 'S']),
  J: new Set(['N', 'W']),
  '|': new Set(['N', 'S']),
  '-': new Set(['E', 'W']),
  7: new Set(['S', 'W']),
  L: new Set(['N', 'E']),
};

const directionMatrix = {
  N: [-1, 0],
  E: [0, 1],
  S: [1, 0],
  W: [0, -1],
};

function isDirectionPossible(direction, actualTile, nextTile) {
  return (
    allowedTileByDirection[direction]?.has(nextTile) &&
    allowedDirectionByTile[actualTile]?.has(direction)
  );
}

let lastPosition = null;
let currentPosition = firstPosition;
let tileNb = 0;

grid[firstPosition[0]][firstPosition[1]] = 'F'; // hard coded

// PART 2
const positionsFromPath = [currentPosition];

while (true) {
  const [row, col] = currentPosition;
  const actualTile = grid[row][col];
  for (const direction of ['S', 'E', 'N', 'W']) {
    const [rowDiff, colDiff] = directionMatrix[direction];
    if (
      row + rowDiff >= grid.length ||
      col + colDiff >= grid[row].length ||
      row + rowDiff < 0 ||
      col + colDiff < 0 ||
      (lastPosition &&
        row + rowDiff === lastPosition[0] &&
        col + colDiff === lastPosition[1])
    ) {
      // console.log('OUT OF BOUNDS');
      continue;
    }
    const nextTile = grid[row + rowDiff][col + colDiff];
    if (isDirectionPossible(direction, actualTile, nextTile)) {
      tileNb += 1;

      // PART 2
      positionsFromPath.push([row + rowDiff, col + colDiff]);

      lastPosition = currentPosition;
      currentPosition = [row + rowDiff, col + colDiff];
      break;
    }
  }
  if (
    currentPosition[0] === firstPosition[0] &&
    currentPosition[1] === firstPosition[1]
  ) {
    break;
  }
}
console.log(tileNb / 2);

// PART 2
const replacedGrid = grid.map((row, rowIdx) =>
  row.map((col, colIdx) => {
    if (
      positionsFromPath.some(([row, col]) => row === rowIdx && col === colIdx)
    )
      return col;
    return '.';
  })
);
let inside = false;
let insideDots = 0;
for (let i = 0; i < replacedGrid.length; i++) {
  inside = false;
  for (let j = 0; j < replacedGrid[i].length; j++) {
    if (inside && replacedGrid[i][j] === '.') insideDots += 1;
    if (['F', '7', '|'].includes(replacedGrid[i][j])) inside = !inside;
  }
}
console.log(insideDots);
