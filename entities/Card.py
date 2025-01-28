from abc import ABC, abstractmethod
from typing import List
from enums.Card_Color import CardColor
from enums.Card_Number import CardNumber

class Card(ABC):
  color: CardColor
  number: CardNumber


@abstractmethod
def execute(self, players, owner, deck):
  pass