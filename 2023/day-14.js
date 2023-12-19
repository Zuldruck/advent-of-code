const path = require('path');
const fs = require('fs');

const input = fs
  .readFileSync(path.join(__dirname, 'input.txt'), 'utf8')
  .toString()
  .trim()
  .split('\n');

let totalLoad = 0;
for (let y = 0; y < input[0].length; y++) {
  let availableRows = [];
  for (let x = 0; x < input.length; x++) {
    if (input[x][y] === '.' || input[x][y] === 'O') availableRows.push(x);
    if (input[x][y] === '#') availableRows = [];
    if (input[x][y] === 'O') {
      const row = availableRows.shift();
      totalLoad += input.length - row;
    }
  }
}

console.log(totalLoad);
