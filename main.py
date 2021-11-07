# WELCOME TO OUR OP CODE
import subprocess as sp
from pyfiglet import figlet_format
import time
import random
from PIL import Image
import timg
import keyboard

gameOver = 0

# declare puzzle finishes
dunwichTreasure = 0
kilerthTreasure = 0
orrinshireTreasure = 0
rochdaleTreasure = 0
nulbaramTreasure = 0


def showMap():
    if kilerthTreasure == 0 and dunwichTreasure == 0:
        print("                              ,-.^._                    _")
        print("                            .'      `-.                 ,' ;")
        print("          /`-.       ,----'          `-.      _  ,-.,'  `;")
        print("       _.'      `--'                   `-' '-'             ;")
        print("      :                     o                              ;__,-.")
        print("      ,'     o           Kilerth                                ;_,-',.__'--.")
        print("     :    Dunwich                                                   ,--````--'")
        print("     :                                                              :")
        print("     :                                                              :")
        print("     :                                                              ;")
        print("    (                                                               ;")
        print("     `-.                                                     o     ,'")
        print("       ;                                                Orrinshire :")
        print("     .'                                                    (WIP).-._,'")
        print("   .'                                                         ..`.")
        print("_.'                                                       .__;")
        print("`._                                        o            ;")
        print("    `.                                 Rochdale:,       :           .--------------------.")
        print("      `., ..__, ---._;                  (WIP)    ,._,--._;           |      Astoria       |")
        print("                      `-.__:                    :                   |  Capital: Dunwich  |")
        print("                            `.--.____;_________:                    |    Pop: 12700000   |")
        print("                                                                    | Area: 250000 sq.mi.|")
        print("                                                                    |   (647500 sq.km.)  |")
        print("                                                                    `--------------------'")

    elif dunwichTreasure == 1:
        if kilerthTreasure == 1 and dunwichTreasure == 1:
            print("                              ,-.^._                    _")
            print("                            .'      `-.                 ,' ;")
            print("          /`-.       ,----'          `-.      _  ,-.,'  `;")
            print("       _.'      `--'                   `-' '-'             ;")
            print("      :                     √                              ;__,-.")
            print("      ,'     √           Kilerth                                ;_,-',.__'--.")
            print("     :    Dunwich                                                   ,--````--'")
            print("     :                                                              :")
            print("     :                                                              :")
            print("     :                                                              ;")
            print("    (                                                               ;")
            print("     `-.                                                     o     ,'")
            print("       ;                                                Orrinshire :")
            print("     .'                                                    (WIP).-._,'")
            print("   .'                                                         ..`.")
            print("_.'                                                       .__;")
            print("`._                                        o            ;")
            print("    `.                                 Rochdale:,       :           .--------------------.")
            print("      `., ..__, ---._;                  (WIP)    ,._,--._;           |      Astoria       |")
            print("                      `-.__:                    :                   |  Capital: Dunwich  |")
            print("                            `.--.____;_________:                    |    Pop: 12700000   |")
            print("                                                                    | Area: 250000 sq.mi.|")
            print("                                                                    |   (647500 sq.km.)  |")
            print("                                                                    `--------------------'")

        print("                              ,-.^._                    _")
        print("                            .'      `-.                 ,' ;")
        print("          /`-.       ,----'          `-.      _  ,-.,'  `;")
        print("       _.'      `--'                   `-' '-'             ;")
        print("      :                     o                              ;__,-.")
        print("      ,'     √           Kilerth                                ;_,-',.__'--.")
        print("     :    Dunwich                                                   ,--````--'")
        print("     :                                                              :")
        print("     :                                                              :")
        print("     :                                                              ;")
        print("    (                                                               ;")
        print("     `-.                                                     o     ,'")
        print("       ;                                                Orrinshire :")
        print("     .'                                                    (WIP).-._,'")
        print("   .'                                                         ..`.")
        print("_.'                                                       .__;")
        print("`._                                        o            ;")
        print("    `.                                 Rochdale:,       :           .--------------------.")
        print("      `., ..__, ---._;                  (WIP)    ,._,--._;           |      Astoria       |")
        print("                      `-.__:                    :                   |  Capital: Dunwich  |")
        print("                            `.--.____;_________:                    |    Pop: 12700000   |")
        print("                                                                    | Area: 250000 sq.mi.|")
        print("                                                                    |   (647500 sq.km.)  |")
        print("                                                                    `--------------------'")

    elif kilerthTreasure == 1:
        if dunwichTreasure == 1 and kilerthTreasure == 1:
            print("                              ,-.^._                    _")
            print("                            .'      `-.                 ,' ;")
            print("          /`-.       ,----'          `-.      _  ,-.,'  `;")
            print("       _.'      `--'                   `-' '-'             ;")
            print("      :                     √                              ;__,-.")
            print("      ,'     √           Kilerth                                ;_,-',.__'--.")
            print("     :    Dunwich                                                   ,--````--'")
            print("     :                                                              :")
            print("     :                                                              :")
            print("     :                                                              ;")
            print("    (                                                               ;")
            print("     `-.                                                     o     ,'")
            print("       ;                                                Orrinshire :")
            print("     .'                                                    (WIP).-._,'")
            print("   .'                                                         ..`.")
            print("_.'                                                       .__;")
            print("`._                                        o            ;")
            print("    `.                                 Rochdale:,       :           .--------------------.")
            print("      `., ..__, ---._;                  (WIP)    ,._,--._;           |      Astoria       |")
            print("                      `-.__:                    :                   |  Capital: Dunwich  |")
            print("                            `.--.____;_________:                    |    Pop: 12700000   |")
            print("                                                                    | Area: 250000 sq.mi.|")
            print("                                                                    |   (647500 sq.km.)  |")
            print("                                                                    `--------------------'")
        print("                              ,-.^._                    _")
        print("                            .'      `-.                 ,' ;")
        print("          /`-.       ,----'          `-.      _  ,-.,'  `;")
        print("       _.'      `--'                   `-' '-'             ;")
        print("      :                     √                              ;__,-.")
        print("      ,'     o           Kilerth                                ;_,-',.__'--.")
        print("     :    Dunwich                                                   ,--````--'")
        print("     :                                                              :")
        print("     :                                                              :")
        print("     :                                                              ;")
        print("    (                                                               ;")
        print("     `-.                                                     o     ,'")
        print("       ;                                                Orrinshire :")
        print("     .'                                                    (WIP).-._,'")
        print("   .'                                                         ..`.")
        print("_.'                                                       .__;")
        print("`._                                        o            ;")
        print("    `.                                 Rochdale:,       :           .--------------------.")
        print("      `., ..__, ---._;                  (WIP)    ,._,--._;           |      Astoria       |")
        print("                      `-.__:                    :                   |  Capital: Dunwich  |")
        print("                            `.--.____;_________:                    |    Pop: 12700000   |")
        print("                                                                    | Area: 250000 sq.mi.|")
        print("                                                                    |   (647500 sq.km.)  |")
        print("                                                                    `--------------------'")


