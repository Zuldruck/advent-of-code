import functools

CardPriority = {
  'A': 14,
  'K': 13,
  'Q': 12,

  # PART 1
  # 'J': 11,

  'T': 10,
  '9': 9,
  '8': 8,
  '7': 7,
  '6': 6,
  '5': 5,
  '4': 4,
  '3': 3,
  '2': 2,

  # PART 2
  'J': 1,
}
HandTypes = {
  'FiveOfAKind': 7,
  'FourOfAKind': 6,
  'FullHouse': 5,
  'ThreeOfAKind': 4,
  'TwoPairs': 3,
  'OnePair': 2,
  'HighCard': 1,
}

def getCardOccurences(hand):
  cardOccurences = {}
  for card in hand:
    cardOccurences[card] = cardOccurences.get(card, 0) + 1
  return cardOccurences

def determineHandType(occurences):
  cardsRepeated = {}

  # PART 2
  jokerCount = occurences.get('J', 0)
  if jokerCount > 0:
    occurences['J'] = 0
  cardMostlyRepeated = max(occurences, key=occurences.get)
  occurences[cardMostlyRepeated] += jokerCount

  values = occurences.values()
  for value in values:
    cardsRepeated[value] = cardsRepeated.get(value, 0) + 1
  
  for card in cardsRepeated:
    if card == 5:
      return HandTypes['FiveOfAKind']
    elif card == 4:
      return HandTypes['FourOfAKind']
    elif card == 3:
      if 2 in cardsRepeated:
        return HandTypes['FullHouse']
      else:
        return HandTypes['ThreeOfAKind']
    elif card == 2:
      if 3 in cardsRepeated:
        return HandTypes['FullHouse']
      elif cardsRepeated[2] == 2:
        return HandTypes['TwoPairs']
      else:
        return HandTypes['OnePair']
  return HandTypes['HighCard']

def sortingFunc(hand1, hand2):
  hand1 = hand1[0]
  hand2 = hand2[0]

  hand1Type = determineHandType(getCardOccurences(hand1))
  hand2Type = determineHandType(getCardOccurences(hand2))

  if hand1Type > hand2Type:
    return 1
  elif hand1Type < hand2Type:
    return -1
  i = 0
  while i < len(hand1) and hand1[i] == hand2[i]:
    i += 1
  if i == len(hand1):
    return 0
  return CardPriority[hand1[i]] - CardPriority[hand2[i]]
    
with open('input.txt') as file:
  hands = file.read().split('\n')
  hands = [hand.split() for hand in hands] # [hand, bid]
  hands = [[hand[0], int(hand[1])] for hand in hands] # [hand, bid]

  hands = sorted(hands, key=functools.cmp_to_key(sortingFunc))
  winningHandsSum = 0
  for i in range(len(hands)):
    bid = hands[i][1]
    winningHandsSum += bid * (i + 1)
  print(winningHandsSum)
