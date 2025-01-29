from entities.Game import Game
from entities.Player import Player


### 004 - Aggressive Agatha just likes to make people sad.
### Don't be an Aggressive Agatha, kids.


class AggressiveAgatha(Player):

  def pickCardToPlay(self, game: Game):
    legalCards = self.getLegalCards(game.faceColor, game.faceNumber)
    if len(legalCards) > 1:
      cardPicked = self.maxFirstCardPriority(legalCards)
    elif len(legalCards) == 1:
      cardPicked = legalCards[0]
    else:
      return None

    return cardPicked
