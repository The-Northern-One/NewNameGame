import time
import random

foodOptions = ["grain", "corn", "rice", "sheep", "fish", "deer"]
biomeOptions = ["forest", "desert", "farmland", "archipelago", "mountains", "hills"]


def openingCredits(creditsSpeed):
    print("        Welcome to:        ")
    print("        NoNameGame         ")
    print("\n\n")
    time.sleep(creditsSpeed)
    print("A game by David Nord")
    time.sleep(creditsSpeed)
    print("This is version 0.1, the beta update!")
    time.sleep(creditsSpeed)
    print("\n\n Now without further ado, let's play:")
    time.sleep(creditsSpeed)
    print("\n\n\n\n\n" * 7)


openingCredits(1)
difficulty = int(input("What should the difficulty level be?\n"))
if difficulty > 10 or difficulty < 0:
   difficulty = 10
toplay = int(input("How many turns would you like to play?\n"))
if toplay <= 0:
   toplay = 100
   print("\n\n\nCongratulations, you're an idiot!")
omnipotBen = (random.randrange(0, 11) - (0.5 * difficulty))
omnipotAct = (random.randrange((difficulty + 2), 13))
if omnipotAct > 10:
   omnipotAct = 10
if omnipotBen > 10:
   omnipotBen = 10


class Civilization:

    def __init__(self):
        self.prowess = random.randrange((10 - difficulty), 15) - difficulty
        if self.prowess < 0:
            self.prowess = 0

player = Civilization()



class Omipotent:


   def __init__(self, benevolence, active):
       self.ben = benevolence
       self.active = active


class Job:

    def __init__(self, foodCost, resourceCost, Benifits, name):
        self.foodCost = foodCost
        self.resourceCost = resourceCost
        self.Benifits = Benifits
        self.name = name


farmerBenifits = [2, 0, 0, 0, 0]
farmer = Job(0, 0, farmerBenifits, "Farmer")
minerBenifits = [0, 1, 0, 0, 0]
miner = Job(0, 0.25, minerBenifits, "Miner")
mapperBenifits = [0, 0, 0.25, 0, 0]
mapper = Job(1, 1, mapperBenifits, "Mapper")
jobs = [farmer, miner, mapper]


# for later (secret no tell anyone)
class Inhabitant:

    def __init__(self, region, alive, job, name):
        self.region = region
        self.alive = alive
        self.work = job
        self.name = name
    
    def addBenifits(self):
        for i in range(0, len(self.region.jobBenifits)):
            self.region.jobBenifits[i] += self.work.Benifits[i]
    
    def removeBenifits(self):
        for i in range(0, len(self.region.jobBenifits)):
            self.region.jobBenifits[i] -= self.work.Benifits[i]

    def kill(self):
        self.removeBenifits()
        self.alive = False
        self.work = "corpse"
        self.region.pops.remove(self)

    def assignJob(self):
        self.work = random.choice(jobs)

    def jobUpdate(self):
        self.addBenifits()

    def changeJob(self, changeTo):
        self.removeBenifits()
        self.work = changeTo
        self.addBenifits()


class Region:


   def __init__(self, terrain, terrainLevel, resource, water, farmGood, spawnRegion, secret):
       self.terrain = terrain
       self.terrainLevel = terrainLevel
       self.resource = resource
       self.water = water
       self.farmGood = farmGood
       self.buildings = []
       self.megaprojects = []
       self.inhabited = False
       self.jobBenifits = [0, 0, 0, 0, 0]
       if spawnRegion == True:
           self.inhabitants = 15
           self.inhabited = True
           self.pops = []
           while len(self.pops) < self.inhabitants:
               self.popBorn("James")
           self.inhabitantsLastTurn = 15
           self.food = 30
           self.foodProduction = (5 * (0.5 * self.farmGood)) + 25 + (0.3334 * self.inhabitants / 2) + self.jobBenifits[0]
           self.resources = 10
           self.resourceProduction = 5 + self.jobBenifits[1]
           player.prowess += self.jobBenifits[2]
           self.name = input("Name your home region:\n")
           self.buildings.append("Capitol")
       if spawnRegion == False:
           self.inhabitants = 0
           self.food = 5
           self.foodProduction = 0
           self.resources = 50
           self.resourceProduction = 0
           self.name = ""

   def popBorn(self, name):
       self.pops.append(Inhabitant(self, True, "No beuno", name))
       self.pops[len(self.pops) - 1].assignJob()
       self.pops[len(self.pops) - 1].jobUpdate()


   def updateRegion(self):
       for i in self.pops:
           i.jobUpdate()
       self.foodProduction = (5 * (0.5 * self.farmGood)) + 25 + (self.inhabitants * 0.5) + self.jobBenifits[0]
       # self.resourceProduction = 5 + self.jobBenifits[1]

   def updateRegionJobs(self):
       self.jobBenifitsLastTurn = self.jobBenifits
       self.jobBenifits = [0, 0, 0, 0, 0]
       for inhab in self.pops:
           inhab.addBenifits()
    
   def startup(self):
       for ben in range(0, len(self.resource.benifit)):
           if "production" == self.resource.benifit[ben]:
               self.resourceProduction += self.resource.benifitValue[ben]
           elif "food" == self.resource.benifit[ben]:
               self.foodProduction += self.resource.benifitValue[ben]
           elif "explore" == self.resource.benifit[ben]:
               player.prowess += self.resource.benifitValue[ben]





