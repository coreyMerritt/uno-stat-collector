from entities.Card import Card
from enums.Card_Color import CardColor
from enums.Card_Number import CardNumber

class NumberCard(Card):

  def __init__(self, color: CardColor, number: CardNumber):
    self.color = color
    self.number = number
