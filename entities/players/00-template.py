from entities.Player import Player
from enums.Card_Color import CardColor
from enums.Card_Number import CardNumber


### This is a template for ease of new player creation.


class Template(Player):

  def pickCardToPlay(self, faceColor: CardColor, faceNumber: CardNumber):
    legalCards = self.getLegalCards(faceColor, faceNumber)
    if len(legalCards) > 1:
      # Some logic here to determine which legalCards index to use.
      cardPicked = legalCards[0000000000]
    elif len(legalCards) == 1:
      cardPicked = legalCards[0]
    else:
      return None

    self.hand.cards.remove(cardPicked)
    return cardPicked



  def pickFaceColor(self):
    colorPicked = CardColor.Null   # Some logic here to detemine the color choice.
    return colorPicked