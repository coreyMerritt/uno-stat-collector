from enum import Enum


class CardNumber(Enum):
  Zero = 0
  One = 1
  Two = 2
  Three = 3
  Four = 4
  Five = 5
  Six = 6
  Seven = 7
  Eight = 8
  Nine = 9
  Reverse = "Reverse"
  Skip = "Skip"
  DrawTwo = "Draw Two"
  Wild = "Wild Card"
  DrawFour = "Draw Four"
  ShuffleHands = "Shuffle Hands"
  SwapHands = "Swap Hands"
  AllPlayersDrawTwo = "All Players Draw Two"
  AllPlayersDrawFour = "All Players Draw Four"
  DiscardAllOfOneColor = "Discard All of One Color"
  Null = 10