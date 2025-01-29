from colorama import Fore
from colorama import Back
from colorama import init

from entities.Card import Card
from enums.Card_Color import CardColor
from enums.Card_Number import CardNumber

init(autoreset=True)



class Logger:

  tab_size = 6


##### Start Public Methods #####

  @staticmethod
  def info(message: str):
    print(message)



  @staticmethod
  def gameChangingEvent(message: str):
    print(Fore.MAGENTA + message)

  

  @staticmethod
  def dealerAssigned(playerName: str):
    indent = " " * Logger.tab_size
    print(indent + Fore.BLUE + playerName + " is the dealer.")



  @staticmethod
  def colorPicked(playerName: str, color: CardColor):
    indent = " " * Logger.tab_size * 2
    foreColor = Logger._getForeColor(color)
    backColor = Logger._getBackColor(color)
    color = backColor + foreColor + color.value
    print(indent + f"{playerName} chooses: {color}")



  @staticmethod
  def cardPlayed(playerName: str, card: Card):
    indent = " " * Logger.tab_size
    foreColor = Logger._getForeColor(card.color)
    backColor = Logger._getBackColor(card.color)
    cardNum = backColor + foreColor + str(card.number.value)
    print(indent + f"{playerName} plays: {cardNum}")



  @staticmethod
  def cardDealt(playerName: str, card: Card):
    indent = " " * Logger.tab_size * 2
    foreColor = Logger._getForeColor(card.color)
    backColor = Logger._getBackColor(card.color)
    cardNum = backColor + foreColor + str(card.number.value)
    print(indent + f"{playerName} is dealt: {cardNum}")
  


  @staticmethod  
  def cardDrawn(playerName: str, card: Card):
    indent = " " * Logger.tab_size * 2
    foreColor = Logger._getForeColor(card.color)
    backColor = Logger._getBackColor(card.color)
    cardNum = backColor + foreColor + str(card.number.value)
    print(indent + f"{playerName} draws: {cardNum}")



  @staticmethod
  def faceCardPlayed(card: Card):
    indent = " " * Logger.tab_size
    foreColor = Logger._getForeColor(card.color)
    backColor = Logger._getBackColor(card.color)
    cardNum = backColor + foreColor + str(card.number.value)
    print(indent + f"The face card is: {cardNum}")



  @staticmethod
  def cardDiscarded(playerName: str, card: Card):
    indent = " " * Logger.tab_size * 2
    foreColor = Logger._getForeColor(card.color)
    backColor = Logger._getBackColor(card.color)
    cardNum = backColor + foreColor + str(card.number.value)
    print(indent + f"{playerName} discards: {cardNum}")  



  @staticmethod
  def playerSkipped(playerName: str):
    indent = " " * Logger.tab_size * 2
    print(indent + f"{playerName} is skipped.")



  @staticmethod
  def handsSwapped(playerOne: str, playerTwo: str):
    indent = " " * Logger.tab_size * 2
    print(indent + f"{playerOne} swaps hands with: {playerTwo}")


##### Start Private Methods ######
  
  @staticmethod
  def _getForeColor(cardColor: CardColor):
    match (cardColor):
      case CardColor.Yellow:
        return Fore.YELLOW
      case CardColor.Green:
        return Fore.GREEN
      case CardColor.Red:
        return Fore.RED
      case CardColor.Blue:
        return Fore.BLUE
      case CardColor.Black:
        return Fore.BLACK
      

  
  @staticmethod
  def _getBackColor(cardColor: CardColor):
    match (cardColor):
      case CardColor.Yellow:
        return Back.BLACK
      case CardColor.Green:
        return Back.BLACK
      case CardColor.Red:
        return Back.BLACK
      case CardColor.Blue:
        return Back.BLACK
      case CardColor.Black:
        return Back.WHITE
