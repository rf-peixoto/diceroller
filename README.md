# DiceRoller
DiceRoller is a command-line dice roll utility aimed at tabletop RPGs.
It's pretty simple. start the program with ```python diceroller.py```
Confirm the session open by entering ```y``` and enter your character name. You will see the data entry screen.

The structure of the commands is as follows: ```[amount of dices]d[value of the dice]```. Ex: 1d20, 2d6, 3d4, 1d100...
If you end your command with an ```h```, the roll will be considered a half roll. This way, the minimum value of each dice will be half of its total value. Ex:

```1d8``` will have a minimum result of 4. On ```3d6```, the minimum result for each dice will be 3.

### TODO
I. Validate inputs. If you try to use dices with a value of 0 or negative, it will cause an error.

II. Include math operations on rolls. (Add and subtract only.)
