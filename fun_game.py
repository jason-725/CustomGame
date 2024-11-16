
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Nicolas Parra
# Samuel Mach
# Jason Xiong
# James Gleadell
# Section: 204
# Assignment: Week 13 Team Lab - Custom Pokemon Assignment
# Date: 4 11 2024

from game_classes import Pokemon, Player
import random

#Welcome Message
print("Welcome to the Pokemon Game!")

# Loading saved data
playerOneProfile = []
playerTwoProfile = []
while True:
    choice = input("Load previous game? (Y/N)\n").strip().upper()
    if choice == 'Y':
        # playerOneData assigned first part of file_data
        # playerTwoData assigned sec
        with open("player_data.txt", "r") as datFile:
            file_data = datFile.read().split('---\n')
            playerOneData = file_data[0].split('\n')
            playerTwoData = file_data[1].split('\n')
            
            # splits each line of playerData into lists
            for i in range(len(playerTwoData)):
                playerOneData[i] = playerOneData[i].strip().split('  ')
                playerTwoData[i] = playerTwoData[i].strip().split('  ')
                
            playerOneData = playerOneData[:-1]
            playerTwoData = playerTwoData[:-1]
        playerOneLevels = []
        playerTwoLevels = []
        for i in range(len(playerOneData)):
            dataSet = []
            for j in range(len(playerOneData[i])):
                # writes list into dataSet temp variable before appending to player profiles
                dataSet.append(playerOneData[i][j])
            playerOneProfile.append(dataSet[:])
        for i in range(len(playerTwoData)):
            dataSet = []
            for j in range(len(playerTwoData[i])):
                dataSet.append(playerTwoData[i][j])
            playerTwoProfile.append(dataSet[:])
        for i in range(len(playerOneProfile[1])):
            playerOneLevels.append(playerOneProfile[1][i][-1:])
            playerOneProfile[1][i] = playerOneProfile[1][i][:-1]
        for i in range(len(playerTwoProfile[1])):
            playerTwoLevels.append(playerTwoProfile[1][i][-1:])
            playerTwoProfile[1][i] = playerTwoProfile[1][i][:-1]
        playerOneProfile.append(playerOneLevels)
        playerTwoProfile.append(playerTwoLevels)
        break
    elif choice ==  'N':
        populated_playerA_inv = []
        populated_playerB_inv = []
        playerOneProfile = [['A'], populated_playerA_inv, ['.'], [5, 9]]
        playerTwoProfile = [['B'], populated_playerB_inv, ['.'], [9, 5]]
        break
poke_roster = ['MOUSE', 'HAWK', 'WOLF', 'BEAR', 'EMBER', 'FLAME DWELLER', 'DRAGON', 'PHOENIX', 'CLAM', 'SWORDFISH', 'NESSIE', 'MEGALODON', 'SPROUT', 'POISON IVY', 'GIANT SEQUOIA', 'BIGFOOT', 'FRODO SPEARS']

#Creating 4 normal pokemon, normal pokemon generally specialize in HEALTH
pk_mouse = Pokemon("MOUSE", "NORMAL", 30, 10, 15, 0, 1, "*", 4)
pk_hawk = Pokemon("HAWK", "NORMAL", 50, 25, 20, 0, 1, "*", 4)
pk_wolf = Pokemon("WOLF", "NORMAL", 90, 30, 20, 10, 1, "*", 4)
pk_bear = Pokemon("BEAR", "NORMAL", 150, 40, 10, 30, 1, "*", 4)

#Creating 4 fire pokemon, fire pokemon generally specialize in DAMAGE
pk_ember = Pokemon("EMBER", "FIRE", 15, 25, 5, 0, 1, "&", 4)
pk_fire_dweller = Pokemon("FLAME DWELLER", "FIRE", 30, 30, 0, 15, 1, "&", 4)
pk_dragon = Pokemon("DRAGON", "FIRE", 60, 45, 15, 10, 1, "&", 4)
pk_phoenix = Pokemon("PHOENIX", "FIRE", 75, 65, 10, 15, 2, "&", 4)

