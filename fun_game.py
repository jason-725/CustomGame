
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

from game_classes import Pokemon, FirePokemon, NormalPokemon, WaterPokemon, EarthPokemon, Player

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


#Creating THE legendary pokemon
# pk_frodo = Pokemon("FRODO SPEARS", "LEGENDARY", 200, 100, 0, 0, 1, ".")

# Factory method to create a Pokemon
def create_pokemon(name):
    # Example Pokemon data (name -> type)
    pokemon_types = {
        "MOUSE": "NORMAL",
        "HAWK": "NORMAL",
        "WOLF": "NORMAL",
        "BEAR": "NORMAL",
        "EMBER": "FIRE",
        "FLAME DWELLER" : "FIRE",
        "DRAGON" : "FIRE",
        "PHOENIX" : "FIRE",
        "CLAM": "WATER",
        "SWORDFISH": "WATER",
        "NESSIE": "WATER",
        "MEGALODON": "WATER",
        "SPROUT":"EARTH",
        "POISON IVY":"EARTH",
        "GIANT SEQUOIA":"EARTH",
        "BIGFOOT":"EARTH"
    }
    
    # Check if the pokemon name exists in the dictionary
    if name not in pokemon_types:
        
        raise ValueError(f"No known Pokemon with name {name}")
    
    # Determine the type of the Pokemon
    type = pokemon_types[name]
    
    level = 1
    
    # Create the correct subclass based on type
    if type == "FIRE":
        if name == "EMBER":
            return FirePokemon("EMBER", "FIRE", 15, 25, 5, 0, 1, "&")
        elif name == "FLAME DWELLER":
            return FirePokemon("FLAME DWELLER", "FIRE", 15, 25, 5, 0, 1, "&")
        elif name == "DRAGON":
            return FirePokemon("DRAGON", "FIRE", 30, 30, 0, 15, 1, "&")
        elif name == "PHOENIX":
            return FirePokemon("PHOENIX", "FIRE", 75, 65, 10, 15, 1, "&")
    elif type == "WATER":
        if name == "CLAM":
            return WaterPokemon("CLAM", "WATER", 25, 10, 30, 15, 1, "~")
        elif name == "SWORDFISH":
            return WaterPokemon("SWORDFISH", "WATER", 45, 25, 35, 0, 1, "~")
        elif name == "NESSIE":
            return WaterPokemon("NESSIE", "WATER", 75, 30, 40, 10, 1, "~")
        elif name == "MEGALODON":
            return WaterPokemon("MEGALODON", "WATER", 100, 45, 45, 20, 1, "~")
    elif type == "EARTH":
        if name == "SPROUT":
            return EarthPokemon("SPROUT", "EARTH", 20, 5, 0, 30, 1, "^")
        elif name == "POISON IVY":
            return EarthPokemon("POISON IVY", "EARTH", 40, 30, 0, 35, 1, "^")
        elif name == "GIANT SEQUOIA":
            return EarthPokemon("GIANT SEQUOIA", "EARTH", 45, 25, 0, 45, 1, "^")
        elif name == "BIGFOOT":
            return EarthPokemon("BIGFOOT", "EARTH", 100, 35, 0, 60, 1, "^")
    elif type == "NORMAL":
        if name == "MOUSE":
            return NormalPokemon("MOUSE", "NORMAL", 30, 10, 15, 0, 1, "*")
        elif name == "HAWK":
            return NormalPokemon("HAWK", "NORMAL", 50, 25, 20, 0, 1, "*")
        elif name == "WOLF":
            return NormalPokemon("WOLF", "NORMAL", 90, 30, 20, 10, 1, "*")
        elif name == "BEAR":
            return NormalPokemon("BEAR", "NORMAL", 150, 40, 10, 30, 1, "*")


