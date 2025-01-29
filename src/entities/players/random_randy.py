import random
from typing import List
from entities.Game import Game
from entities.Player import Player
from enums.Card_Color import CardColor


### 001 - Random Randy chooses cards from his hand randomly, as well
### as picks colors entirely randomly. He's not bright...


class RandomRandy(Player):
  
  def pickFaceColor(self):
    randomNum = random.randint(1, 4)
    if randomNum == 1:
      return CardColor.Yellow
    if randomNum == 2:
      return CardColor.Green
    if randomNum == 3:
      return CardColor.Red
    if randomNum == 4:
      return CardColor.Blue
    

  
  def discardAllOfOneColor(self):
    randomNum = random.randint(1, 4)
    discardColor = None
    if randomNum == 1:
      discardColor = CardColor.Yellow
    if randomNum == 2:
      discardColor = CardColor.Green
    if randomNum == 3:
      discardColor = CardColor.Red
    if randomNum == 4:
      discardColor = CardColor.Blue
    
    cardsToDiscard = []
    for card in self.hand.cards:
      if card.color == discardColor:
        cardsToDiscard.append(card)
        
    return cardsToDiscard
  


  def pickPlayerToSwapWith(self, players: List[Player]) -> Player:
    playerCount = len(players)
    randomIndex = random.randint(0, playerCount - 1)
    return players[randomIndex]