#Creating 4 water pokemon, water pokemon generally specialize in DODGE
pk_clam = Pokemon("CLAM", "WATER", 25, 10, 30, 15, 1, "~", 4)
pk_swordfish = Pokemon("SWORDFISH", "WATER", 45, 25, 35, 0, 1, "~", 4)
pk_nessie = Pokemon("NESSIE", "WATER", 75, 30, 40, 10, 1, "~", 4)
pk_megalodon = Pokemon("MEGALODON", "WATER", 100, 45, 45, 20, 1, "~", 4)

#Creating 4 earth pokemon, earth pokemon generally specialize in DEFENSE
pk_sprout = Pokemon("SPROUT", "EARTH", 20, 5, 0, 30, 1, "^", 4)
pk_poison_ivy = Pokemon("POISON IVY", "EARTH", 40, 30, 0, 35, 1, "^", 4)
pk_giant_sequoia = Pokemon("GIANT SEQUOIA", "EARTH", 45, 25, 0, 45, 1, "^", 4)
pk_bigfoot = Pokemon("BIGFOOT", "EARTH", 100, 35, 0, 60, 1, "^", 4)

#Creating THE legendary pokemon
pk_frodo = Pokemon("FRODO SPEARS", "LEGENDARY", 200, 100, 0, 0, 1, ".", 4)

#create a list of the pokemon object to sort through
list_of_pokemon_types = [pk_mouse, pk_hawk, pk_wolf, pk_bear, 
                         pk_ember, pk_fire_dweller, pk_dragon, pk_phoenix, 
                         pk_clam, pk_swordfish, pk_nessie, pk_megalodon, 
                         pk_sprout, pk_poison_ivy, pk_giant_sequoia, pk_bigfoot, 
                         pk_frodo]


# test = ["MOUSE", "NESSIE"]
#Delcare the array that the player's inventory that pokemon will be adding into
populated_playerA_inv = []
#playerOneProfile is the saved list of pokemon names in previous safe file
#Go through the list and find the pokemon previously caught
for name in playerOneProfile[1]:
    for pokemon in list_of_pokemon_types:
        if pokemon.getName() == name:
            #Add the found pokemon to the array
            populated_playerA_inv.append(pokemon)
            
#Delcare the array that the player's inventory that pokemon will be adding into            
# test = ["SPROUT", "MEGALODON"]
populated_playerB_inv = []
#playerTwoProfile is the saved list of pokemon names in previous safe file
#Go through the list and find the pokemon previously caught
for name in playerTwoProfile[1]:
    for pokemon in list_of_pokemon_types:
        if pokemon.getName() == name:
            #Add the found pokemon to the array
            populated_playerB_inv.append(pokemon)

#Creating two player objects
playerA = Player(playerOneProfile[0][0], int(playerOneProfile[3][0]), int(playerOneProfile[3][1]), populated_playerA_inv, playerOneProfile[2][0])
playerB = Player(playerTwoProfile[0][0], int(playerTwoProfile[3][0]), int(playerTwoProfile[3][1]), populated_playerB_inv, playerOneProfile[2][0])

#Testing player movement
# print(playerA.getName(), playerA.getX(), playerA.getY(), playerA.getInventory())
# playerA.moveRight()
# print(playerA.getX())

# # #Sample training 
# print(pk_mouse.getName())
# print(pk_mouse.getDamage())
# pk_mouse.train()
# print(pk_mouse.getDamage())

#           Map
#           earth
#    water  center  fire
#           city

#Creation of the board
board = [[" ", " ", " ", " ", " ", "^", "^", "^", "^", "^", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", "^", "^", "^", "^", "^", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", "^", "^", "^", "^", "^", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", "^", "^", "^", "^", "^", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", "^", "^", "^", "^", "^", " ", " ", " ", " ", " "],
         ["~", "~", "~", "~", "~", ".", ".", ".", ".", ".", "&", "&", "&", "&", "&"],
         ["~", "~", "~", "~", "~", ".", ".", ".", ".", ".", "&", "&", "&", "&", "&"],
         ["~", "~", "~", "~", "~", ".", ".", ".", ".", ".", "&", "&", "&", "&", "&"],
         ["~", "~", "~", "~", "~", ".", ".", ".", ".", ".", "&", "&", "&", "&", "&"],
         ["~", "~", "~", "~", "~", ".", ".", ".", ".", ".", "&", "&", "&", "&", "&"],
         [" ", " ", " ", " ", " ", "*", "*", "*", "*", "*", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", "*", "*", "*", "*", "*", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", "*", "*", "*", "*", "*", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", "*", "*", "*", "*", "*", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", "*", "*", "*", "*", "*", " ", " ", " ", " ", " "]]


