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
            
