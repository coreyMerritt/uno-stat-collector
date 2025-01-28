import random
import time
from typing import List

from entities.Deck import Deck
from entities.Card import Card
from entities.Player import Player
from entities.players.colorful_colin import ColorfulColin
from entities.players.random_randy import RandomRandy
from enums.Card_Color import CardColor
from enums.Card_Number import CardNumber


class Game:
  deck: Deck
  players: List[Player]
  activeDealer: Player
  activePlayer: Player
  faceCard: Card
  faceColor: CardColor
  faceNumber: CardNumber
  turnOrderClockwise: bool



  def __init__(self, players: List[Player]):
    self.players = players



  def loadDeck(self, deckCount):
    self.deck = Deck(deckCount)


  def startNewGame(self, deckCount: int):
    self.loadDeck(deckCount)
    self.turnOrderClockwise = True
    self.determineActiveDealer()
    self.determineActivePlayer()
    self.dealStartingHands()
    self.drawInitialFacecard()
    self.playUntilWinner()


  def drawInitialFacecard(self):
    card = self.deck.draw()
    print(f"\tThe face card is a {card.color.value} {card.number.value}!")
    self.playCard(card, True)
    self.setNextActivePlayer()


  def determineActiveDealer(self):
    if not hasattr(self, 'activeDealer') or self.activeDealer is None:
      activeDealer = self.players[0]
    else:
      activeDealer = self.getNextPlayerClockwise(self.activeDealer)

    print(f"\t{activeDealer.name} is the dealer.")
    self.activeDealer = activeDealer


  def determineActivePlayer(self):
    self.activePlayer = self.activeDealer


  def dealStartingHands(self):
    cardsToDeal: List[Card] = []
    for i in range(7 * len(self.players)):
      card = self.deck.draw()
      cardsToDeal.append(card)
    self.dealHands(cardsToDeal)


  def dealHands(self, cardsToDeal):
    peopleInGame = len(self.players)
    i = self.players.index(self.activePlayer)
    for card in cardsToDeal:
      if self.turnOrderClockwise:
        i += 1
        if i == peopleInGame:
          i = 0
      else:
        i -= 1
        if i == -1:
          i = peopleInGame - 1
      nextPlayer = self.players[i]
      nextPlayer.hand.cards.append(card)
      print(f"\t\t{nextPlayer.name} was dealt a {card.color.value} {card.number.value}")


  def playUntilWinner(self):
    while not self.isWinner():
      self.takeTurn()
    if self.isWinner():
      self.declareWinner()


  def takeTurn(self):
    cardBeingPlayed = self.determineCardBeingPlayed()
    self.playCard(cardBeingPlayed)
    self.setNextActivePlayer()


  def determineCardBeingPlayed(self):
    cardBeingPlayed = self.activePlayer.pickCardToPlay(self.faceColor, self.faceNumber)
    while cardBeingPlayed is None:
      cardBeingPlayed = self.activePlayer.drawAndPlay(self.deck, self.faceColor, self.faceNumber)
    return cardBeingPlayed


  def playCard(self, card: Card, system=False):
    if not system:
      player = self.activePlayer
      print(f"\t{player.name} played a {card.color.value} {card.number.value}")
    else:
      player = self.activeDealer
    
    if card.color != CardColor.Black:
      self.executeEffect(card.number, player)
      self.setFacecard(card, card.color, card.number)
    else:
      self.executeEffect(card.number, player)
      color = player.pickFaceColor()
      print(f"\t{player.name} chose {color.value}!")
      self.setFacecard(card, color, card.number)

    

  def executeEffect(self, cardNumber: CardNumber, owner: Player):
    match (cardNumber):
      case CardNumber.AllPlayersDrawFour:
        self.allPlayersDrawFour()
      case CardNumber.AllPlayersDrawTwo:
        self.allPlayersDrawTwo()
      case CardNumber.DiscardAllOfOneColor:
        self.discardAllOfOneColor()
      case CardNumber.DrawFour:
        self.drawFour()
      case CardNumber.DrawTwo:
        self.drawTwo()
      case CardNumber.Reverse:
        self.reverse()
      case CardNumber.ShuffleHands:
        self.shuffleHands()
      case CardNumber.Skip:
        self.skip()
      case CardNumber.SwapHands:
        self.swapHands()