def TestForLevelUp():
    if Player1.exp >= Player1.maxExp:
        tempExp = Player1.exp - Player1.maxExp
        Player1.LevelUp()
        Player1.exp = tempExp
    if Player2.exp >= Player2.maxExp:
        tempExp = Player2.exp - Player2.maxExp
        Player2.LevelUp()
        Player2.exp = tempExp


def ChooseCity():

    print("Choose where you want to go:")
    if dunwichTreasure == 0:
        print("1. Dunwich")
    else:
        print("1. Dunwich √")

    if kilerthTreasure == 0:
        print("2. Kilerth")
    else:
        print("2. Kilerth √")

    if dunwichTreasure == 1 and kilerthTreasure == 1:
        print("3. Nulbaram")

    cityOption = int(input())

    if cityOption == 1:
        Dunwich()

    if cityOption == 2:
        Kilerth()

    if cityOption == 3:
        Nulbaram()



def Kilerth():
    print(Player1.name + " and " + Player2.name + " travel north in search of a treasure chest.")
    time.sleep(5)
    print("As it gets dark, you both enter the town of Kilerth.")
    time.sleep(5)
    print("The town looks barren, with just a few cottages, a store, and a cafeteria.")
    time.sleep(5)
    print("You both decide to rest for the night, and ask the townspeople for a place to stay.")
    time.sleep(5)
    if Player1.hp != Player1.maxHp or Player2.hp != Player2.maxHp:
        print("They allow you to stay, seeing that you both are beaten up.")
        Player1.hp = int(Player1.maxHp)
        Player2.hp = int(Player2.maxHp)
    else:
        print("Although both of you are not hurt, they allow you to rest.")
        time.sleep(5)
    sp.call('cls', shell=True)
    print(figlet_format("DAY 2", font="big"))
    input("Press Enter to Continue...")
    sp.call('cls', shell=True)
    print("As dawn breaks, you both prepare to leave the cottage.")
    time.sleep(4)
    print("Before you both leave, the townsperson tells you about a cave that no one has come back alive from.")
    time.sleep(4)
    print("He offers a piece of an ancient treasure map for clearing the cave.")
    time.sleep(4)
    print("He offers a wooden sword to both of you for protection from monsters.")
    time.sleep(4)
    print("It's too dangerous to go alone! Take this!")
    time.sleep(4)
    print("You both acquired wooden sword! Attack increased by 1!")
    Player1.atk = Player1.atk + 1
    Player2.atk = Player2.atk + 1
    time.sleep(4)
    print("You both enter the dark cave. The sound of water trickling grows louder.")
    time.sleep(4)
    print(Player1.name + " notices some weird blue goop on the walls as you go deeper in the cave.")
    time.sleep(4)
    print("A slime suddenly forms from the goop!")
    time.sleep(4)
    sp.call('cls', shell=True)
    tutorialSlime(0, "Blue Slime", 10, 10, 2, 300, 35)
    if gameOver == 0:
        print("The slime bursts back into the little blobs and retreats.")
        time.sleep(4)
        print("You both chase the goop deeper into the cave.")
        time.sleep(4)
        print("You both enter a large room. The ground starts rumbling.")
        time.sleep(4)
        print("Suddenly, the goop forms together to form a giant slime.")
        time.sleep(4)
        sp.call('cls', shell=True)
        tutorialSlime(0, "Enormous Slime", 25, 25, 4, 1500, 40)
        if gameOver == 0:
            print("The goop disintegrates, and the cave becomes clean.")
            time.sleep(4)
            print("The slime leaves behind a magic mushroom. Hp increases by 10! Health Restored!")
            Player1.maxHp = Player1.maxHp + 10
            Player2.maxHp = Player2.maxHp + 10
            Player1.hp = Player1.maxHp
            Player2.hp = Player2.maxHp
            print("You both exit the cave and go back to the townsperson.")
            time.sleep(4)
            print("Townsperson: Great job! You guys are amazing! No one has been able to clear it out! Here is your "
                  "reward.")
            time.sleep(4)
            print("You both acquired a piece of the ancient treasure map!")
            global kilerthTreasure
            kilerthTreasure = 1
            time.sleep(4)
            print("You both leave the town.")
        elif gameOver == 1:
            print(figlet_format("GAME OVER", font="big"))
    elif gameOver == 1:
        print(figlet_format("GAME OVER", font="big"))
    ChooseCity()