class Building:


   def __init__(self, resourceCost, foodCost, benifits, name):
       self.resourceCost = resourceCost
       self.foodCost = foodCost
       self.benifits = benifits
       self.name = name


   def built(self):
       spawnRegion.foodProduction += self.benifits[0]
       spawnRegion.resourceProduction += self.benifits[1]
       spawnRegion.water += self.benifits[2]
       spawnRegion.farmGood += self.benifits[3]


   def beginBuilding(self):
       spawnRegion.resources -= self.resourceCost
       spawnRegion.food -= self.foodCost




class Megaproject:


   def __init__(self, resourceCost, foodCost, benifit):
       self.resourceCost = resourceCost
       self.foodCost = foodCost
       self.benifit = benifit


   def beginBuilding(self):
       spawnRegion.resources -= self.resourceCost
       spawnRegion.food -= self.foodCost


   def built(self):
       spawnRegion.foodProduction += self.benifit[0]
       spawnRegion.terrainLevel -= self.benifit[1]
       spawnRegion.water += self.benifit[2]
       spawnRegion.farmGood += self.benifit[3]
       if spawnRegion.terrainLevel <= 0:
           spawnRegion.terrainLevel = 0
       if spawnRegion.farmGood >= 10:
           spawnRegion.farmGood = 10
       if spawnRegion.water >= 10:
           spawnRegion.water = 10


class Resources:

    def __init__(self, name, benifit, benifitValue, easeOfProduction, tradeCostBase):
        self.name = name
        self.benifit = benifit
        self.benifitValue = benifitValue
        self.easeOfProduction = easeOfProduction
        self.tradeCostBase = tradeCostBase


iron = Resources("iron", ["production"], [2], 0.5, 3)
copper = Resources("copper", ["production"], [1], 1, 1.5)
woodBenifits = ["production", "food"]
woodBenifitValues = [1, 5]
wood = Resources("wood", woodBenifits, woodBenifitValues, 3, 0.5)
horse = Resources("horse", ["explore"], [2], 1, 2)
salt = Resources("salt", ["food"], [10], 0.5, 3)
gold = Resources("gold", ["none"], [0], 0.5, 10)
stone = Resources("stone", ["production"], [4], 2, 2)
resourceOptions = [iron, copper, wood, horse, salt, gold, stone]

spawnTerrainLevel = random.randrange(int(0.5 * difficulty), 10)
spawnTerrain = random.choice(biomeOptions)
spawnResource = random.choice(resourceOptions)
spawnWater = random.randrange(int(5 - (0.5 * difficulty)), int(10 - (0.5 * difficulty)))
spawnFarmGood = random.randrange(int(5 - (0.5 * spawnTerrainLevel)), int(10 - (0.5 * difficulty)))
spawnRegion = Region(spawnTerrain, spawnTerrainLevel, spawnResource, spawnWater, spawnFarmGood, True, "")
spawnRegion.startup()
omnipot = Omipotent(omnipotBen, omnipotAct)
turn = 0

megaprojects = []
newRiverBenifits = [0, 0, 2, 0]
newRiver = Megaproject(40, 20, newRiverBenifits)
megaprojects.append(newRiver)
flattenRegionBenifits = [0, 3, 0, 0]
flattenRegion = Megaproject(20, 40, flattenRegionBenifits)
megaprojects.append(flattenRegion)
fertilizeLandBenifits = [0, 0, 0, 3]
fertilizeLand = Megaproject(50, 30, fertilizeLandBenifits)
megaprojects.append(fertilizeLand)


buildings = []
farmHouseBenifits = [5, 0, 0, 1]
farmHouse = Building(10, 5, farmHouseBenifits, "Farm House food production is increased by 5, farm ability is increased by 1, costs 10 resources and 5 food.")
buildings.append(farmHouse)
mineBenifits = [0, 2, 0, 0]
mine = Building(5, 10, mineBenifits, "Mine +2 resource production per turn, costs 5 resources and 10 food.")
buildings.append(mine)
canalsBenifits = [0, 0, 2, 1]
canals = Building(20, 10, canalsBenifits, "Canals +2 water level in " + spawnRegion.name + ", costs 20 resources and 10 food.")
buildings.append(canals)