'''
for i in range(len(board)):
    try:
        print(f'[{i}][{board[i].index("x")}]')
    except:
        continue
#potential method for finding player chords where ‘x’ would be player char
'''

 
        
def battleCheck():
    if playerA.getX() == playerB.getX() and playerA.getY() == playerB.getY():
        battle()
        battlestatus = True
        return battlestatus

def battle():
    #Code for when the two players battle
    if turncount % 2 == 0:
        print("Player A has challenged Player B to a battle!")
    else:
        print("Player B has challenged Player A to a battle!")
    


def printBoard():
    for i in range(15):
        for j in range(15):
            print(board[i][j], end = " ")
        print()
    print()

def pokeChoose(player, r=False):
    print('\n----------------')
    for i in range(len(player.getInventory())):
        if player.getInventory()[i].getBiome() == '*':
            element = 'Normal'
        elif player.getInventory()[i].getBiome() == '^':
            element = 'Earth'
        elif player.getInventory()[i].getBiome() == '~':
            element = 'Water'
        elif player. getInventory()[i].getBiome() == '&':
            element = 'Fire'
        #prints list of pokemon and stats
        print(f'{i+1}. {player.getInventory()[i].getName()} [Health]: {player.getInventory()[i].getHealth()+10*player.getInventory()[i].getLevel()} [Damage]: {player.getInventory()[i].getDamage()+10*player.getInventory()[i].getLevel()} [Dodge]: {player.getInventory()[i].getDodge()+10*player.getInventory()[i].getLevel()} [Defense]: {player.getInventory()[i].getDefense()+10*player.getInventory()[i].getLevel()} [Level]: {player.getInventory()[i].getLevel()} [Element]: {element}')
    print('----------------')
    
    if r == True:
        replace = ' to replace'
    else:
        replace = ' to use in battle'
    # asks for number input to limit chance for user error
    while True:
        
        choice = input(f'Player {player.getName()}: \nChoose a pokemon{replace}.(1-{len(player.getInventory())})\n')
        print('----------------')
        try:
            if 0 <= (int(choice)-1) <= len(player.getInventory()):
                if r == True:
                    choice = player.getInventory()[int(choice)-1]
                    # if r is true it returns the pokemon object
                else:
                    if player.getInventory()[int(choice)-1].getBiome() == '*':
                        element = 'Normal'
                    elif player.getInventory()[int(choice)-1].getBiome() == '^':
                        element = 'Earth'
                    elif player.getInventory()[int(choice)-1].getBiome() == '~':
                        element = 'Water'
                    elif player. getInventory()[int(choice)-1].getBiome() == '&':
                        element = 'Fire'
                    choice = [player.getInventory()[int(choice)-1].getName(), player.getInventory()[int(choice)-1].getHealth(), player.getInventory()[int(choice)-1].getDamage(), player.getInventory()[int(choice)-1].getDodge(), player.getInventory()[int(choice)-1].getDefense(), player.getInventory()[int(choice)-1].getAp(), element, player.getInventory()[int(choice)-1].getLevel(), 0]
                    for i in range(1,len(choice)-4):
                        # this applies level bonuses
                        choice[i] += 10*(choice[-2]-1)
                    # creates a list of all the pokemons features 
                    # [name, health, damage, dodge, defense, ap, biome/element, level, ap turns]
                    # I had to make it into a list because pokemon stats are not alterable to my knowledge
                break
            else:
                input('Invalid choice!\n')
        except:
            input('Input must be a number!\n')
    
    return choice
# takes in a list of poke stats and prints it to terminal
def pokeStats(pokeA):
    print('----------------')
    print(f'Name: [{pokeA[0]}]')
    print(f'Level: [{pokeA[7]}]')
    print(f'Health: [{pokeA[1]}]')
    print(f'Damage: [{pokeA[2]}]')
    print(f'Dodge: [{pokeA[3]}]')
    print(f'Defense: [{pokeA[4]}]')
    print(f'AP: [{pokeA[5]}]')
    print(f'Element: [{pokeA[6]}]')
    if pokeA[8] > 0:
        print(f'Rounds of AP left: [{pokeA[8]}]')
    input('----------------\n')