def Dunwich():  # +yeti fight if we have time     baby slime 7 hp 1 atk, 100 exp
    print(Player1.name + " and " + Player2.name + " decide to go to Dunwich to the NorthWest.")
    time.sleep(4)
    print("While traveling to Dunwich, the first thing you notice is the heavy snowfall forming around the path.")
    time.sleep(4)
    print("The snow slowly increases around you both, slowly decreasing your vision")
    time.sleep(4)
    print("You can no longer see anything farther than 5 meters ahead of you")
    time.sleep(4)
    print("Your vision consists of only white, when suddenly...")
    time.sleep(2)
    print("THE GROUND OPENS UP BENEATH YOU AND YOU BOTH FALL IN")
    time.sleep(0.6)
    print(".")
    time.sleep(0.6)
    print(".")
    time.sleep(0.6)
    print(".")
    time.sleep(0.6)
    print(".")
    time.sleep(0.6)
    print(".")
    time.sleep(0.6)
    print(".")
    time.sleep(0.6)
    print(".")
    time.sleep(0.6)
    print(figlet_format("BOOM", font="big"))
    time.sleep(2)
    sp.call('cls', shell=True)
    print(".")
    time.sleep(1)
    sp.call('cls', shell=True)
    print("..")
    time.sleep(1)
    sp.call('cls', shell=True)
    print("...")
    time.sleep(1)
    print("Both of you get up")
    time.sleep(4)
    print("Somehow, none of you had gotten hurt.")
    time.sleep(4)
    print("But there doesn't seem to be any way to get back up")
    time.sleep(4)
    print(Player2.name + " notices a door behind both of you")
    time.sleep(4)
    print("A worn down sign above the door frame reads: ")
    sp.call('cls', shell=True)
    print(figlet_format("DUNWICH", font="big"))
    time.sleep(4)
    sp.call('cls', shell=True)
    print(Player1.name + " opens the door leading to a long and dark hallway")
    time.sleep(4)
    print("Both of you look around to see what little you can see")
    time.sleep(4)
    print("The walls around you look old and worn down, yet look more advanced than a typical city.")
    time.sleep(4)
    print("You reach a well lit room with vibrant murals on all four walls.")
    time.sleep(4)
    print("You hear a loud clank from behind you...")
    time.sleep(4)
    print("The door behind you is closed and you are now trapped in the Dunwich Mural Room")
    time.sleep(4)
    print("In front of both of you appears a password lock on a door. " + Player2.name + "notices that the lock is "
                                                                                         "numbered 1 - 10.")

    time.sleep(4)
    print("You both try to guess a random number.")
    time.sleep(4)
    sp.call('cls', shell=True)

    # CODE TIME WOAH
    trapped = 1
    while trapped == 1:

        randNum = random.randint(1, 10)  # takes a random number from 1 - 10 over and over again

        print("Guess a number from 1-10.")
        userInput = int(input())

        if randNum == userInput:
            print("The lock opens, and reveals a chest behind the door. In the chest is a piece of an ancient "
                  "treasure map.")
            trapped = 0

        else:
            print("A tile from the mural opens up, and two arrows shoot out of hit hitting both of you for 1 damage "
                  "each!")
            Player1.hp = Player1.hp - 1
            Player2.hp = Player2.hp - 1

    print("You both acquired a piece of an ancient treasure map!")
    global dunwichTreasure
    dunwichTreasure = 1
    ChooseCity()


