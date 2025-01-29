from dataclasses import dataclass
from datetime import datetime, timedelta
import math



class Stopwatch:
  def __init__(self):
    self.start_time = None
    self.total_time = timedelta(0)
    self.running = False


  def start(self):
    if not self.running:
      self.start_time = datetime.now()
      self.running = True


  def pause(self):
    if self.running:
      self.total_time += (datetime.now() - self.start_time)
      self.start_time = None
      self.running = False


  def reset(self):
    self.start_time = None
    self.total_time = timedelta(0)
    self.running = False


  def getRawTime(self):
    if self.running:
      return self.total_time + (datetime.now() - self.start_time)
    else:
      return self.total_time

  
  def getCleanTime(self):
    
    @dataclass
    class cleanTime:
      days: int
      hours: int
      minutes: int
      seconds: int
      miliseconds: int

    time = self.getRawTime()
    cleanTime.days = time.days
    cleanTime.hours = math.floor(time.seconds / 3600)
    cleanTime.minutes = math.floor(time.seconds / 60) % 60
    cleanTime.seconds = math.floor(time.seconds % 60)
    cleanTime.miliseconds = int(time.microseconds / 1000)

    return cleanTime


  def getTimeAsString(self):
    time = self.getCleanTime()
    return f"{time.days}d {time.hours}h {time.minutes}m {time.seconds}.{time.miliseconds}s"


  def getGamesPerSecond(self, gameCount):
    time = self.getRawTime()
    days = time.days
    seconds = time.seconds
    miliseconds = time.microseconds / 1000
    if days != 0:
      seconds += (86400 * days)
    seconds += miliseconds / 1000
    gamesPerSecond = round((gameCount / seconds), 2)
    return gamesPerSecond