def apManager(pokeA, addsub):
    if addsub == 'add':
        if pokeA[8] > 0:
            input('AP already active')
        elif pokeA[5] > 0:
            pokeA[5] -= 1
            pokeA[8] = 2
            if pokeA[6] == 'Fire':
                pokeA[2] += 20 
                print(f'Attack damage increased! [{pokeA[2]}]')
            elif pokeA[6] == 'Water':
                pokeA[3] += 20
                print(f'Dodge chance increased! [{pokeA[6]}]')
            elif pokeA[6] == 'Earth':
                pokeA[4] += 20
                print(f'Defense stat increased! [{pokeA[4]}]')
            elif pokeA[6] == 'Normal':
                pokeA[1] += 20
                print(f'Health increased! [{pokeA[1]}]')
        else:
            print('No AP left!')
    elif addsub == 'sub':
        print(f'[{pokeA[0]}]\'s AP has worn off!')
        if pokeA[6] == 'Fire':
            pokeA[2] -= 20 
            print(f'Attack damage dropped! [{pokeA[2]}]')
        elif pokeA[6] == 'Water':
            pokeA[3] -= 20
            print(f'Dodge chance dropped! [{pokeA[6]}]')
        elif pokeA[6] == 'Earth':
            pokeA[4] -= 20
            print(f'Defense stat dropped! [{pokeA[4]}]')
        elif pokeA[6] == 'Normal':
            pokeA[1] -= 20
            if pokeA[1] <= 0:
                pokeA[1] = 1
            print(f'Health dropped! [{pokeA[1]}]')
        print('----------------')
        pokeA[-1] = 0
    return pokeA
            

