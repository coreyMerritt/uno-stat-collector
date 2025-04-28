# Uno Strategy Simulation Engine

This project is a Python-based Uno game engine built for testing and comparing different player strategies.  
It fully simulates Uno games, handling all rules, card effects, turn orders, and player interactions.

## Overview

At the core of the project is the `Game` class, which manages:

- Game setup, deck creation, and dealing starting hands
- Player turns and full rule enforcement
- Card effects like Draw Two, Draw Four, Reverse, Skip, Swap Hands, and more
- Wild card color picking and special black card logic
- Turn direction (clockwise/counter-clockwise) and draw stacking
- Win detection and tracking over multiple games
- Full deck management (draw pile, discard pile, shuffling)

Other major components include:

- `Deck`: Manages the set of cards, shuffling, drawing, and discarding
- `Card`: Defines each card’s color and number/type
- Specialized `cards/`: Individual files for each special card type (e.g., `Draw_Four`, `Skip`)
- `Player`: Base class for player logic
- `players/`: Collection of sample bots like `aggressive_agatha`, `random_randy`, `tactical_tanner`, etc.
- `Logger`: Centralized logging for gameplay events
- Enums for `CardColor` and `CardNumber` to represent the deck structure
- `stat_collector.py`: For collecting win/loss statistics during large-scale simulations

## Purpose

The main goal of this project is to **simulate Uno games between different player strategies** and evaluate their performance over many games.

You can test strategies like:

- Aggressive playstyles (rapid card dumping)
- Conservative playstyles (hoarding special cards)
- Random decision-making
- Tactical hand management
- Color control strategies

## Getting Started
```
git clone git@github.com:coreyMerritt/uno-stat-collector.git
cd uno-stat-collector/src
pip install colorama
python3 ./stat_collector.py
```

Then, press `enter` at any time to see the current stats.

Press `enter` again to continue playing.

## Features

- Full Uno rule implementation
- Special cards handled: Draw Two, Draw Four, Reverse, Skip, Swap Hands, Wild cards, and more
- Draw stacking supported
- Turn order reversal supported
- Custom player strategies easily defined and tested
- Win tracking over repeated simulations
- Designed for scalability (fast simulation of thousands of games)

## Requirements

- Python 3.7+
- Colorama (Installation covered in [Getting Started](#getting-started))

## Notes

- New player strategies can be added by subclassing `Player` and implementing custom decision-making.

## License

This project is licensed under the [MIT License](LICENSE).

