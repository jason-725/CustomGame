import random


class Pokemon():
    def __init__(self, name, type, health, damage, dodge, defense, level, biome, ap):
        self.name = name
        self.type = type
        self.health = health
        self.damage = damage
        self.dodge = dodge
        self.defense = defense
        self.level = level
        self.biome = biome
        self.ap = ap
    
    def getName(self):
        return self.name
    
    def getType(self):
        return self.type
    
    def getHealth(self):
        return self.health
    
    def getDamage(self):
        return self.damage
    
    def getDodge(self):
        return self.dodge
    
    def getDefense(self):
        return self.defense
    
    def getLevel(self):
        return self.level
    
    def getBiome(self):
        return self.biome
        
    def getAp(self):
        return self.ap

    def train(self):
        self.level += 1
        self.health += 5
        self.damage += 5
        self.dodge += 5
        self.defense += 5
        
    def printPokemonLevel(self):
        print(f"{self.name}'s level is {self.level}")

class FirePokemon(Pokemon):
    def __init__(self, name, type, health, damage, dodge, defense, level, biome):
        super().__init__(name, type, health, damage, dodge, defense, level, biome)


class WaterPokemon(Pokemon):
    def __init__(self, name, type, health, damage, dodge, defense, level, biome):
        super().__init__(name, type, health, damage, dodge, defense, level, biome)
        
    
class EarthPokemon(Pokemon):
    def __init__(self, name, type, health, damage, dodge, defense, level, biome):
        super().__init__(name, type, health, damage, dodge, defense, level, biome)
        
        
class NormalPokemon(Pokemon):
    def __init__(self, name, type, health, damage, dodge, defense, level, biome):
        super().__init__(name, type, health, damage, dodge, defense, level, biome)
        
        
        
