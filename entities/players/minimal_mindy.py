from typing import List
from entities.Card import Card
from entities.Player import Player
from enums.Card_Color import CardColor
from enums.Card_Number import CardNumber


### Minimal mandy chooses the "card to play" based on a
### "less valuable card first" model, judged subjectively.c


class MinimalMindy(Player):

  def pickCardToPlay(self, faceColor: CardColor, faceNumber: CardNumber):
    legalCards = self.getLegalCards(faceColor, faceNumber)
    if len(legalCards) > 1:
      index = self.cardPriority(legalCards)
      cardPicked = legalCards[index]
    elif len(legalCards) == 1:
      cardPicked = legalCards[0]
    else:
      return None

    self.hand.cards.remove(cardPicked)
    return cardPicked



  def cardPriority(self, legalCards: List[Card]):
    # Simple Numbers First
    for i, card in enumerate(legalCards):
      if card.color != CardColor.Black:
        if card.number != CardNumber.DrawTwo:
          if card.number != CardNumber.Skip:
            if card.number != CardNumber.Reverse:
              return i
            
    for i, card in enumerate(legalCards):
      if card.number == CardNumber.Reverse:
        return i
    
    for i, card in enumerate(legalCards):
      if card.number == CardNumber.Skip:
        return i
      
    for i, card in enumerate(legalCards):
      if card.number == CardNumber.DrawTwo:
        return i
    
    for i, card in enumerate(legalCards):
      if card.number == CardNumber.Wild:
        return i
      
    for i, card in enumerate(legalCards):
      if card.number == CardNumber.AllPlayersDrawTwo:
        return i
      
    for i, card in enumerate(legalCards):
      if card.number == CardNumber.AllPlayersDrawFour:
        return i
      
    for i, card in enumerate(legalCards):
      if card.number == CardNumber.DiscardAllOfOneColor:
        return i
    
    for i, card in enumerate(legalCards):
      if card.number == CardNumber.DrawFour:
        return i
    
    for i, card in enumerate(legalCards):
      if card.number == CardNumber.ShuffleHands:
        return i
    
    for i, card in enumerate(legalCards):
      if card.number == CardNumber.SwapHands:
        return i