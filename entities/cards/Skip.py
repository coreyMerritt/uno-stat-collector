from entities.Card import Card
from enums.Card_Color import CardColor
from enums.Card_Number import CardNumber

class Skip(Card):

  def __init__(self, color: CardColor):
    self.color = color
    self.number = CardNumber.Skip
