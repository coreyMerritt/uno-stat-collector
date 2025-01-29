from entities.Game import Game
from entities.Player import Player
from enums.Card_Color import CardColor
from enums.Card_Number import CardNumber


### This is a template for ease of new player creation.


class Template(Player):

  def pickCardToPlay(self, game: Game):
    legalCards = self.getLegalCards(game.faceColor, game.faceNumber)
    if len(legalCards) > 1:
      # Some logic here to determine which legalCards index to use.
      cardPicked = ...
    elif len(legalCards) == 1:
      cardPicked = legalCards[0]
    else:
      return None

    return cardPicked



  def pickFaceColor(self):
    # Some logic here to detemine the color choice.
    # Type should be CardColor
    colorPicked = ...   
    return colorPicked