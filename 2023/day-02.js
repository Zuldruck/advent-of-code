const path = require('path');
const fs = require('fs');

const input = fs
  .readFileSync(path.join(__dirname, 'input.txt'), 'utf8')
  .toString()
  .trim()
  .split('\n');

const games = input.map((line) => {
  // get game number from line which is in the form 'Game X: ...'
  const gameNb = line.match(/Game (\d+):/)[1];
  const [, splitsString] = line.split(': ');
  const splits = splitsString.split(';');
  const formattedSplits = splits.map((split) => {
    const colorsStrings = split.trim().split(', ');
    const colors = colorsStrings.map((colorString) => {
      const [quantity, color] = colorString.split(' ');
      return { color, quantity: parseInt(quantity) };
    });
    return {
      red: colors.find((color) => color.color === 'red'),
      green: colors.find((color) => color.color === 'green'),
      blue: colors.find((color) => color.color === 'blue'),
    };
  });
  return { gameNb, splits: formattedSplits };
});

// PART 1
const possibleGames = games.filter((game) => {
  // Find games where each of the splits are lower or equal than 12 red, 13 green and 14 blue
  return game.splits.every((split) => {
    return (
      (split.red?.quantity || 0) <= 12 &&
      (split.green?.quantity || 0) <= 13 &&
      (split.blue?.quantity || 0) <= 14
    );
  });
});

const gameNbAddition = possibleGames.reduce((acc, game) => {
  return acc + parseInt(game.gameNb);
}, 0);

console.log(gameNbAddition);

// PART 2
const maximumColorsPerGame = games.map((game) => {
  const reds = game.splits.map((split) => split.red?.quantity || 0);
  const greens = game.splits.map((split) => split.green?.quantity || 0);
  const blues = game.splits.map((split) => split.blue?.quantity || 0);
  return {
    red: Math.max(...reds),
    green: Math.max(...greens),
    blue: Math.max(...blues),
  };
});

const productOfMaximumColors = maximumColorsPerGame.reduce((acc, game) => {
  return acc + game.red * game.green * game.blue;
}, 0);

console.log(productOfMaximumColors);