class Player():
    def __init__(self, name, y_position, x_position, inventory, biome):
        self.name = name
        self.x_position = x_position
        self.y_position = y_position
        self.inventory = inventory
        self.biome = biome
        
    def getName(self):
        return self.name
    
    def getX(self):
        return self.x_position
    
    def getY(self):
        return self.y_position
    
    def getInventory(self):
        return self.inventory
    
    def getInventoryAsString(self):
        inv = []
        for pokemon in self.inventory:
            inv.append(pokemon.getName())
        return inv
    
    def getBiome(self):
        return self.biome
    
    def setBiome(self, char):
        self.biome = char
    
    def moveRight(self):
        self.x_position += 1
    
    def moveLeft(self):
        self.x_position -= 1
        
    def moveUp(self):
        self.y_position -= 1
    
    def moveDown(self):
        self.y_position += 1
        
    def move(self, move):
        if move == "W":
            self.moveUp()
        elif move == "A":
            self.moveLeft()
        elif move == "S":
            self.moveDown()
        elif move == "D":
            self.moveRight()
            
        if random.random() < 0.5:
            print(f"Player {self.name} has a chance to catch a Pokemon!")
            self.catchPokemon()
            
    def inBounds(self, move):
         #Checking player's location
            if move == "W":
                if (self.y_position - 1 >= 5 and self.biome in "~&") or (self.y_position - 1 >= 0 and self.biome in "*^."):
                    return True
                else:
                    return False
            if move == "S":
                if (self.y_position + 1 <= 9 and self.biome in "~&") or (self.y_position + 1 <= 14 and self.biome in "*^."):
                    return True
                else:
                    return False
            if move == "A":
                if (self.x_position - 1 >= 5 and self.biome in "^*") or (self.x_position - 1 >= 0 and self.biome in "~.&"):
                    return True
                else:
                    return False
            else:
                if (self.x_position + 1 <= 9 and self.biome in "^*") or (self.x_position + 1 <= 14 and self.biome in "~.&"):
                    return True
                else:
                    return False
            
    def enterBiome(self):
        #Print out which biome the player is joining
        if self.biome == "^":
            print(f"Player {self.name} is now entering the Mountain Biome")
        elif self.biome == "~":
            print(f"Player {self.name} is now entering the Water Biome")
        elif self.biome == "&":
            print(f"Player {self.name} is now entering the Fire Biome")
        elif self.biome == "*":
            print(f"Player {self.name} is now entering the Home Biome")
        else:
            print(f"Player {self.name} is now entering the City Biome")
            
    def displayInventory(self):
        if len(self.inventory) == 0:
            print(f"Player {self.name} has no Pokemon in their inventory!")
        else:
            print(f"Player {self.name}'s inventory:")
            for pokemon in self.inventory:
                if pokemon.getLevel() >= 5:
                    print(f"\t{pokemon.getName()} - Level {pokemon.getLevel()} (MAX LEVEL)")
                else:
                    print(f"\t{pokemon.getName()} - Level {pokemon.getLevel()}")

    def trainPokemon(self, trainee):
        #Goes iterates through each pokemon
        for pokemon in self.inventory:
            #Retrieves the string name from each pokemon to easily compare and trains the pokemon
            if pokemon.getName() == trainee:
                if pokemon.getLevel() >= 5:
                    print(f"{pokemon.getName()}'s level is maxed out! Select train again or select another option!")
                    return 1
                else:
                    pokemon.train()
                    print(f"{pokemon.getName()} leveled up to level {pokemon.getLevel()}!")
                    return 0
                
        def catchPokemon(self):
        #returns a number between 0-1
        rarity_chance = random.random()
        pokemon = None
        if rarity_chance < 0.4:
            # 40% chance for common
            if self.biome == "*":
                pokemon = NormalPokemon("MOUSE", "NORMAL", 30, 10, 15, 0, 1, "*")
            elif self.biome == "&":
                pokemon = FirePokemon("EMBER", "FIRE", 15, 25, 5, 0, 1, "&")
            elif self.biome == "~":
                pokemon = WaterPokemon("CLAM", "WATER", 25, 10, 30, 15, 1, "~")
            elif self.biome == "^":
                pokemon = EarthPokemon("SPROUT", "EARTH", 20, 5, 0, 30, 1, "^")
                
        elif rarity_chance < 0.7:
            # 30% chance for uncommon (next 30%)
            if self.biome == "*":
                pokemon = NormalPokemon("HAWK", "NORMAL", 50, 25, 20, 0, 1, "*")
            elif self.biome == "&":
                pokemon = FirePokemon("FLAME DWELLER", "FIRE", 15, 25, 5, 0, 1, "&")
            elif self.biome == "~":
                pokemon = WaterPokemon("SWORDFISH", "WATER", 45, 25, 35, 0, 1, "~")
            elif self.biome == "^":
                pokemon = EarthPokemon("POISON IVY", "EARTH", 40, 30, 0, 35, 1, "^")
        elif rarity_chance < 0.9:
            # 20% chance for rare (next 20%)
            if self.biome == "*":
                pokemon = NormalPokemon("WOLF", "NORMAL", 90, 30, 20, 10, 1, "*")
            elif self.biome == "&":
                pokemon = FirePokemon("DRAGON", "FIRE", 30, 30, 0, 15, 1, "&")
            elif self.biome == "~":
                pokemon = WaterPokemon("NESSIE", "WATER", 75, 30, 40, 10, 1, "~")
            elif self.biome == "^":
                pokemon = EarthPokemon("GIANT SEQUOIA", "EARTH", 45, 25, 0, 45, 1, "^")
        else:
            # 10% chance for legendary (last 10%)
            if self.biome == "*":
                pokemon = NormalPokemon("BEAR", "NORMAL", 150, 40, 10, 30, 1, "*")
            elif self.biome == "&":
                pokemon = FirePokemon("PHOENIX", "FIRE", 75, 65, 10, 15, 1, "&")
            elif self.biome == "~":
                pokemon = WaterPokemon("MEGALODON", "WATER", 100, 45, 45, 20, 1, "~")
            elif self.biome == "^":
                pokemon = EarthPokemon("BIGFOOT", "EARTH", 100, 35, 0, 60, 1, "^")

        # Add the newly caught Pokémon to the player's inventory
        if pokemon != None:
            if len(self.inventory) >= 3:
                print(f"Player {self.name} already has the maximum amount of pokemon!")
                answer = input(f"Would you like to switch out an already caught pokemon with {pokemon.getName()}? (Y/N)").strip().upper()
                if answer == "Y":
                    print("Which Pokemon would you like to remove?")
                    self.displayInventory()
                    bad_pokemon = input("Enter Pokemon: ")
                    while bad_pokemon not in self.inventory:
                        bad_pokemon = input("You do not have that Pokemon, select another to release")
                    for i in range(len(self.inventory)):
                        if self.inventory[i].getName() == bad_pokemon:
                            self.inventory.pop(i)
                            break
                    self.inventory.append(pokemon)
                    print(f"{self.name} caught a {pokemon.getName()}!")
                else:
                    print(f"Player {self.name} ran away from {pokemon.getName()}")
            else:
                not_caught = True
                for name in self.inventory:
                    if pokemon.getName() == name.getName():
                        print(f"Player {self.name} cannot catch {pokemon.getName()}! He already has one!")
                        not_caught = False
                        break
                if not_caught:
                    self.inventory.append(pokemon)
                    print(f"{self.name} caught a {pokemon.getName()}!")
                
           
        
        
                
    def saveData(self):
    # Open the file in append mode after clearing it initially
        with open('player_data.txt', 'a') as datFile:
        # Write the player's name
            datFile.write(f'{self.name}\n')
        
        # Loop through the player's inventory and write each Pokémon's data
            for pokemon in self.inventory:
                datFile.write(f'{pokemon.getName()} {pokemon.getLevel()}  ')
            datFile.write(f'\n')

        # Write biome and position data
            datFile.write(f'{self.biome}\n')
            datFile.write(f'{self.x_position}  {self.y_position}\n')

        # Write separator for clarity between player data
            datFile.write('---\n')
        #not sure what we want to do here with the --- at the end of the file. shouldn't matter?
        # datFile.write(f'{playerB.getName()}\n')
            
            