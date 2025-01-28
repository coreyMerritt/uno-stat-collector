#!/usr/bin/env python3

import sys
import threading
import time
from typing import List
from utilities.Logger import Logger
from utilities.Stopwatch import Stopwatch
from entities.Player import Player
from entities.Game import Game
from entities.players.aggressive_agatha import AggressiveAgatha
from entities.players.colorful_colin import ColorfulColin
from entities.players.minimal_mindy import MinimalMindy
from entities.players.random_randy import RandomRandy



class StatCollector():
  players: List[Player]
  play: bool
  draws: int
  games_to_play: int
  stopwatch: Stopwatch
  

  @staticmethod
  def start():
    StatCollector.draws = 0
    StatCollector.players = []

    StatCollector.determineNumOfGamesToPlay()
    StatCollector.startPauseGameListener()
    StatCollector.loadPlayers()

    game = Game(StatCollector.players)
    StatCollector.play = True

    while True:
      if StatCollector.getTotalGamesPlayed() < StatCollector.games_to_play:
        if StatCollector.play:
          StatCollector.playNextRound(game)
      else:
        StatCollector.outputResults()
        exit(0)



  @staticmethod
  def determineNumOfGamesToPlay():
    if len(sys.argv) > 1:
      StatCollector.games_to_play = int(sys.argv[1])
    else:
      StatCollector.games_to_play = 1000000000



  @staticmethod
  def startPauseGameListener():
    listener_thread = threading.Thread(target=StatCollector.pauseGameListener, daemon=True)
    listener_thread.start()


  
  @staticmethod
  def pauseGameListener():
    StatCollector.stopwatch = Stopwatch()
    StatCollector.stopwatch.start()
    while True:
      input()
      if StatCollector.play == True:
        StatCollector.play = False
        StatCollector.stopwatch.pause()
        time.sleep(0.1)
        StatCollector.outputResults()
      else:
        StatCollector.play = True
        StatCollector.stopwatch.start()


  @staticmethod
  def loadPlayers():
    players = []
    randomRandyCount = 1
    colorfulColinCount = 1
    minimalMindyCount = 1
    AggressiveAgathaCount = 1

    for i in range(randomRandyCount):
      players.append(RandomRandy(f"Randy_{i + 1}"))
    
    for i in range(colorfulColinCount):
      players.append(ColorfulColin(f"Colin_{i + 1}"))
    
    for i in range(minimalMindyCount):
      players.append(MinimalMindy(f"Mindy_{i + 1}"))
    
    for i in range(AggressiveAgathaCount):
      players.append(AggressiveAgatha(f"Agatha_{i + 1}"))
    
    StatCollector.players = players
  

  @staticmethod
  def outputResults():
    total = StatCollector.getTotalGamesPlayed()

    Logger.info(f"\n\nTotal Games Played: {total:<{0},}")
    for player in StatCollector.players:
      Logger.info(f"\t{player.name:<{19}} {player.winCount:<{15},} [{round((player.winCount / total) * 100, 2):<{5}}%]")
    Logger.info(f"\t{'Draw count':<{19}} {StatCollector.draws:<{15},} [{round((StatCollector.draws / total) * 100, 2):<{5}}%]")

    time = StatCollector.stopwatch.getTimeAsString()
    Logger.info(f"\nElapsed Time: {time}")

    gamesPerSecond = StatCollector.stopwatch.getGamesPerSecond(total)
    Logger.info(f"Games per second: {gamesPerSecond}")


  @staticmethod
  def getTotalGamesPlayed():
    total = 0
    for player in StatCollector.players:
      total += player.winCount
    total += StatCollector.draws
    return total
  


  def playNextRound(game: Game):
    try:
      Logger.info(f"Game #: {StatCollector.getTotalGamesPlayed() + 1}")
      game.startNewGame(2)
    except IndexError as e:
      StatCollector.draws += 1



StatCollector.start()