def battleScenario(attacker, defender, pokeA, pokeB, histA, histB):
    
    while True:
        print(f'Player {attacker.getName()}\'s attack!\n----------------')
        print(f'Your pokemon: [{pokeA[0]}]')
        print('1. Basic Attack')
        print('2. Strike')
        print(f'3. Use AP [{pokeA[5]}]')
        print(f'4. Stats')
        print('5. Swap pokemon')
        while True:
            attackerChoice = input(f'Select action (1-5):\n')
            try:
                if 1 <= int(attackerChoice) <= 5:
                    attackerChoice = int(attackerChoice)
                    break
                else:
                    print('Invalid input!')
            except:
                print('Input must be a number!')
        if attackerChoice == 1:
            attackType = 'basic'
            break
        if attackerChoice == 2:
            attackType = 'strike'
            break
        if attackerChoice == 3:
            pokeA = apManager(pokeA, 'add')
            continue    
        if attackerChoice == 4:
            pokeStats(pokeA)
            continue
        if attackerChoice == 5:
            if pokeA[-1] > 0:
                pokeA = apManager(pokeA, 'sub')
            histA.insert(0, pokeA)
            pokeA = pokeChoose(attacker)
            input(f'Player {attacker.getName()} has switched to [{pokeA[0]}]!\n')
            for i in range(len(histA)):
                if histA[i][0] == pokeA[0]:
                    pokeA = histA[i]
                    break
            attackType = 'nothing'
            break
    while True:
        print(f'Player {defender.getName()}\'s defense!\n----------------')
        print(f'Your pokemon: [{pokeB[0]}]')
        print('1. Defend')
        print('2. Dodge')
        print(f'3. Use AP [{pokeB[5]}]')
        print(f'4. Stats')
        print('5. Swap pokemon')
        while True:
            defenderChoice = input(f'Select action (1-5):\n')
            try:
                if 1 <= int(defenderChoice) <= 5:
                    defenderChoice = int(defenderChoice)
                    break
                else:
                    print('Invalid input!')
            except:
                print('Input must be a number!')
        if defenderChoice == 1:
            defenseType = 'defend'
            break
        if defenderChoice == 2:
            defenseType = 'dodge'
            break
        if defenderChoice == 3:
            pokeB = apManager(pokeB, 'add')
            continue    
        if defenderChoice == 4:
            pokeStats(pokeB)
            continue
        if defenderChoice == 5:
            if pokeB[-1] > 0:
                pokeB = apManager(pokeB, 'sub')
            histB.insert(0, pokeB)
            pokeB = pokeChoose(defender)
            input(f'Player {defender.getName()} has switched to [{pokeB[0]}]!\n')
            for i in range(len(histB)):
                if histB[i][0] == pokeB[0]:
                    pokeB = histB[i]
                    break
            defenseType = 'nothing'
            break
    # attack effectiveness is determined by d20
    if attackType == 'basic':
        attackRoll = random.randint(1,20)
        defenseRoll = random.randint(1, 20)
        if defenseType == 'defend':
            x = (attackRoll * pokeA[2] // 20) - (defenseRoll * pokeB[4] // 20)
            if x > 0:
                print(f'Player {attacker.getName()}\'s [{pokeA[0]}] broke through [{pokeB[0]}]\'s defense dealing {x} damage!')
                pokeB[1] -= x
            else:
                print(f'[{pokeB[0]}]\'s defense held and [{pokeA[0]}] dealt no damage!')
        elif defenseType == 'dodge':
            if (attackRoll * pokeA[2] // 20) > (defenseRoll * pokeB[3] // 20):
                print(f'Player {attacker.getName()}\'s [{pokeA[0]}] hit [{pokeB[0]}] for {(attackRoll * pokeA[2] // 20)} damage!')
                pokeB[1] -= (attackRoll * pokeA[2] // 20)
            else:
                print(f'[{pokeB[0]}] dodged [{pokeA[0]}]\'s attack!')
        else:
            x = (attackRoll * pokeA[2] // 20)
            print(f'Player {attacker.getName()}\'s [{pokeA[0]}] hit [{pokeB[0]}] for {x} damage!')
            pokeB[1] -= x
    # strike rolls with disadvantage but deal double damage if they land
    # if the opponent manages to defend they can parry 
    if attackType == 'strike':
        attackRoll1 = random.randint(1,20)
        attackRoll2 = random.randint(1,20)
        defenseRoll = random.randint(1, 20)
        if attackRoll1 <= attackRoll2:
            attackRoll = attackRoll1
        else:
            attackRoll = attackRoll2
        if defenseType == 'defend':
            x = (attackRoll * pokeA[2] // 20) - (defenseRoll * pokeB[4] // 20)
            if x > 0:
                print(f'Player {attacker.getName()}\'s [{pokeA[0]}] broke through [{pokeB[0]}]\'s defense with a strike dealing {2 * x} damage!')
                pokeB[1] -= 2*x
            else:
                print(f'Player {defender.getName()}\'s [{pokeB[0]}] parried [{pokeA[0]}]\'s strike dealing {-x} damage!')
                pokeA[1] -= -x
        elif defenseType == 'dodge':
            x = (attackRoll * pokeA[2] // 20) - (defenseRoll * pokeB[3] // 20)
            if x > 0:
                print(f'Player {attacker.getName()}\'s [{pokeA[0]}] hit [{pokeB[0]}] for {2*(attackRoll * pokeA[2] // 20)} damage!')
                pokeB[1] -= 2*(attackRoll * pokeA[2] // 20)
            else:
                print(f'[{pokeB[0]}] dodged [{pokeA[0]}]\'s attack!')
        else:
            x = 2 * (attackRoll * pokeA[2] // 20)
            print(f'Player {attacker.getName()}\'s [{pokeA[0]}] hit [{pokeB[0]}] for {x} damage!')
            pokeB[1] -= x
    print('----------------')
    if pokeA[8] > 0:
        pokeA[8] -= 1
        if pokeA[8] == 0:
            pokeA = apManager(pokeA, 'sub')
    if pokeB[8] > 0:
        pokeB[8] -= 1
        if pokeB[8] == 0:
            pokeB = apManager(pokeB, 'sub')
    if pokeA[1] <= 0:
        print(f'[{pokeA[0]}] has fainted!')
        input('----------------\n')
        for i in range(len(attacker.getInventory())):
            if attacker.getInventory()[i].getName() == pokeA[0]:
                del attacker.getInventory()[i]
                break
        if len(attacker.getInventory()) == 0:
            print(f'Player {defender.getName()} wins!')
            input('\n----------------\n')
            battlestatus = False
            return pokeA, pokeB, histA, histB, battlestatus
        else:
            pokeA = pokeChoose(attacker)
    if pokeB[1] <= 0:
        print(f'[{pokeB[0]}] has fainted!')
        input('----------------\n')

        for i in range(len(defender.getInventory())):
            if defender.getInventory()[i].getName() == pokeB[0]:
                del defender.getInventory()[i]
                break
        if len(defender.getInventory()) == 0:
            print(f'Player {attacker.getName()} wins!')
            input('\n----------------\n')
            battlestatus = False
            return pokeA, pokeB, histA, histB, battlestatus
        else:
            pokeB = pokeChoose(defender)
    battlestatus = True
    return pokeA, pokeB, histA, histB, battlestatus
            
    

#Prompting the players for a turn
battlestatus = False
pokeA = ''
pokeB = ''
histA = []
histB = []
turncount = 0
action = ""
while (action != "quit"):
    
    if turncount % 2 == 0:
        name = "A"
    else:
        name = "B"
    if battlestatus == True:
        # if player does not have an active pokemon pokeChoose has them select one
        if pokeA == '':
            pokeA = pokeChoose(playerA)
            
            print()
        if pokeB == '':
            pokeB = pokeChoose(playerB)
            print()
            #print(pokeB.getName())
        if name == 'A':
            # if player does not have an active pokemon pokeChoose has them select one
            if pokeA == '':
                pokeA = pokeChoose(playerA)
            
                print()
                
            if pokeB == '':
                pokeB = pokeChoose(playerB)
                print()
                #print(pokeB.getName())
            pokeA, pokeB, histA, histB, battlestatus = battleScenario(playerA, playerB, pokeA, pokeB, histA, histB)
            
        elif name == 'B':
            # if player does not have an active pokemon pokeChoose has them select one
            if pokeB == '':
                pokeB = pokeChoose(playerB)
                print()
                #print(pokeB.getName())
            if pokeA == '':
                pokeA = pokeChoose(playerA)
            
                print()
            pokeB, pokeA, histB, histA, battlestatus = battleScenario(playerB, playerA, pokeB, pokeA, histB, histA)
            
        turncount += 1
        
        # if youre in combat, the loop skips over printing the board and player options
        continue
        
    #Assigning original or loaded locations of the Players
    board[playerA.getY()][playerA.getX()] = "A"
    board[playerB.getY()][playerB.getX()] = "B"
    
    #Printing the board for the start of the game    
    printBoard()
    
    action = input(f"Player {name} please enter an option (inventory/move/train/quit): ")
    
    if action == "move":
        move = input("Please enter a move (W, A, S, D): ").strip().upper()
        while move not in ["W", "A", "S", "D"]:
            move = input("Invalid input. Please enter a move (W, A, S, D): ").strip().upper()
        if name == "A" and playerA.inBounds(move):
            #Resetting the previous location back to the old biome, moving the player
            board[playerA.getY()][playerA.getX()] = playerA.getBiome()
            old_biome = playerA.getBiome()
            playerA.move(move)
            
            #Setting the new biome tag to the new location, assigning the player to the new position
            playerA.setBiome(board[playerA.getY()][playerA.getX()])
            board[playerA.getY()][playerA.getX()] = "A"

            #Printing the board
            printBoard()

            #Checks new biome against old biome to see if we changed biomes
            new_biome = playerA.getBiome()
            if old_biome != new_biome:
                playerA.enterBiome()
            
            #Checking for a battle
            battlestatus = battleCheck()
            
        elif name == "B" and playerB.inBounds(move):
            #Resetting the previous location back to the old biome, moving the player
            board[playerB.getY()][playerB.getX()] = playerB.getBiome()
            old_biome = playerB.getBiome()
            playerB.move(move)
            
            #Setting the new biome tag to the new location, assigning the player to the new position
            playerB.setBiome(board[playerB.getY()][playerB.getX()])
            board[playerB.getY()][playerB.getX()] = "B"
            
            #Printing the board
            printBoard()
            
            #Checks new biome against old biome to see if we changed biomes
            new_biome = playerB.getBiome()
            if old_biome != new_biome:
                playerB.enterBiome()

            #Checking for a battle
            battleCheck()
    
        else:
            print("Sorry, that move is not inbounds! Please try again!")
            turncount -=1
    
    elif action == "inventory":
        if name == "A":
            playerA.displayInventory()
        else:
            playerB.displayInventory()
        turncount -= 1
            
    elif action == "train":
        #Check which player is training
        if name == "A":
            #Let the user know what level their pokemon are at
            playerA.displayInventory()
            #store the inventory into a temporary varibale that can be checked with
            inv = playerA.getInventoryAsString()
            #if the user has no pokemon, they can't train their pokemon
            if len(inv) <= 0:
                print("You have no Pokemon to train! Please select another option!")
                turncount -= 1
            else:
                #asks the user which pokemon they want to train
                trainee = input("Which Pokemon would you like to train? \n").upper().strip()
                #if they didn't type in a pokemon that is in the list keep asking until they do
                while trainee not in inv and len(inv) > 0:
                    trainee = input("Pokemon not found in inventory. Please select a Pokemon in your inventroy: \n").upper().strip()
                    playerA.displayInventory()
                if trainee in inv:
                    #trains the pokemon by adding a level to the pokemon
                    #the method returns a 1 if the pokemon is already at level 5 which allows the user to select another option
                    #the method returns a 0 if the pokemon is not at level 5 and continues alternating players
                    turncount -= playerA.trainPokemon(trainee)

            
        else:
            #Let the user know what level their pokemon are at
            playerB.displayInventory()
            #store the inventory into a temporary varibale that can be checked with
            inv = playerB.getInventoryAsString()
            #if the user has no pokemon, they can't train their pokemon
            if len(inv) <= 0:
                print("You have no Pokemon to trian! Please select another option!")
                turncount -= 1
            else: 
                #asks the user which pokemon they want to train
                trainee = input("Which Pokemon would you like to train? \n").upper().strip()
                #if they didn't type in a pokemon that is in the list keep asking until they do
                while trainee not in inv and len(inv) > 0:
                    trainee = input("Pokemon not found in inventory. Please select a Pokemon in your inventroy: \n").upper().strip()
                    playerA.displayInventory()
                if trainee in inv:
                    #trains the pokemon by adding a level to the pokemon
                    #the method returns a 1 if the pokemon is already at level 5 which allows the user to select another option
                    #the method returns a 0 if the pokemon is not at level 5 and continues alternating players
                    turncount -= playerB.trainPokemon(trainee)
        
        
    elif action == "quit":
        break   
        
    else:
        print("Invalid input. Please enter (move/train/quit): ")
        turncount -= 1

    turncount += 1

print("Thank you for playing the Pokemon Game!")
        
            

with open('player_data.txt', 'w') as datFile:
    datFile.write(f'{playerA.getName()}\n')
    for i in range(len(playerA.getInventory())):
        datFile.write(f'{playerA.getInventory()[i].getName()}{playerA.getInventory()[i].getLevel()}  ')
        datFile.write(f'\n')
    datFile.write(f'{playerA.getBiome()}\n')
    datFile.write(f'{playerA.getX}  {playerA.getY}\n')
    datFile.write('---\n')
    datFile.write(f'{playerB.getName()}\n')
    for i in range(len(playerB.getInventory())):
        datFile.write(f'{playerB.getInventory()[i].getName()}{playerB.getInventory()[i].getLevel()}  ')
        datFile.write(f'\n')
    datFile.write(f'{playerB.getBiome()}\n')
    datFile.write(f'{playerB.getX}  {playerB.getY}\n')
    
    
    '''for i in range(len(playerOneProfile)):
        for j in range(len(playerOneProfile[i])):
            datFile.write(f'{playerOneProfile[i][j]}')
            if playerOneProfile[i][j] in poke_roster:
                datFile.write(f'{}')
            datFile.write('  ')
        datFile.write('\n')
    datFile.write(f'---\n')
    for i in range(len(playerTwoProfile)):
        for j in range(len(playerTwoProfile[i])):
            datFile.write(f'{playerTwoProfile[i][j]}')
            datFile.write(f'  ')
        datFile.write('\n')'''
