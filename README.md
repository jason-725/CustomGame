# CustomGame Code Documentation

Team: The 12th Men
Team Members:
Nicolas Para
Samuel Mach
Jason Xiong
James Gleadell
Why We Chose Pokemon:
	We chose Pokemon because we wanted to create something that we could be proud of, and not simply something that would pass for the project. Seeing as pokemon is a well known game and seeing as this years projects have best lent their use to the creation of a game such as pokemon it seemed to be an obvious choice.

Game Manual:
Movement – The game uses a similar board to the go-game project, however, in this case players can only move one space per turn on a dramatically decreased board. The movement is also different from go-game as players utilize WASD as input to determine where their player marker moves.

Training – training is how your pokemon gain experience and increase in level. Training takes a player turn and allows them to choose from the pokemon in their inventory to increase their pokemon’s level. Pokemon levels add 10 additional points to health, attack, dodge, and defense per level.

Catching Pokemon – Catching pokemon works by giving a player a random chance of finding a pokemon every time they move to a new space in any biome. The pokemon you can catch are dependent on the biome you are in. When you encounter a pokemon it will be immediately added to your inventory. You can have a max of 3 pokemon.

Combat – When both players occupy the same space they will immediately initiate combat. While in combat players cannot quit or flee from the fight. The game ends when one player is victorious. Combat is broken up into offensive and defensive turns. On offense, the attacker has the option to use a basic attack, as a safe action, or a strike, as a high-risk high-reward action. On defense, the defender chooses between defending, in which case the defender will take reduced damage, or dodging, in which case if the defender is successful they take no damage, but otherwise take full damage. Available to both the attacker and defender are the abilities to check their active pokemon’s stats, use an AP, or switch a pokemon. Using an AP will temporarily increase the active pokemon’s specialty stat which will be either health, damage, dodge, or defense depending on the pokemon’s type (normal, fire, water, earth). Switching pokemon, unlike checking stats and using AP, takes your pokemon’s attack/defense turn! When attacking or defending, your action’s effectiveness is determined by a d20 which is multiplied by your action’s relevant stat to determine how effective you were against your opponent by comparing the product of your action to the product of your opponent’s action. Striking presents a risk-reward situation by rolling two d20s and taking the lower of the two rolls, but if the strike manages to hit, then your pokemon will deal twice as much damage. However, strikes also present an opportunity for the defender as having a higher defensive roll than the attacker’s will result in you taking no damage and dealing some damage to your attacker in the form of a parry. Lastly, due to the pvp being the conclusion of the game, pokemon that faint are removed from the inventory entirely.

Saving and Loading Saves – When launching the game the player will be prompt on whether they want to load the previous save. Loading the save will return players to where they were when the game last saved and will have their pokemon restored to their inventories. Should the players choose a new game, the players’ inventory will be set to nothing and their markers will be placed at their preset positions. When the players quit they will have their game automatically saved as a last action before terminating the program; however, the game will not save the player’s data in the event of the game ending by player victory. This way the players can reload the game again pre-battle and replay, it also means a player will not receive an unfair start by one player starting with last game’s pokemon, while the other receives nothing.

The full bottom-up design diagram of the game can be viewed below:

![image](https://github.com/user-attachments/assets/4d29db8e-7f33-4c17-9335-81bbc9a16e6e)