def Nulbaram():
    print("THIS CITY ISN'T OUT YET SORRY")


def tutorialSlime(tutorialArea, name, hp, maxHp, atk, exp, hitChance):
    # bbdddbdbdbbdbdbdbdbdb ENEMY ENCOUTNERERRR
    # Test multiplayer fighting with slime
    slime = Slime(name, hp, maxHp, atk, exp)
    sp.call('cls', shell=True)
    while (Player1.hp > 0 or Player2.hp > 0) and (slime.hp > 0):

        # Playerturn()
        # calculates if they are defending
        playerDef = [0, 0]
        playerAtk = [0, 0]

        # Does loop for both players: i = 0 = Player1; i = 1 = Player2
        for i in range(2):
            # displays enemy's health

            slime.EnemyStats()

            fighting = 1
            while fighting == 1:

                print(" ")
                print("It is " + str(PlayerList[i].name) + "'s turn")
                print(" ")
                print("Choose an action (number):")
                print("1: Attack")
                print("2: Defend")
                print("3: Item")
                print("4: Check Stats")

                fightOption = int(input())

                if fightOption == 1:
                    sp.call('cls', shell=True)
                    print(str(PlayerList[i].name + " charges up their attack!"))
                    playerAtk[i] = 1
                    fighting = 0

                elif fightOption == 2:
                    sp.call('cls', shell=True)
                    print(PlayerList[i].name + " is now defending!")
                    playerDef[i] = 1
                    fighting = 0

                elif fightOption == 3:
                    sp.call('cls', shell=True)
                    if not PlayerItemList[i]:
                        print("You do not own any items...")
                    else:
                        print("You have an item pouch, but the brain capacity to open it")

                elif fightOption == 4:
                    keepLoop = "a"
                    while keepLoop != "":
                        sp.call('cls', shell=True)
                        PlayerList[i].CurrentStats()
                        print(" ")
                        print("Press Enter to get back to fighting!")
                        keepLoop = input()

                if fightOption < 1 or fightOption > 4:
                    print("Please input a number from 1-4")
                time.sleep(2)
                sp.call('cls', shell=True)

        # Slime dialogue
        if tutorialArea == 1:
            if int(slime.hp) == 10:
                print("The " + slime.name + " jiggles excitedly!")
            elif int(slime.hp) >= 8:
                print("The " + slime.name + " is happy someone is playing with them!")
            elif int(slime.hp) >= 5:
                print("The " + slime.name + " stops wiggling...")
            elif int(slime.hp) >= 2:
                print("The " + slime.name + " starts shaking nervously")
            elif int(slime.hp) >= 1:
                print("The " + slime.name + " wants to run away...")
            time.sleep(2)

        if playerAtk[0] == 1:
            print("The " + slime.name + " takes " + str(PlayerList[0].atk) + " damage by " + str(
                PlayerList[0].name) + "!")
            slime.hp = slime.hp - PlayerList[0].atk
        if playerAtk[1] == 1:
            print("The " + slime.name + " takes " + str(PlayerList[1].atk) + " damage by " + str(
                PlayerList[1].name) + "!")
            slime.hp = slime.hp - PlayerList[1].atk

        # Slime's Turn
        if slime.hp > 0:
            print("The " + slime.name + " charges its attack... ")
            time.sleep(2)
            if random.randint(1, 100) <= hitChance:
                print("IT HITS!")
                time.sleep(1)

                # if Player 1 did not defend, they get hit
                if playerDef[0] == 0:
                    print(str(Player1.name) + " takes " + str(slime.atk) + " damage!")
                    Player1.hp = int(Player1.hp) - int(slime.atk)

                # if Player 1 did defend, they block the attack
                else:
                    print(str(Player1.name) + " blocks the attack!")

                # if Player 2 did not defend, they get hit
                if playerDef[1] == 0:
                    print(str(Player2.name) + " takes " + str(slime.atk) + " damage!")
                    Player2.hp = int(Player2.hp) - int(slime.atk)

                # if Player 2 did defend, they
                else:
                    print(str(Player2.name) + " blocks the attack!")
                time.sleep(2)

            else:
                print("It misses!")
                time.sleep(2)

            sp.call('cls', shell=True)

        elif tutorialArea == 1:
            print("D:")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            sp.call('cls', shell=True)
            print(figlet_format("You...", font="big"))
            time.sleep(2)
            print(figlet_format("MURDERER", font="big"))
            time.sleep(2)
            sp.call('cls', shell=True)
            print(figlet_format("THAT POOR SLIME", font="big"))
            time.sleep(2)

    if Player1.hp <= 0 and Player2.hp <= 0:
        sp.call('cls', shell=True)
        print("You died! what a loser LOL")
        gameOver = 1

    elif slime.hp <= 0:
        time.sleep(1)
        sp.call('cls', shell=True)
        print("You won!")
        time.sleep(1)
        print("You have gained...")
        time.sleep(1)
        print(str(slime.exp) + " exp each!")
        time.sleep(3)
        Player1.exp = Player1.exp + slime.exp
        Player2.exp = Player2.exp + slime.exp

        #Test Level up system!!!
        TestForLevelUp()