# test = ["MOUSE", "NESSIE"]
#Delcare the array that the player's inventory that pokemon will be adding into
populated_playerA_inv = []
#playerOneProfile is the saved list of pokemon names in previous safe file
#Go through the list and find the pokemon previously caught
for name in playerOneProfile[1]:
    if len(name) > 1:
        pass_variable = name.strip()
        populated_playerA_inv.append(create_pokemon(pass_variable))
            
# for i in range(len(playerOneProfile[1])):
#     if len(playerOneProfile[1][i]) > 1:
#         pass_variable = playerOneProfile[1][i].strip()
#         populated_playerA_inv.append(create_pokemon(pass_variable, playerOneProfile[-1][i]))            

#Delcare the array that the player's inventory that pokemon will be adding into            
# test = ["SPROUT", "MEGALODON"]
populated_playerB_inv = []
#playerTwoProfile is the saved list of pokemon names in previous safe file
#Go through the list and find the pokemon previously caught
for name in playerTwoProfile[1]:
    if len(name) > 1:
        pass_variable = name.strip()
        populated_playerB_inv.append(create_pokemon(pass_variable))

#Creating two player objects
playerA = Player(playerOneProfile[0][0], int(playerOneProfile[3][1]), int(playerOneProfile[3][0]), populated_playerA_inv, playerOneProfile[2][0])
playerB = Player(playerTwoProfile[0][0], int(playerTwoProfile[3][1]), int(playerTwoProfile[3][0]), populated_playerB_inv, playerOneProfile[2][0])


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

def battle():
    #Code for when the two players battle
    if turncount % 2 == 0:
        print("Player A has challeged Player B to a battle!")
    else:
        print("Player B has challeged Player A to a battle!")

def printBoard():
    for i in range(15):
        for j in range(15):
            print(board[i][j], end = " ")
        print()
    print()
    

#Prompting the players for a turn
turncount = 0
action = ""
#Printing the board for the start of the game  
#Assigning original or loaded locations of the Players
board[playerA.getY()][playerA.getX()] = "A"
board[playerB.getY()][playerB.getX()] = "B"
printBoard()
while (action != "quit"):
    if turncount % 2 == 0:
        name = "A"
    else:
        name = "B"
    
    
    
      
    
    
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
            battleCheck()
            
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

#Resets the save file so the program can save new data
open('player_data.txt', 'w').close()  # Clear the file before saving data

# Save data for playerA and playerB
playerA.saveData()
playerB.saveData()

# with open('player_data.txt', 'w') as datFile:
#     datFile.write(f'{playerA.getName()}\n')
#     for i in range(len(playerA.getInventory())):
#         datFile.write(f'{playerA.getInventory()[i].getName()}{playerA.getInventory()[i].getLevel()}  ')
#         datFile.write(f'\n')
#     datFile.write(f'{playerA.getBiome()}\n')
#     datFile.write(f'{playerA.getX}  {playerA.getY}\n')
#     datFile.write('---\n')
#     datFile.write(f'{playerB.getName()}\n')
#     for i in range(len(playerB.getInventory())):
#         datFile.write(f'{playerB.getInventory()[i].getName()}{playerB.getInventory()[i].getLevel()}  ')
#         datFile.write(f'\n')
#     datFile.write(f'{playerB.getBiome()}\n')
#     datFile.write(f'{playerB.getX}  {playerB.getY}\n')
    
    
#     '''for i in range(len(playerOneProfile)):
#         for j in range(len(playerOneProfile[i])):
#             datFile.write(f'{playerOneProfile[i][j]}')
#             if playerOneProfile[i][j] in poke_roster:
#                 datFile.write(f'{}')
#             datFile.write('  ')
#         datFile.write('\n')
#     datFile.write(f'---\n')
#     for i in range(len(playerTwoProfile)):
#         for j in range(len(playerTwoProfile[i])):
#             datFile.write(f'{playerTwoProfile[i][j]}')
#             datFile.write(f'  ')
#         datFile.write('\n')'''
