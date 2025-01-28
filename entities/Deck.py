from typing import List
import random
from entities.Card import Card
from entities.cards.Discard_All_Of_One_Color import DiscardAllOfOneColor
from enums.Card_Color import CardColor
from entities.cards.Number_Card import NumberCard
from entities.cards.Reverse import Reverse
from entities.cards.Skip import Skip
from entities.cards.Draw_Two import DrawTwo
from entities.cards.Wild import Wild
from entities.cards.Draw_Four import DrawFour
from entities.cards.Shuffle_Hands import ShuffleHands
from entities.cards.Swap_Hands import SwapHands
from entities.cards.All_Players_Draw_Two import AllPlayersDrawTwo
from entities.cards.All_Players_Draw_Four import AllPlayersDrawFour
from enums.Card_Number import CardNumber
from utilities.Logger import Logger



class Deck:
  cards: List[Card]
  discard: List[Card]

  def __init__(self, deckCount: int):
    self.cards = []
    self.discard  = []

    self.loadZero(deckCount)
    self.loadOneThroughNine(deckCount * 2)
    self.loadReverseCards(deckCount * 2)
    self.loadSkipCards(deckCount * 2)
    self.loadDrawTwoCards(deckCount * 2)
    self.loadWildCards(deckCount * 4)
    self.loadDrawFours(deckCount * 4)
    self.loadAllPlayersDrawTwo(deckCount)
    self.loadAllPlayersDrawFour(deckCount)
    self.loadDiscardAllOfOneColor(deckCount)
    self.loadShuffleHands(deckCount)
    self.loadSwapHands(deckCount)
    self.shuffleDeck()

  
  def loadZero(self, cardQuantity):
    for i in range(cardQuantity):
      for color in CardColor:
        if color != CardColor.Black and color != CardColor.Null:        
          self.cards.append(NumberCard(color, CardNumber.Zero))


  def loadOneThroughNine(self, cardQuantity):
    for i in range(cardQuantity):
      for num in range(1, 10):
        for color in CardColor:
          if color != CardColor.Black and color != CardColor.Null:
            match num:
              case 1:
                self.cards.append(NumberCard(color, CardNumber.One))
              case 2:
                self.cards.append(NumberCard(color, CardNumber.Two))
              case 3:
                self.cards.append(NumberCard(color, CardNumber.Three))
              case 4:
                self.cards.append(NumberCard(color, CardNumber.Four))
              case 5:
                self.cards.append(NumberCard(color, CardNumber.Five))
              case 6:
                self.cards.append(NumberCard(color, CardNumber.Six))
              case 7:
                self.cards.append(NumberCard(color, CardNumber.Seven))
              case 8:
                self.cards.append(NumberCard(color, CardNumber.Eight))
              case 9:
                self.cards.append(NumberCard(color, CardNumber.Nine))
                

  def loadReverseCards(self, cardQuantity):
    for i in range(cardQuantity):
      for color in CardColor:
        if color != CardColor.Black: 
          if color != CardColor.Null:
            self.cards.append(Reverse(color))


  def loadSkipCards(self, cardQuantity):
    for i in range(cardQuantity):
      for color in CardColor:
        if color != CardColor.Black: 
          if color != CardColor.Null:
            self.cards.append(Skip(color))


  def loadDrawTwoCards(self, cardQuantity):
    for i in range(cardQuantity):
      for color in CardColor:
        if color != CardColor.Black: 
          if color != CardColor.Null:
            self.cards.append(DrawTwo(color))


  def loadWildCards(self, cardQuantity):
    for i in range(cardQuantity):
      self.cards.append(Wild())


  def loadDrawFours(self, cardQuantity):
    for i in range(cardQuantity):
      self.cards.append(DrawFour())


  def loadShuffleHands(self, cardQuantity):
    for i in range(cardQuantity):
      self.cards.append(ShuffleHands())


  def loadSwapHands(self, cardQuantity):
    for i in range(cardQuantity):
      self.cards.append(SwapHands())


  def loadAllPlayersDrawTwo(self, cardQuantity):
    for i in range(cardQuantity):
      self.cards.append(AllPlayersDrawTwo())


  def loadAllPlayersDrawFour(self, cardQuantity):
    for i in range(cardQuantity):
      self.cards.append(AllPlayersDrawFour())


  def loadDiscardAllOfOneColor(self, cardQuantity):
    for i in range(cardQuantity):
      self.cards.append(DiscardAllOfOneColor())


  def shuffleDeck(self):
    random.shuffle(self.cards)


  def reloadDeck(self):
    self.cards.extend(self.discard)
    self.discard = []
    self.shuffleDeck()


  def draw(self):
    if len(self.cards) > 0:
      return self.cards.pop()
    else:
      Logger.info(f"The deck is empty. Shuffling the deck...")
      self.reloadDeck()
      return self.cards.pop()