def explore(prowess, difficulty):
   raiseChance = (random.randrange(1, 10) * (3 * random.random() * 0.5 * prowess))
   raiseOdds = (random.randrange(0, 100) + difficulty)
   exploreRoll = (random.randrange(int(prowess), 100) - difficulty)
   if raiseChance >= raiseOdds:
       exploreRoll += 10 + (0.5 * prowess)
   if exploreRoll <= 10:
       print("Your explorers have mysteriously disappeared, lose 10 population.")
       spawnRegion.inhabitants -= 10
   elif exploreRoll <= 30:
       print("Your explorers have returned unsuccessful, nothing happens.")
   elif exploreRoll <= 50:
       wandererGain = random.randrange(0, 3) + int(3 * (0.5 * prowess))
       print("Your explorers have found some wanderers who decided to join "
             "you, gain " + str(wandererGain) + " regional population")
       spawnRegion.inhabitants += wandererGain
       spawnRegion.food += wandererGain * 2
   elif exploreRoll <= 70:
       exploreFood = (0.5 * (exploreRoll - 50)) + (prowess * 2) + random.randrange(0, 5)
       print("Your explorers have found some food, gain " + str(exploreFood) + " food in " + spawnRegion.name + ".")
       spawnRegion.food += exploreFood
   elif exploreRoll <= 90:
       exploreResources = (exploreRoll - 70) + prowess
       print("Your explorers have found some abandoned building resources,"
             " gain " + str(exploreResources) + " resources in " + spawnRegion.name + ".")
   elif exploreRoll <= 100:
       print("Your explorers fell asleep under a tree and had a strange dream.")
   elif exploreRoll > 100:
       print("Congrats, your explorers are awesome, +10 food, pops and resources")
       spawnRegion.food += 30
       spawnRegion.resources += 10
       spawnRegion.inhabitants += 10
   input("\n\nPress enter to move on\n")




def whatToDo():
   print("\n\n\nActions for this turn:")
   if spawnRegion.inhabitants >= 10:
       print("    1. Explore")
   else:
       print("    1. Explore -- unavailable, you need at least 10 pops")
   print("    2. Build")
   print("    3. Improve Region (for late game)")
   print("    4. More Statistics")
   print("    5. Skip turn")
   choice = ""
   while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
      choice = input("\nWhat would you like to do?\n")
   choice = int(choice)
   while choice < 1 or choice > 5:
       choice = int(input("\nInvalid choice, what would you like to do?\n"))
   if choice == 1 and spawnRegion.inhabitants >= 10:
       explore(player.prowess, difficulty)
   elif choice == 1 and spawnRegion.inhabitants < 10:
       print("Like I said, you don't have enough people.")
       whatToDo()
   if choice == 2:
       build()
   if choice == 3:
       improveRegion()
   if choice == 4:
       statsForNerds()
   if choice == 5:
       skip = 0
       while skip != 1 and skip != 2:
           print("Are you sure you would like to skip your turn?\n    1. Yes\n    2. No")
           skip = int(input())
           if skip == 1:
               pass
           if skip == 2:
               whatToDo()




def statsForNerds():
   print("Your regional stats are currently:")
   print("Water:          " + str(spawnRegion.water))
   print("Farm ability:   " + str(spawnRegion.farmGood))
   print("Terrain suitability   " + str(10 - spawnRegion.terrainLevel))
   print("You win when all of these stats are 10.")
   input("\n\nPress enter to continue.")
   whatToDo()




def build():
   print(spawnRegion.name + " has the following buildings built:")
   for b in spawnRegion.buildings:
       print(b)
   time.sleep(0.25)
   print("Which building would you like to build")
   cannotBuild = []
   canBuild = []
   # Checks if building is built
   for c in buildings:
       for h in spawnRegion.buildings:
           if h == c.name:
               cannotBuild.append(c)
   # If building is not built, adds it to a list
   for i in buildings:
       if i not in cannotBuild:
           canBuild.append(i)
           time.sleep(0.25)
   if len(canBuild) == 0:
       print("Oops, you can't build anything")
       time.sleep(0.25)
       whatToDo()
   else:
       numdone = 0
       for i in canBuild:
           numdone += 1
           print("    " + str(numdone) + ". " + str(i.name))
       print("\n")
       buildChoice = int(input())
       toBuild = canBuild[(buildChoice - 1)]
       if toBuild.foodCost > spawnRegion.food or toBuild.resourceCost > spawnRegion.resources:
           print("oops you don't have enough to build that")
           whatToDo()
       else:
           toBuild.beginBuilding()
           toBuild.built()
           spawnRegion.buildings.append(toBuild.name)
           input("The building has been built, press enter to continue.\n")




