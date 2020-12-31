# Jetpack-Joyride-Terminal-game
A terminal-based python game, made without any inbuilt game-building library, followed OOPS concepts and the game has many cool features like dragon, firing, shield, magnet, gravity , coins, etc


## Running the game

```
    pip3 install -r requirements.txt
    python3 main.py
```


### Coins and Powerups

* There are coins ($) in the game. Collecting one coin increments the score by one.
* There are speed boosts (B) in the game. Collecting them increases the game's speed by a factor of 1.5
* There are Shields (S) in game. It gets activated once a player presses space. The player won't be affected affected by
the enemies and obstacles and shiled lasts for 10
seconds. It will take 60 seconds for shield power-up to refill again after use.

## Controls

* Press 'w' to jump.
* Press 'a' to move left.
* Press 'd' to move right.
* Press 'e' to fire.
* Press 'q' at any time to quit.
* Press ' ' to activate shield(if collected :p)

## Playing the game

* When the game starts, enter your name and press enter.

* Start moving Din using the control keys. 

* Make sure you don't collide with an enemy! If you do, you'll respawn from the top of the screen and lose a life as indicated at the bottom of the screen. 

* Collect powerups to increase number of lives and coins to increase score. Number of lives can at any time be maximum five. 

* At the end of the game, you'll have to destroy the dragon by pressing the spacebar key multiple times.

* After the game ends, your score will be displayed on your terminal.

## Additional features

* Colorama module has been used to generate colors.