class Player:
    def __init__(self, name, hp, maxHp, exp, maxExp, level, atk, mana, maxMana):
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.exp = exp
        self.maxExp = maxExp
        self.level = level
        self.atk = atk
        self.mana = mana
        self.maxMana = maxMana

    # function for displaying current stats
    def CurrentStats(self):
        print("Hello " + str(self.name) + ", Your current stats are:")
        print("hp: " + str(self.hp) + "/" + str(self.maxHp))
        print("exp: " + str(self.exp))
        print("exp needed to level up: " + str(self.maxExp - self.exp))
        print("level: " + str(self.level))
        print("atk: " + str(self.atk))
        print("mana: " + str(self.mana) + "/" + str(self.maxMana))
        print(" ")

    def LevelUp(self):

        self.maxHp = self.maxHp + 5
        self.hp = self.maxHp
        self.level = self.level + 1
        self.atk = self.atk + 1
        self.exp = 0
        self.maxExp = self.maxExp + 500
        print(self.name + " leveled up!")
        self.CurrentStats()


class Enemy:
    def __init__(self, name, hp, maxHp, atk, exp):
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.atk = atk
        self.exp = exp

    def EnemyStats(self):
        print("A " + str(self.name) + " appears!")
        print("Hp: " + str(self.hp) + "/" + str(self.maxHp))
        print("Atk: " + str(self.atk))

    def EnemyHit(self, hitDmg):
        self.hp = int(self.hp - hitDmg)


class Slime(Enemy):
    def __init__(self, name, hp, maxHp, atk, exp):
        super().__init__(name, hp, maxHp, atk, exp)
        # Enemy.__init>>(self, name, hp, atk)  is the same thing


# Introduce Player
sp.call('cls', shell=True)
print("Input your Name!")
username1 = input()
print(" ")
Player1 = Player(username1, 10, 10, 0, 500, 1, 2, 10, 10)
player1Items = []
print("Hello, " + username1 + "!")
time.sleep(2)
sp.call('cls', shell=True)

