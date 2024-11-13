
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
        playerOneProfile = [['A'], [], ['.'], [5, 9]]
        playerTwoProfile = [['B'], [], ['.'], [9, 5]]
        break
poke_roster = ['MOUSE', 'HAWK', 'WOLF', 'BEAR', 'EMBER', 'FLAME DWELLER', 'DRAGON', 'PHOENIX', 'CLAM', 'SWORDFISH', 'NESSIE', 'MEGALODON', 'SPROUT', 'POISON IVY', 'GIANT SEQUOIA', 'BIGFOOT', 'FRODO SPEARS']

#Creating 4 normal pokemon, normal pokemon generally specialize in HEALTH
pk_mouse = Pokemon("MOUSE", "NORMAL", 30, 10, 15, 0, 1, "*")
pk_hawk = Pokemon("HAWK", "NORMAL", 50, 25, 20, 0, 1, "*")
pk_wolf = Pokemon("WOLF", "NORMAL", 90, 30, 20, 10, 1, "*")
pk_bear = Pokemon("BEAR", "NORMAL", 150, 40, 10, 30, 1, "*")

#Creating 4 fire pokemon, fire pokemon generally specialize in DAMAGE
pk_ember = Pokemon("EMBER", "FIRE", 15, 25, 5, 0, 1, "&")
pk_fire_dweller = Pokemon("FLAME DWELLER", "FIRE", 30, 30, 0, 15, 1, "&")
pk_dragon = Pokemon("DRAGON", "FIRE", 60, 45, 15, 10, 1, "&")
pk_phoenix = Pokemon("PHOENIX", "FIRE", 75, 65, 10, 15, 1, "&")

#Creating 4 water pokemon, water pokemon generally specialize in DODGE
pk_clam = Pokemon("CLAM", "WATER", 25, 10, 30, 15, 1, "~")
pk_swordfish = Pokemon("SWORDFISH", "WATER", 45, 25, 35, 0, 1, "~")
pk_nessie = Pokemon("NESSIE", "WATER", 75, 30, 40, 10, 1, "~")
pk_megalodon = Pokemon("MEGALODON", "WATER", 100, 45, 45, 20, 1, "~")

#Creating 4 earth pokemon, earth pokemon generally specialize in DEFENSE
pk_sprout = Pokemon("SPROUT", "EARTH", 20, 5, 0, 30, 1, "^")
pk_poison_ivy = Pokemon("POISON IVY", "EARTH", 40, 30, 0, 35, 1, "^")
pk_giant_sequoia = Pokemon("GIANT SEQUOIA", "EARTH", 45, 25, 0, 45, 1, "^")
pk_bigfoot = Pokemon("BIGFOOT", "EARTH", 100, 35, 0, 60, 1, "^")

#Creating THE legendary pokemon
pk_frodo = Pokemon("FRODO SPEARS", "LEGENDARY", 200, 100, 0, 0, 1, ".")

#Creating two player objects
playerA = Player(playerOneProfile[0][0], int(playerOneProfile[3][0]), int(playerOneProfile[3][1]), playerOneProfile[1], playerOneProfile[2][0])
playerB = Player(playerTwoProfile[0][0], int(playerTwoProfile[3][0]), int(playerTwoProfile[3][1]), playerTwoProfile[1], playerOneProfile[2][0])

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

def inBounds(user, move):
    #Checking player A's location
    if user == "A":
        if move == "W":
            if (playerA.getY() - 1 >= 5 and playerA.getBiome() in "~&") or (playerA.getY() - 1 >= 0 and playerA.getBiome() in "*^."):
                return True
            else:
                return False
        if move == "S":
            if (playerA.getY() + 1 <= 9 and playerA.getBiome() in "~&") or (playerA.getY() + 1 <= 14 and playerA.getBiome() in "*^."):
                return True
            else:
                return False
        if move == "A":
            if (playerA.getX() - 1 >= 5 and playerA.getBiome() in "^*") or (playerA.getX() - 1 >= 0 and playerA.getBiome() in "~.&"):
                return True
            else:
                return False
        else:
            if (playerA.getX() + 1 <= 9 and playerA.getBiome() in "^*") or (playerA.getX() + 1 <= 14 and playerA.getBiome() in "~.&"):
                return True
            else:
                return False
    
    #Checking player B's location        
    else:
        if move == "W":
            if (playerB.getY() - 1 >= 5 and playerB.getBiome() in "~&") or (playerB.getY() - 1 >= 0 and playerB.getBiome() in "*^."):
                return True
            else:
                return False
        elif move == "S":
            if (playerB.getY() + 1 <= 9 and playerB.getBiome() in "~&") or (playerB.getY() + 1 <= 14 and playerB.getBiome() in "*^."):
                return True
            else:
                return False
        elif move == "A":
            if (playerB.getX() - 1 >= 5 and playerB.getBiome() in "^*") or (playerB.getX() - 1 >= 0 and playerB.getBiome() in "~.&"):
                return True
            else:
                return False
        else:
            if (playerB.getX() + 1 <= 9 and playerB.getBiome() in "^*") or (playerB.getX() + 1 <= 14 and playerB.getBiome() in "~.&"):
                return True
            else:
                return False
 