def turnFoodGain():
   spawnRegion.food -= spawnRegion.inhabitants
   exessFood = spawnRegion.food
   spawnRegion.food += spawnRegion.foodProduction
   return exessFood




def turnResourceGain():
   spawnRegion.resources += spawnRegion.resourceProduction


turnGameEnd = 0


def improveRegion():
   print("Your regional stats are currently:")
   print("Water:          " + str(spawnRegion.water))
   print("Farm ability:   " + str(spawnRegion.farmGood))
   print("Terrain suitability:   " + str(10 - spawnRegion.terrainLevel))
   time.sleep(0.25)
   print("\n\nHere are your options:")
   print("    1. Dig a new river, costs 40 resources and 20 food, raises water by 2.")
   print("    2. Flatten the lands around us, costs 20 resources and 40 food, raises terrain suitability by 3.")
   print("    3. Fertilize the Land, costs 50 resources and 30 food, raises farm ability by 3.")
   print("    4. Return to main screen")
   choice = int(input("What would you like to do?\n"))
   if choice > 0 and choice < 4:
       if megaprojects[choice - 1].resourceCost <= spawnRegion.resources and megaprojects[choice - 1].foodCost <= spawnRegion.food:
           megaprojects[choice - 1].beginBuilding()
           megaprojects[choice - 1].built()
       else:
           print("Oops, you don't have the resources to do that!")
           whatToDo()
   else:
       whatToDo()


global win
win = 0

def mainScreen(turn):
   print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
   spawnRegion.updateRegionJobs()
   spawnRegion.updateRegion()
   turn += 1
   if turn != 1:
       exessFood = turnFoodGain()
       if exessFood > 10:
           exessFood = 10
       popgain = int(0.02 * exessFood * spawnRegion.inhabitants)
       if popgain < -10:
           popgain = -10
       spawnRegion.inhabitants += popgain
       turnResourceGain()
   else:
       popgain = 0
   if spawnRegion.inhabitants < 10 and spawnRegion.inhabitantsLastTurn < 10:
       randomizer = random.randrange(0, 2)
       if randomizer == 1:
          print("\n\nSome wandering people have come by your region and found it to their liking\nYou gained 5 population\n\n")
          spawnRegion.inhabitants += 5
   gainedpops = spawnRegion.inhabitants - spawnRegion.inhabitantsLastTurn
   if gainedpops < 0:
       while len(spawnRegion.pops) > spawnRegion.inhabitants:
           toKill = random.choice(spawnRegion.pops)
           toKill.kill()
        #   pass
       #pass
   else:
       while len(spawnRegion.pops) < spawnRegion.inhabitants + gainedpops:
           spawnRegion.popBorn("James who was born")
   print("Turn " + str(turn))
   time.sleep(0.25)
   print("\n\nStats:")
   print("Population:   " + str(spawnRegion.inhabitants))
   print("Food:         " + str(spawnRegion.food))
   print("Resources:    " + str(spawnRegion.resources) + " units of " + spawnRegion.resource.name)
   time.sleep(0.25)
   print("\n\nYou gain:")
   print(str(spawnRegion.foodProduction) + " food every turn")
   print(str(spawnRegion.resourceProduction) + " resource every turn")
   print("And last turn you gained " + str(gainedpops) + " inhabitants in " + spawnRegion.name + ".")
   spawnRegion.inhabitantsLastTurn = spawnRegion.inhabitants
   time.sleep(0.25)
   whatToDo()
   global win
   global turnGameEnd
   if spawnRegion.terrainLevel == 0 and spawnRegion.farmGood == 10 and spawnRegion.water == 10 and win == 0:
       turnGameEnd = turn
       turn = toplay
       win = 1
   if spawnRegion.inhabitants <= 0:
       turnGameEnd = turn
       turn = toplay + 51
       win = -1
   return turn




while turn < toplay:
   print(random.choice(spawnRegion.pops).work.Benifits)
   print(spawnRegion.jobBenifits)
   #print(spawnRegion.resourceProduction)
   #print(spawnRegion.jobBenifits[1])
   turn = mainScreen(turn)
   for i in spawnRegion.pops:
       spawnRegion.inhabitants = 1
   
if win == 1:
    time.sleep(1)
    print("Congrats, you win! It took you " + str(turnGameEnd) + " turns!")
elif win == -1:
    print("Oops, you lost, better luck next time.")
else:
    print("You either ran out of turns or broke the game. \n\nPS. You lost the game") 