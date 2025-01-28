from abc import ABC, abstractmethod
import random
from typing import List
from entities.Card import Card
from entities.Hand import Hand
from entities.Deck import Deck
from enums.Card_Color import CardColor
from enums.Card_Number import CardNumber
from utilities.Logger import Logger


class Player(ABC):
  name: str
  hand: Hand
  winCount: int


  def __init__(self, name: str):
    self.name = name
    self.winCount = 0
    self.hand = Hand()
    
    
  def getLegalCards(self, faceColor: CardColor, faceNumber: CardNumber):
    legalCards = []
    for handCard in self.hand.cards:
      if self.isLegalCard(handCard, faceColor, faceNumber):
        legalCards.append(handCard)
    return legalCards


  def isLegalCard(self, someCard: Card, faceColor: CardColor, faceNumber: CardNumber):    
    if someCard.color == faceColor:
      return True
    elif someCard.number == faceNumber:
      return True
    elif someCard.color == CardColor.Black:
      return True
    else:
      return False
  

  def drawAndPlay(self, deck: Deck, faceColor: CardColor, faceNumber: CardNumber):
    newCard = deck.draw()
    Logger.cardDrawn(self.name, newCard)
    if self.isLegalCard(newCard, faceColor, faceNumber):
      return newCard
    else:
      self.hand.cards.append(newCard)
      return None


  def colorWeOwnTheMostOf(self):
    yellow = 0
    green = 0
    red = 0
    blue = 0
    for card in self.hand.cards:
      if card.color == CardColor.Yellow:
        yellow += 1
      elif card.color == CardColor.Green:
        green += 1
      elif card.color == CardColor.Red:
        red += 1
      elif card.color == CardColor.Blue:
        blue += 1
    largest_quantity = max([yellow, green, red, blue])

    colorsWeOwnTheMostOf = []
    if yellow == largest_quantity:
      colorsWeOwnTheMostOf.append(CardColor.Yellow)
    if green == largest_quantity:
      colorsWeOwnTheMostOf.append(CardColor.Green)
    if red == largest_quantity:
      colorsWeOwnTheMostOf.append(CardColor.Red)
    if blue == largest_quantity:
      colorsWeOwnTheMostOf.append(CardColor.Blue)

    return colorsWeOwnTheMostOf


  def getPlayersWithLowestCards(self, players: List['Player']):
    playersWithLowestCards: List[Card] = []
    lowestCardCount = 99

    for player in players:
      cardCount = len(player.hand.cards)
      if cardCount < lowestCardCount:
        lowestCardCount = cardCount
      
    for player in players:
      cardCount = len(player.hand.cards)
      if cardCount == lowestCardCount:
        playersWithLowestCards.append(player)
    
    return playersWithLowestCards



# Override these for player implementations when desired:
  def pickCardToPlay(self, faceColor: CardColor, faceNumber: CardNumber):
    legalCards = self.getLegalCards(faceColor, faceNumber)
    if len(legalCards) > 1:
      randomIndex = random.randint(0, len(legalCards) - 1)
      cardPicked = legalCards[randomIndex]
    elif len(legalCards) == 1:
      cardPicked = legalCards[0]
    else:
      return None

    self.hand.cards.remove(cardPicked)
    return cardPicked

  def pickFaceColor(self):
    colorsWeOwnTheMostOf = self.colorWeOwnTheMostOf()
    randomIndex = random.randint(0, len(colorsWeOwnTheMostOf) - 1)
    return colorsWeOwnTheMostOf[randomIndex]


  def discardAllOfOneColor(self):
    colorsWeOwnTheMostOf = self.colorWeOwnTheMostOf()
    randomIndex = random.randint(0, len(colorsWeOwnTheMostOf) - 1)
    discardColor = colorsWeOwnTheMostOf[randomIndex]
    
    cardsToDiscard = []
    for i, card in enumerate(self.hand.cards):
      if card.color == discardColor:
        cardsToDiscard.append(card)

    for card in cardsToDiscard:
      self.hand.cards.remove(card)

    return cardsToDiscard


  def pickPlayerToSwapWith(self, players: List['Player']) -> 'Player':
    playersWithLowestCards = self.getPlayersWithLowestCards(players)
    playerCount = len(playersWithLowestCards)
    randomIndex = random.randint(0, playerCount - 1)
    return playersWithLowestCards[randomIndex]
