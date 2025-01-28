from typing import List
from entities.Deck import Deck
from entities.Card import Card

class Hand:
  cards: List[Card]
  
  def __init__(self):
    self.cards = []
