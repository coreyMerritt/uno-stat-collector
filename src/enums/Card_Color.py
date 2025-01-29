#!/usr/bin/env python3

from enum import Enum

class CardColor(Enum):
  Black = "Black"
  Yellow = "Yellow"
  Green = "Green"
  Red = "Red"
  Blue = "Blue"
  Null = "Null"

  def __str__(self):
    return self.name