# Black card effects
    
  def allPlayersDrawFour(self):
    for player in self.players:
      if player != self.activePlayer:
        for i in range(4):
          card = self.deck.draw()
          print(f"\t\t{player.name} drew a {card.color.value} {card.number.value}")
          player.hand.cards.append(card)


  def allPlayersDrawTwo(self):
    for player in self.players:
      if player != self.activePlayer:
        for i in range(2):
          card = self.deck.draw()
          print(f"\t\t{player.name} drew a {card.color.value} {card.number.value}")
          player.hand.cards.append(card)
  

  def discardAllOfOneColor(self):
    cardsToDiscard = self.activePlayer.discardAllOfOneColor()
    for card in cardsToDiscard:
      print(f"\t\t{self.activePlayer.name} discards a {card.color.value} {card.number.value}")
      self.deck.discard.append(card)


  def drawFour(self):
    for i in range(4):
      card = self.deck.draw()
      player = self.getNextPlayer()
      player.hand.cards.append(card)
      print(f"\t\t{player.name} drew a {card.color.value} {card.number.value}")


  def drawTwo(self):
    for i in range(2):
      card = self.deck.draw()
      player = self.getNextPlayer()
      player.hand.cards.append(card)
      print(f"\t\t{player.name} drew a {card.color.value} {card.number.value}")


  def reverse(self):
    if self.turnOrderClockwise:
      self.turnOrderClockwise = False
    else:
      self.turnOrderClockwise = True


  def shuffleHands(self):
    cardsInAllHands: List[Card] = []
    for player in self.players:
      cardsInAllHands.extend(player.hand.cards)
      player.hand.cards.clear()

    random.shuffle(cardsInAllHands)
    self.dealHands(cardsInAllHands)
    

  def skip(self):
    self.activePlayer = self.getNextPlayer()
    print(f"\t\t{self.activePlayer.name} is skipped!")


  def swapHands(self):
    playersExceptMe: List[Player] = []
    for player in self.players:
      if player != self.activePlayer:
        playersExceptMe.append(player)

    playerToSwapWith = self.activePlayer.pickPlayerToSwapWith(playersExceptMe)
    
    temp_hand = self.activePlayer.hand
    self.activePlayer.hand = playerToSwapWith.hand
    playerToSwapWith.hand = temp_hand
    print(f"\t\t{self.activePlayer.name} swapped hands with {playerToSwapWith.name}!")



### Misc / Helpers

  def setNextActivePlayer(self):
    if self.turnOrderClockwise:
      for i, player in enumerate(self.players):
        if player == self.activePlayer:
          if self.isFinalPlayer(player):
            self.activePlayer = self.players[0]
          else:
            self.activePlayer = self.players[i + 1]
          break
    else:
      for i, player in enumerate(self.players):
        if player == self.activePlayer:
          if self.isFirstPlayer(player):
            self.activePlayer = self.players[len(self.players) - 1]
          else:
            self.activePlayer = self.players[i - 1]
          break



  def isFirstPlayer(self, player):
    for i, p in enumerate(self.players):
      if player == p:
        if (i == 0):
          return True
        else:
          return False


  def isFinalPlayer(self, player):
    for i, p in enumerate(self.players):
      if player == p:
        if (i == (len(self.players) - 1)):
          return True
        else:
          return False

  
  def setFacecard(self, faceCard: Card, faceColor: CardColor, faceNumber: CardNumber):
    if hasattr(self, 'faceCard') and self.faceCard is not None:
      self.deck.discard.append(self.faceCard)
    self.faceCard = faceCard
    self.faceColor = faceColor
    self.faceNumber = faceNumber


  def isWinner(self):
    for player in self.players:
      if len(player.hand.cards) == 0:
        return True
    return False


  def declareWinner(self):
    for i, player in enumerate(self.players):
      if len(player.hand.cards) == 0:
        winningPlayer = player
    
    if winningPlayer:
      print(f"{winningPlayer.name} wins!")
      i = self.players.index(winningPlayer) 
      self.players[i].winCount += 1
      print(f"{winningPlayer.name} win count: {player.winCount:<{0},}")
      

      self.addHandsToDeck()
      self.deck.reloadDeck()
        

  
  def addHandsToDeck(self):
    for player in self.players:
      self.deck.discard.extend(player.hand.cards)
      player.hand.cards = []


  def getNextPlayer(self, givenPlayer=False) -> Player:
    if not givenPlayer:
      givenPlayer = self.activePlayer

    for i, player in enumerate(self.players):
      if player == givenPlayer:
        if self.turnOrderClockwise:
          if self.isFinalPlayer(player):
            return self.players[0]
          else:
            return self.players[i + 1]
        else:
          if self.isFirstPlayer(player):
            return self.players[len(self.players) - 1]
          else:
            return self.players[i - 1]


  def getNextPlayerClockwise(self, givenPlayer=False) -> Player:
    if not givenPlayer:
      givenPlayer = self.activePlayer

    for i, player in enumerate(self.players):
      if player == givenPlayer:
        if self.isFinalPlayer(player):
          return self.players[0]
        else:
          return self.players[i + 1]
