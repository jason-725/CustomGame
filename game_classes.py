class Pokemon():
    def __init__(self, name, type, health, damage, dodge, defense, level, biome):
        self.name = name
        self.type = type
        self.health = health
        self.damage = damage
        self.dodge = dodge
        self.defense = defense
        self.level = level
        self.biome = biome
    
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
            
    def displayInventory(self):
        for pokemon in self.inventory:
            print(f"{pokemon.getName()} - Level {pokemon.getLevel()}")

    def trainPokemon(self, trainee):
        for pokemon in self.inventory:
            if pokemon.getName() == trainee:
                pokemon.train()
            