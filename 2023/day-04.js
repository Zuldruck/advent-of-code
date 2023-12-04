const path = require('path');
const fs = require('fs');

const input = fs
  .readFileSync(path.join(__dirname, 'input.txt'), 'utf8')
  .toString()
  .trim()
  .split('\n');

const cards = input.map((line, index) => {
  const [, numbers] = line.split(': ');
  const [winningNumbers, cardNumbers] = numbers.split('|');
  const winningNumbersArray = winningNumbers.split(' ').map((number) => parseInt(number)).filter((number) => !isNaN(number));
  const cardNumbersArray = cardNumbers.split(' ').map((number) => parseInt(number)).filter((number) => !isNaN(number));
  return { cardNb: index + 1, winningNumbers: winningNumbersArray, cardNumbers: cardNumbersArray };
});

const cardWinningNumbersCount = {};

// PART 1
const sumOfPoints = cards.reduce((sum, card) => {
  const winningNumbersCount = card.winningNumbers.reduce((points, winningNumber) => {
    return points + (card.cardNumbers.includes(winningNumber) ? 1 : 0);
  }, 0);
  
  // PART 2
  cardWinningNumbersCount[card.cardNb] = winningNumbersCount;
  
  if (winningNumbersCount === 0) return sum;
  return sum + (winningNumbersCount === 1 ? 1 : 2 ** (winningNumbersCount - 1));
}, 0);

// PART 2
const scratchcards = cards.reduce((acc, card) => ({ ...acc, [card.cardNb]: 1 }), {});

for (const card of cards) {
  const cardNb = card.cardNb;
  const scratchcardNb = scratchcards[cardNb];
  const winningNumbersCount = cardWinningNumbersCount[cardNb];
  if (winningNumbersCount === 0) continue;
  for (let i = 1; i <= winningNumbersCount; i++) {
    scratchcards[cardNb + i] = scratchcards[cardNb + i] + scratchcardNb;
  }
}

console.log(sumOfPoints);
console.log(Object.values(scratchcards).reduce((sum, value) => sum + value, 0));
