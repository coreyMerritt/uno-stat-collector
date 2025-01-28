from entities.Card import Card
from enums.Card_Color import CardColor
from enums.Card_Number import CardNumber



class NullCard(Card):
  def __init__(self):
    self.color = CardColor.Null
    self.number = CardNumber.Null