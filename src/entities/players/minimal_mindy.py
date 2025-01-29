from entities.Game import Game
from entities.Player import Player


### 003 - Minimal mandy chooses the "card to play" based on a
### "less valuable card first" model, judged subjectively.


class MinimalMindy(Player):

  def pickCardToPlay(self, game: Game):
    legalCards = self.getLegalCards(game.faceColor, game.faceNumber)
    if len(legalCards) > 1:
      cardPicked = self.minFirstCardPriority(legalCards)
    elif len(legalCards) == 1:
      cardPicked = legalCards[0]
    else:
      return None

    return cardPicked
