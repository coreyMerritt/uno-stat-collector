from entities.Card import Card
from enums.Card_Color import CardColor
from enums.Card_Number import CardNumber

class AllPlayersDrawFour(Card):

  def __init__(self):
    self.color = CardColor.Black
    self.number = CardNumber.AllPlayersDrawFour
