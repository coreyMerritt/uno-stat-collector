from typing import List
from entities.Card import Card
from entities.Game import Game
from entities.Player import Player
from enums.Card_Number import CardNumber


### 005 - Tactical Tanner is the first player who assesses
### other player's hand sizes to determine if he should "attack."


class TacticalTanner(Player):

  def pickCardToPlay(self, game: Game):
    legalCards = self.getLegalCards(game.faceColor, game.faceNumber)
    if len(legalCards) > 1:
      cardPicked = self.determineCard(legalCards, game)
    elif len(legalCards) == 1:
      cardPicked = legalCards[0]
    else:
      return None

    return cardPicked



  def determineCard(self, legalCards: List[Card], game: Game):
    playersWithTwoCards = []
    for player in game.players:
      if len(player.hand.cards) <= 2:
        playersWithTwoCards.append(player)
    
    if len(playersWithTwoCards) > 1:
      if len(game.getNextPlayer().hand.cards) <= 2:
        priority = self.multiplePeopleWithTwoCards(legalCards, True)
      else:
        priority = self.multiplePeopleWithTwoCards(legalCards, False)
      card = self.getCardFromPriorityList(legalCards, priority)
      return card
    
    elif len(playersWithTwoCards) == 1:
      if len(game.getNextPlayer().hand.cards) <= 2:
        priority = self.onePersonWithTwoCards(legalCards, True)
      else:
        priority = self.onePersonWithTwoCards(legalCards, False)
      card = self.getCardFromPriorityList(legalCards, priority)
      return card

    else:
      card = self.minFirstCardPriority(legalCards)
      return card   



  def multiplePeopleWithTwoCards(self, legalCards: List[Card], nextPlayerHasOneCard: bool):
    if nextPlayerHasOneCard:
      priority = [
        CardNumber.AllPlayersDrawFour,
        CardNumber.AllPlayersDrawTwo,
        CardNumber.SwapHands,
        CardNumber.ShuffleHands,
        CardNumber.DrawTwo,
        CardNumber.DrawFour,
        CardNumber.Skip,
        CardNumber.Reverse,
        CardNumber.Wild,
        "number",
        CardNumber.DiscardAllOfOneColor,
      ]

    else:
      priority = [
        CardNumber.AllPlayersDrawFour,
        CardNumber.AllPlayersDrawTwo,
        CardNumber.SwapHands,
        CardNumber.ShuffleHands,
        "number",
        CardNumber.Reverse,
        CardNumber.Skip,
        CardNumber.DrawTwo,
        CardNumber.Wild,
        CardNumber.DiscardAllOfOneColor,
        CardNumber.DrawFour
      ]

    return priority
    


  def onePersonWithTwoCards(self, legalCards: List[Card], nextPlayerHasTwoCards: bool):
    if nextPlayerHasTwoCards:
      priority = [
        CardNumber.DrawTwo,
        CardNumber.DrawFour,
        CardNumber.Skip,
        CardNumber.Reverse,
        CardNumber.AllPlayersDrawTwo,
        CardNumber.AllPlayersDrawFour,
        CardNumber.SwapHands,
        CardNumber.ShuffleHands,
        "number",
        CardNumber.Wild,
        CardNumber.DiscardAllOfOneColor,
      ]

    else:
      priority = [
        CardNumber.AllPlayersDrawTwo,
        CardNumber.AllPlayersDrawFour,
        CardNumber.SwapHands,
        CardNumber.ShuffleHands,
        "number",
        CardNumber.Reverse,
        CardNumber.Skip,
        CardNumber.DrawTwo,
        CardNumber.Wild,
        CardNumber.DiscardAllOfOneColor,
        CardNumber.DrawFour
      ]

    return priority
