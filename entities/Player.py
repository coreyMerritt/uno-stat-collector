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
    self.hand.cards.append(newCard)
    Logger.cardDrawn(self.name, newCard)

    if self.isLegalCard(newCard, faceColor, faceNumber):
      return newCard
    else:
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



  def minFirstCardPriority(self, legalCards: List[Card]):
    priority = [
      "number", 
      CardNumber.Reverse, 
      CardNumber.Skip,
      CardNumber.DrawTwo,
      CardNumber.Wild,
      CardNumber.AllPlayersDrawTwo,
      CardNumber.AllPlayersDrawFour,
      CardNumber.DiscardAllOfOneColor,
      CardNumber.DrawFour,
      CardNumber.ShuffleHands,
      CardNumber.SwapHands
      ]
    return self.getCardFromPriorityList(legalCards, priority)


  
  def getCardFromPriorityList(self, legalCards: List[Card], priority):
    for pri in priority:
      match pri:
        case CardNumber.Reverse:
          for card in legalCards:
            if card.number == CardNumber.Reverse:
              return card
            
        case CardNumber.Skip:
          for card in legalCards:
            if card.number == CardNumber.Skip:
              return card
            
        case CardNumber.DrawTwo:
          for card in legalCards:
            if card.number == CardNumber.DrawTwo:
              return card
            
        case CardNumber.Wild:
          for card in legalCards:
            if card.number == CardNumber.Wild:
              return card
            
        case CardNumber.AllPlayersDrawTwo:
          for card in legalCards:
            if card.number == CardNumber.AllPlayersDrawTwo:
              return card
            
        case CardNumber.AllPlayersDrawFour:
          for card in legalCards:
            if card.number == CardNumber.AllPlayersDrawFour:
              return card
            
        case CardNumber.DiscardAllOfOneColor:
          for card in legalCards:
            if card.number == CardNumber.DiscardAllOfOneColor:
              return card
            
        case CardNumber.DrawFour:
          for card in legalCards:
            if card.number == CardNumber.DrawFour:
              return card
        
        case CardNumber.ShuffleHands:
          for card in legalCards:
            if card.number == CardNumber.ShuffleHands:
              return card
        
        case CardNumber.SwapHands:
          for card in legalCards:
            if card.number == CardNumber.SwapHands:
              return card
            
        case _:
          for card in legalCards:
            if card.color != CardColor.Black:
              if card.number != CardNumber.DrawTwo:
                if card.number != CardNumber.Skip:
                  if card.number != CardNumber.Reverse:
                    return card



  def maxFirstCardPriority(self, legalCards: List[Card]):
    priority = [
      CardNumber.SwapHands,
      CardNumber.ShuffleHands,
      CardNumber.DrawFour,
      CardNumber.DiscardAllOfOneColor,
      CardNumber.AllPlayersDrawFour,
      CardNumber.AllPlayersDrawTwo,
      CardNumber.Wild,
      CardNumber.DrawTwo,
      CardNumber.Skip,
      CardNumber.Reverse,
      "number"
    ]
    return self.getCardFromPriorityList(legalCards, priority)
            


  def playDrawTwoIfAvailable(self):
    for card in self.hand.cards:
      if card.number == CardNumber.DrawTwo:
        return card
    return None



  def playDrawFourIfAvailable(self):
    for card in self.hand.cards:
      if card.number == CardNumber.DrawFour:
        return card
    return None



  def removeCardFromHand(self, card: Card):
    for handCard in self.hand.cards:
      if handCard.color == card.color:
        if handCard.number == card.number:
          self.hand.cards.remove(handCard)



# Override these for player implementations when desired:
  def pickCardToPlay(self, game):
    legalCards = self.getLegalCards(game.faceColor, game.faceNumber)
    if len(legalCards) > 1:
      randomIndex = random.randint(0, len(legalCards) - 1)
      cardPicked = legalCards[randomIndex]
    elif len(legalCards) == 1:
      cardPicked = legalCards[0]
    else:
      return None

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
    for card in self.hand.cards:
      if card.color == discardColor:
        cardsToDiscard.append(card)

    return cardsToDiscard



  def pickPlayerToSwapWith(self, players: List['Player']) -> 'Player':
    playersWithLowestCards = self.getPlayersWithLowestCards(players)
    playerCount = len(playersWithLowestCards)
    randomIndex = random.randint(0, playerCount - 1)
    return playersWithLowestCards[randomIndex]