def enterBiome(player, biome): 
    if biome == "^":
        print(f"Player {player} is now entering the Mountain Biome")
    elif biome == "~":
        print(f"Player {player} is now entering the Water Biome")
    elif biome == "&":
        print(f"Player {player} is now entering the Fire Biome")
    elif biome == "*":
        print(f"Player {player} is now entering the Home Biome")
    else:
        print(f"Player {player} is now entering the City Biome")
        
def battleCheck():
    if playerA.getX() == playerB.getX() and playerA.getY() == playerB.getY():
        battle()

def battle():
    #Code for when the two players battle
    if turncount % 2 == 0:
        print("Player A has challeged Player B to a battle!")
    else:
        print("Player B has challeged Player A to a battle!")

#Prompting the players for a turn
turncount = 0
action = ""
while (action != "quit"):
    if turncount % 2 == 0:
        name = "A"
    else:
        name = "B"
    
    #Assigning original or loaded locations of the Players
    board[playerA.getX()][playerA.getY()] = "A"
    board[playerB.getX()][playerB.getY()] = "B"
    
    #Printing the board for the start of the game    
    if turncount == 0:
        for i in range(15):
            for j in range(15):
                print(board[i][j], end = " ")
            print()
        print()
    
    action = input(f"Player {name} please enter an option (inventory/move/train/quit): ")
    
    if action == "move":
        move = input("Please enter a move (W, A, S, D): ").strip().upper()
        while move not in ["W", "A", "S", "D"] and inBounds():
            move = input("Invalid input. Please enter a move (W, A, S, D): ").strip().upper()
        if name == "A" and inBounds("A", move):
            #Resetting the previous location back to the old biome, moving the player
            board[playerA.getX()][playerA.getY()] = playerA.getBiome()
            old_biome = playerA.getBiome()
            playerA.move(move)
            
            #Setting the new biome tag to the new location, assigning the player to the new position
            playerA.setBiome(board[playerA.getX()][playerA.getY()])
            board[playerA.getX()][playerA.getY()] = "A"

            #Printing the board
            for i in range(15):
                for j in range(15):
                    print(board[i][j], end = " ")
                print()
            print()

            #Checks new biome against old biome to see if we changed biomes
            new_biome = playerA.getBiome()
            if old_biome != new_biome:
                enterBiome("A", playerA.getBiome())
            
            #Checking for a battle
            battleCheck()
            
        elif name == "B" and inBounds("B", move):
            #Resetting the previous location back to the old biome, moving the player
            board[playerB.getX()][playerB.getY()] = playerB.getBiome()
            old_biome = playerB.getBiome()
            playerB.move(move)
            
            #Setting the new biome tag to the new location, assigning the player to the new position
            playerB.setBiome(board[playerB.getX()][playerB.getY()])
            board[playerB.getX()][playerB.getY()] = "B"
            
            #Printing the board
            for i in range(15):
                for j in range(15):
                    print(board[i][j], end = " ")
                print()
            print()
            
            #Checks new biome against old biome to see if we changed biomes
            new_biome = playerB.getBiome()
            if old_biome != new_biome:
                enterBiome("B", playerB.getBiome())

            #Checking for a battle
            battleCheck()
    
        else:
            print("Sorry, that move is not inbounds! Please try again!")
    
    elif action == "inventory":
        if name == "A":
            print(f"Player {name}'s inventory: \n{playerA.displayInventory()}")
        else:
            print(f"Player {name}'s inventory: \n{playerB.displayInventory()}")
        turncount -= 1
            
    elif action == "train":
        if name == "A":
            playerA.displayInventory()
            trainee = input("Which Pokemon would you like to train?").upper().strip()
            while trainee not in playerA.getInventory():
                trainee = input("Pokemon not found in inventory. Please select a Pokemon in your inventroy").upper().strip()
                print(playerA.getInventory())
            if trainee in playerA.displayInventory():
                playerA.trainPokemon(trainee)
        else:
            playerB.displayInventory()
            trainee = input("Which Pokemon would you like to train?").upper().strip()
            while trainee not in playerB.getInventory():
                trainee = input("Pokemon not found in inventory. Please select a Pokemon in your inventroy").upper().strip()
                print(playerB.getInventory())
            if trainee in playerB.getInventory():
                playerB.trainPokemon(trainee)
        
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
