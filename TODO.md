List of things to do / change
-
- decide on what the game/story will be
- then learn how to use github and then we're good to do commits on our own branch and merge requests when ready

Battle:
- add agaility to play a role in Dodging
- fix calculations for dmg and def

#Note: I've added a save() function in basics.py. Not sure if I should just dump the data directly in the function or not... (specifically on line 40 in main.py) - Jacob

Stats :
-
- Stats are too flat; there should be a slightly greater difference between `Level 1 to Level 2` and `Level 7 and level 8`so it somehow grows exponentially
- fix EVERYTHING all the stats are broken and have too much impact.
- Damage should be a flat amount plus a small multiplier like each level adds 2 damage + 10%
- Defence should be a flat reduction like 1 per level + a tiny percentage (right now if you're defence level 10 you're literally invincible wtf) make it like 50% reduction at level 10 or something
- Smart moves is not RNG enough (if someone's got one extra point of intelligence they always win?). Do something like constantly having a chance of doing smart moves but int makes it more likely to happen
  - Also find something to do with intelligence for the player as for now it's useless (having more intelligence than your opponent shouldn't make it less likely for them to do something smart so find something else)
- Charisma is completely useless for now either find an actual use (only using it for surrendering is not useful enough for it to be a stat) to it or maybe change the name of the stat to luck or whatever
  - Same issue here, it shouldn't be that if the enemy has more charisma yours is worthless
- I literally forgot agility was a thing because we didn't give it a use yet but here are some ideas
  - Dodging
  - Turn priority (I never saw an RPG in which there could be ties it's usually either player prio or with stats like I presented here)

Misc
-
- Make it impossible to reach chapters without having unlocked them first (of course keep the debug for now)
- Update algorithm (see stats markdown)
- Move battle() and all subsequent battle related functions to battly.py
- Implement levels

Notes:
-
- was thinking that in chapter one the fights could be Les Boyeez TM fighting the paintings in the art project (ali)
- I took the liberty to add a bunch of things and organise your ideas as well in this file (ADIBOS)