# Menu for Game
print("Welcome to Astoria!")
print("Select your option:")
print("1. Story Mode")
print("2. PVP Mode (WIP)")
print("3. Quit")
# makes a faux boolean
x = 1
# Checks for second player
hasPlayer2 = 0

# loop to see what the user wants to play
while x == 1:
    # takes the user input
    menuOption = int(input())

    # tests if its a value between 1 and 3
    if 0 < menuOption < 4:

        # Code branches out for different options
        x = 2  # stops the line 20 while loop

        sp.call('cls', shell=True)
        # branch to story mode
        if menuOption == 1:
            # outputs the prompt
            print("Select your option:")
            print("1. Single Player")
            print("2. Multiplayer")

            x = 1  # is the loop maker <faux boolean>

            # makes sure that the user inputs a valid number: 1 or 2
            while x == 1:
                menuOption = int(input())
                if 0 < menuOption < 3:
                    x = 2
                    sp.call('cls', shell=True)
                    # branch to single player
                    if menuOption == 1:
                        print("Welcome" + username1 + ", to the world of Astoria!!!!")

                    # branch to multi player
                    if menuOption == 2:
                        print("What is the name of player 2?")
                        username2 = input()
                        print(" ")
                        Player2 = Player(username2, 10, 10, 0, 500, 1, 2, 10, 10)
                        PlayerList = [Player1, Player2]
                        player2Items = []
                        PlayerItemList = [player1Items, player2Items]
                        print("Hello, " + username2 + "!")
                        hasPlayer2 = 1
                        time.sleep(2)
                        sp.call('cls', shell=True)

                # reminds person to put a valid number
                else:
                    print("Please input a valid number")

        # branch to PVP mode
        elif menuOption == 2:
            print("WORK IN PROGRESS")

        # quits the game
        elif menuOption == 3:
            print("Goodbye!")

    # yells at the player because they're stupid!
    else:
        print("Please input a valid number")

if menuOption == 1:
    print("WORK IN PROGRESS")
    print(" ")
elif menuOption == 2:
    time.sleep(1)
    print(
        "You both are in the kitchen eating your favorite cereal, Atomic Asteroids, when " + username1 + " notices a "
                                                                                                         "game on the"
                                                                                                         " back of "
                                                                                                         "the box.")
    time.sleep(5)
    print("The game turns out to be a treasure hunt. " + username2 + " notices a red 'Start!' button on the bottom of "
                                                                     "the box.")
    time.sleep(5)
    print("You both press the button, and are teleported to the world of Astoria.")
    time.sleep(5)

    enter = 1
    while enter != "":
        anim1 = 0
        sp.call('cls', shell=True)
        print(figlet_format("Astoria", font='big'))
        print("")
        time.sleep(2)
        print("Press Enter to continue...")
        enter = input()

    sp.call('cls', shell=True)
    print("You both wake up in the middle of a grassy plain. You both see a path in the distance, but there is a "
          "forest in the way.")
    time.sleep(5)
    print(username2 + " follows " + username1 + " into the forest. You find a happy slime.")
    time.sleep(5)
    print("Slime: *happy blub blub blub*")
    time.sleep(5)
    print("Would you like to attack the slime?")
    print("1. Attack (Tutorial)")
    print("2. Let it go (Skip Tutorial)")
    menuOption = int(input())

    x = 1
    while x == 1:
        if menuOption == 1:
            x = 2
            print("You both attack the harmless slime.")
            tutorialSlime(1, "Tutorial Slime", 10, 10, 1, 200, 20)
            if gameOver == 0:
                sp.call('cls', shell=True)
                print("You both destroy the slime into smithereens and continue down the path.")
                time.sleep(5)
            elif gameOver == 1:
                print(figlet_format("GAME OVER", font="big"))

        elif menuOption == 2:
            x = 2
            print("You both leave the slime alone, and watch it hop away into the forest.")
        else:   
            print("Please input a valid number.")
            menuOption = int(input())

    print("After continuing on the path, you both leave the forest. You both see a sign and a map.")
    time.sleep(5)
    showMap()
    time.sleep(5)
    print("The sign points in 2 different directions with different city names.")
    time.sleep(5)
    sp.call('cls', shell=True)
    ChooseCity()