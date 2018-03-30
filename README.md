# Python-Game
A 2D python Game using curses

Space Invaders​

is a classic arcade video game created by Tomohiro Nishikado and released in 
1978 - the port of which was also responsible for the massive popularity of gaming consoles in 
the 80s - and hence played a major role in pushing the gaming industry towards mainstream 
media.This is a recreation of this iconic game in 
Python. 
 
Elements of the game:
 
a. Spaceship​ : Denoted by ^. The spaceship can only be moved horizontally on Row number 1. 
That is, it’s movement is restricted from 1x1 to 1x8. Move it using key ‘A’ to move 
left and key ‘D’ to move it to the right. 
b. Aliens​ : Denoted by *, The are randomly 
spawned anywhere in rows 8 and 7. A new alien is spawned every 10 
seconds and each alien lasts for 8 seconds, after which it self destructs. 
 
 
c. Missiles​ : There are two types of missiles: 
i.
Character ‘i’ used to denote a missile. A missile is spawned each time 
the spacebar is clicked and is always spawned in the (row+1, column) 
block if the spaceship is in (row, column) when spacebar is clicked. For 
example, if the spaceship is in (1, 2) when spacebar is hit, the missile 
spawns in (2,2). The missile must move one row up every second. If a 
missile and alien collide, the alien gets destroyed.  
ii.
Character ‘l’ to denote the second form of missile. This missile is 
shot when the ‘S’ key is clicked, and unlike the first kind of bullet, will 
move two rows up every second. If this bullet collides with an alien, the 
alien will exist on the board for another 5 seconds. Also look of alien changes 
when this missile collides with it. 
 
Number of aliens shot down is the score of the player.

