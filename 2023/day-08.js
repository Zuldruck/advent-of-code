const path = require('path');
const fs = require('fs');

const input = fs
  .readFileSync(path.join(__dirname, 'input.txt'), 'utf8')
  .toString()
  .trim()
  .split('\n');

const directions = input[0].split('');

const nodes = {};
for (let i = 2; i < input.length; i++) {
  const [from, to] = input[i].split('=').map((x) => x.trim());
  const [left, right] = to.split(', ');
  nodes[from] = {
    name: from,
    leftName: left.substring(1),
    rightName: right.substring(0, right.length - 1), 
  }
}

// PART 1
let tmpNode = nodes.AAA;
let moves = 0;
while (tmpNode && tmpNode.name !== 'ZZZ') {
  const direction = directions[moves % directions.length];
  if (direction === 'L') {
    tmpNode = nodes[tmpNode.leftName];
  } else {
    tmpNode = nodes[tmpNode.rightName];
  }
  moves += 1;
}
console.log(moves);

// PART 2
const gcd = (a, b) => {
  if (b == 0) return a;
  return gcd(b, a % b);
};
 
// Returns LCM of array elements
const lcm = (numbers) => {
  // Initialize result
  let ans = numbers[0];

  for (let i = 1; i < numbers.length; i++)
    ans = (((numbers[i] * ans)) / (gcd(numbers[i], ans)));
  return ans;
};

let tmpNodes = Object.values(nodes).filter((node) => node.name[node.name.length - 1] === 'A');
const distancesToZ = tmpNodes.map((node) => {
  let tmpNode = node;
  let moves = 0;
  while (tmpNode.name[tmpNode.name.length - 1] !== 'Z') {
    const direction = directions[moves % directions.length];
    if (direction === 'L') {
      tmpNode = nodes[tmpNode.leftName];
    } else {
      tmpNode = nodes[tmpNode.rightName];
    }
    moves += 1;
  }
  return moves;
});

console.log(lcm(distancesToZ));
