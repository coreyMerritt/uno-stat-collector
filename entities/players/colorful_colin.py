import random

from entities.Player import Player
from enums.Card_Color import CardColor
from enums.Card_Number import CardNumber


### Colorful Colin chooses cards from his hand randomly, but
### picks colors based on what he has the most of.


class ColorfulColin(Player):
  foo = "Colorful Colin is just an implementation of Player defaults!"